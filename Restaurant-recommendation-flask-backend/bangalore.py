import numpy as np
import pandas as pd
import re
import warnings
warnings.filterwarnings('ignore')
import pickle
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import os 

current_directory = os.path.dirname(os.path.abspath(__file__))



data = pd.read_csv(os.path.join(current_directory, 'zomato.csv'))





data.head()
print(data.isnull().sum())
data.info()
data.describe()
data=data.drop(['url','dish_liked','phone'],axis=1)
data.head()
data.duplicated().sum()
data.drop_duplicates(inplace=True)
data.head()
data.isnull().sum()
data.dropna(how='any',inplace=True)
data.head()
data.isnull().sum()
data = data.rename(columns={'approx_cost(for two people)':'cost','listed_in(type)':'type', 'listed_in(city)':'city'})
data['cost'] = data['cost'].astype(str) 
data['cost'] = data['cost'].str.replace(',', '').astype(float)
data = data.loc[data.rate !='NEW']
data = data.loc[data.rate !='-'].reset_index(drop=True)
remove_slash = lambda x: x.replace('/5', '')
data.rate = data.rate.apply(remove_slash).str.strip().astype('float')
data.head()
data.name = data.name.apply(lambda x:x.title())
data.online_order.replace(('Yes','No'),(True, False),inplace=True)
data.book_table.replace(('Yes','No'),(True, False),inplace=True)
data.head()
restaurants = list(data['name'].unique())
data['Mean Rating'] = 0

for i in range(len(restaurants)):
    data['Mean Rating'][data['name'] == restaurants[i]] = data['rate'][data['name'] == restaurants[i]].mean()
data.head()
data.loc[data.name =='Jalsa']
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (1,5))
#X_scaled = ((X - X.min()) / (X.max() - X.min())) * (b - a) + a {Here, [a,b]=[1,5]}
data[['Mean Rating']] = scaler.fit_transform(data[['Mean Rating']]).round(2)
data.head()
# Some of the common text preprocessing / cleaning steps are:

# Lower casing,
# Removal of Punctuations,
# Removal of Stopwords and
# Removal of URLs
#Before Text Processing
data[['reviews_list', 'cuisines']].head()
#Lower Casing
data["reviews_list"] = data["reviews_list"].str.lower()
data[['reviews_list', 'cuisines']].head()
#Removal of Punctuations 
import string
punc = string.punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', punc))

data["reviews_list"] = data["reviews_list"].apply(lambda text: remove_punctuation(text))
data[['reviews_list', 'cuisines']].head()
#Removal of Stopwords
Stopwords = set(stopwords.words('english'))
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in Stopwords])

data["reviews_list"] = data["reviews_list"].apply(lambda text: remove_stopwords(text))
data[['reviews_list', 'cuisines']].head()
#Removal of URLS
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

data["reviews_list"] = data["reviews_list"].apply(lambda text: remove_urls(text))
data[['reviews_list', 'cuisines']].head()
# RESTAURANT NAMES:
list(data['name'].unique())
data.head()
data=data.drop(['address','rest_type', 'type', 'menu_item', 'votes'],axis=1)





# Recommendation by Reviews
df_percent = data.sample(frac=0.5)
df_percent.set_index('name', inplace=True)
indices = pd.Series(df_percent.index)
# Creating tf-idf matrix
tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=1, stop_words='english')
tfidf_matrix = tfidf.fit_transform(df_percent['reviews_list'])
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
# def recommend_like(name, top_n=10, cosine_similarities=cosine_similarities):
#     recommend_restaurant = []
#     idx = indices[indices == name].index[0]
#     score_series = pd.Series(cosine_similarities[idx])
#     top_indexes = list(score_series.iloc[1:top_n+1].index)
    
#     for each in top_indexes:
#         recommend_restaurant.append(list(df_percent.index)[each])
    
#     df_new = pd.DataFrame(columns=['cuisines', 'Mean Rating', 'cost'])
    
#     for each in recommend_restaurant:
#         selected_data = df_percent[['cuisines', 'Mean Rating', 'cost']][df_percent.index == each].sample()
#         df_new = pd.concat([df_new, selected_data])
    
#     df_new = df_new.drop_duplicates(subset=['cuisines', 'Mean Rating', 'cost'], keep=False)
#     df_new = df_new.sort_values(by='Mean Rating', ascending=False).head(top_n)
    
#     print(f'TOP {top_n} RESTAURANTS LIKE {name.upper()}: ')
#     df_new.reset_index(drop=True, inplace=True)
#     return df_new


def recommend_like(name, top_n=10, cosine_similarities=cosine_similarities):
    recommend_restaurant = []
    try:
        idx = indices[indices == name].index[0]
        score_series = pd.Series(cosine_similarities[idx])
        top_indexes = list(score_series.iloc[1:top_n+1].index)

        for each in top_indexes:
            recommend_restaurant.append(list(df_percent.index)[each])

        df_new = pd.DataFrame(columns=['name', 'cuisines', 'Mean Rating', 'cost'])
        for each in recommend_restaurant:
            selected_data = df_percent.loc[df_percent.index == each, ['cuisines', 'Mean Rating', 'cost']].sample()
            selected_data['name'] = each 
            df_new = pd.concat([df_new, selected_data])
        df_new = df_new.drop_duplicates(subset=['name', 'cuisines', 'Mean Rating', 'cost'], keep=False)
        df_new = df_new.sort_values(by='Mean Rating', ascending=False).head(top_n)

        print(f'TOP RESTAURANTS LIKE {name.upper()}: ')
        df_new.reset_index(drop=True, inplace=True)

        return df_new
    except:
        print('No restaurants with similar reviews.')




data.loc[(data.name == 'Jalsa')][:1]
recommend_like('Jalsa')





# Recommendation by Cuisine
df_percent = data.sample(frac=1)
df_percent.set_index('cuisines'.lower(), inplace=True) 
indices = pd.Series(df_percent.index)

from fuzzywuzzy import fuzz

# Create a mapping of normalized cuisine values to restaurant names
cuisine_mapping = {}
for index, row in data.iterrows():
    for cuisine in row['cuisines'].split(', '):
        normalized_cuisine = cuisine.lower()
        if normalized_cuisine not in cuisine_mapping:
            cuisine_mapping[normalized_cuisine] = []
        cuisine_mapping[normalized_cuisine].append(index)

def recommend_by_cuisine(criteria_value, top_n=10, cosine_similarities=cosine_similarities):
    recommend_restaurant = []
    normalized_criteria = criteria_value.lower()
    matching_restaurants = cuisine_mapping.get(normalized_criteria, [])

    for restaurant_index in matching_restaurants:
        recommend_restaurant.append(restaurant_index)

    df_new = pd.DataFrame(columns=['name', 'cuisines', 'Mean Rating', 'cost'])
    for each in recommend_restaurant:
        selected_data = data[['name', 'cuisines', 'Mean Rating', 'cost']][data.index == each].sample()
        df_new = pd.concat([df_new, selected_data])
    df_new = df_new.drop_duplicates(subset=['name', 'cuisines', 'Mean Rating', 'cost'], keep=False)
    df_new = df_new.sort_values(by='Mean Rating', ascending=False).head(top_n)

    print(f'TOP {top_n} RESTAURANTS WITH SIMILAR CUISINE: ')
    # df_new.set_index('name', inplace=True)
    df_new.reset_index(drop=True, inplace=True)
    return df_new
recommend_by_cuisine('North Indian')



# Recommendation by Rating
df_percent = data.sample(frac=1)
df_percent.set_index('Mean Rating', inplace=True) 
indices = pd.Series(df_percent.index)

def recommend_by_mean_rating(mean_rating_value, top_n=10):
    recommend_restaurant = data[data['Mean Rating'] >= mean_rating_value].index
    df_new = data.loc[recommend_restaurant, ['name', 'cuisines', 'Mean Rating', 'cost']]
    df_new = df_new.sample(frac=1) 
    df_new = df_new.head(top_n)
    print(f'TOP {top_n} RESTAURANTS WITH A MINIMUM RATING OF {mean_rating_value}: ')
    # df_new.set_index('name', inplace=True)
    df_new.reset_index(drop=True, inplace=True)
    return df_new
recommend_by_mean_rating(4)




# Recommendation by Cost
df_percent = data.sample(frac=1)
df_percent.set_index('cost', inplace=True)  
indices = pd.Series(df_percent.index)

def recommend_by_cost(min_value,max_value, top_n=10):
    recommend_restaurant = data[(data['cost'] > min_value) & (data['cost'] <= max_value)].index
    df_new = data.loc[recommend_restaurant, ['name', 'cuisines', 'Mean Rating', 'cost']]
    df_new = df_new.sample(frac=1) 
    df_new = df_new.head(top_n)
    print(f'TOP {top_n} RESTAURANTS IN THE PROVIDED RANGE: ')
    # df_new.set_index('name', inplace=True)
    # names = df_new.columns.tolist()
    print("hmmmm")
    # print(df_new)
    # print(names)
    print("no")
    # return names
    df_new.reset_index(drop=True, inplace=True)
    return df_new

recommend_by_cost(1000,2000)

# model_functions = recommend_by_mean_rating



# pickle.dump(model_functions, open('model.pkl', 'wb'))

model_functions = {
    'byRating': recommend_by_mean_rating,
    'byCuisine': recommend_by_cuisine,
    'byLike': recommend_like,
    'byCost': recommend_by_cost
}


# with open('model_functions.pkl', 'wb') as f:
#     pickle.dump(recommend_by_mean_rating, f)
with open('model_functions.pkl', 'wb') as f:
    pickle.dump(model_functions, f)