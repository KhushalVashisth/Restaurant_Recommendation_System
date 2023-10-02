import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import re
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

current_directory = os.path.dirname(os.path.abspath(__file__))


data = pd.read_csv(os.path.join(current_directory, 'DelhiNCR Restaurants.csv.xls'))

data
print(data.isnull().sum())
data.info()
data.describe()
data=data.drop(['Dining_Review_Count','Delivery_Rating','Delivery_Rating_Count','Website','Address','Phone_No','Latitude','Longitude','Known_For2'],axis=1)
data
data.duplicated().sum()
data.drop_duplicates(inplace=True)
data.head()
data.isnull().sum()
data.dropna(how='any',inplace=True)
data.head()
data = data.rename(columns={'Restaurant_Name':'name','Category':'cuisines','Pricing_for_2':'cost','Locality':'location', 'Dining_Rating':'rating', 'Known_For22':'reviews_list'})
data.head()
data.name = data.name.apply(lambda x:x.title())
data['cost'] = data['cost'].astype(float)
restaurants = list(data['name'].unique())
data['Mean Rating'] = 0

for i in range(len(restaurants)):
    data['Mean Rating'][data['name'] == restaurants[i]] = data['rating'][data['name'] == restaurants[i]].mean()
data
data.loc[data.name =='Burma Burma']
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (1,5))
data[['Mean Rating']] = scaler.fit_transform(data[['Mean Rating']]).round(2)
data.head()
#Before Text Processing
data[['reviews_list', 'cuisines']].head()
#Lower Casing
data["reviews_list"] = data["reviews_list"].str.lower()

#Removal of Punctuations 
import string
punc = string.punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', punc))

data["reviews_list"] = data["reviews_list"].apply(lambda text: remove_punctuation(text))

#Removal of Stopwords
Stopwords = set(stopwords.words('english'))
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in Stopwords])

data["reviews_list"] = data["reviews_list"].apply(lambda text: remove_stopwords(text))

#Removal of URLS
def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

data["reviews_list"] = data["reviews_list"].apply(lambda text: remove_urls(text))
data[['reviews_list', 'cuisines']].head()
# Recommendation by Reviews
data
df_percent = data.sample(frac=1)
df_percent.set_index('name', inplace=True)
indices = pd.Series(df_percent.index)
tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=1, stop_words='english')
tfidf_matrix = tfidf.fit_transform(df_percent['reviews_list'])
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)


# def recommend_like(name, top_n=10, cosine_similarities=cosine_similarities):
#     recommend_restaurant = []
#     try:
#         idx = indices[indices == name].index[0]
#         score_series = pd.Series(cosine_similarities[idx])
#         top_indexes = list(score_series.iloc[1:top_n+1].index)

#         for each in top_indexes:
#             recommend_restaurant.append(list(df_percent.index)[each])

#         df_new = pd.DataFrame(columns=['cuisines', 'Mean Rating', 'cost'])

#         for each in recommend_restaurant:
#             selected_data = df_percent[['cuisines', 'Mean Rating', 'cost']][df_percent.index == each].sample()
#             df_new = pd.concat([df_new, selected_data])

#         df_new = df_new.drop_duplicates(subset=['cuisines', 'Mean Rating', 'cost'], keep=False)
#         df_new = df_new.sort_values(by='Mean Rating', ascending=False).head(top_n)

#         print(f'TOP {top_n} RESTAURANTS LIKE {name.upper()}: ')
#         df_new.reset_index(drop=True, inplace=True)
#         return df_new
#     except:
#         print('No restaurants with similar reviews.')


# def recommend_like(name, top_n=10, cosine_similarities=cosine_similarities):
#     recommend_restaurant = []
#     try:
#         idx = indices[indices == name].index[0]
#         score_series = pd.Series(cosine_similarities[idx])
#         top_indexes = list(score_series.iloc[1:top_n+1].index)

#         for each in top_indexes:
#             recommend_restaurant.append(list(df_percent.index)[each])

#         df_new = pd.DataFrame(columns=['name', 'cuisines', 'Mean Rating', 'cost'])
#         for each in recommend_restaurant:
#             selected_data = df_percent.loc[df_percent.index == each, ['cuisines', 'Mean Rating', 'cost']].sample()
#             selected_data['name'] = each 
#             df_new = pd.concat([df_new, selected_data])
#         df_new = df_new.drop_duplicates(subset=['name', 'cuisines', 'Mean Rating', 'cost'], keep=False)
#         df_new = df_new.sort_values(by='Mean Rating', ascending=False).head(top_n)

#         print(f'TOP RESTAURANTS LIKE {name.upper()}: ')
#         df_new.reset_index(drop=True, inplace=True)

#         # return df_new
#         return df_new.style.hide_index()
#     except:
#         print('No restaurants with similar reviews.')

# def recommend_like(name, top_n=10, cosine_similarities=cosine_similarities):
#     recommend_restaurant = []
#     try:
#         idx = indices[indices == name].index[0]
#         score_series = pd.Series(cosine_similarities[idx])
#         top_indexes = list(score_series.iloc[1:top_n+1].index)

#         for each in top_indexes:
#             recommend_restaurant.append(list(df_percent.index)[each])

#         df_new = pd.DataFrame(columns=['name', 'cuisines', 'Mean Rating', 'cost'])
#         for each in recommend_restaurant:
#             selected_data = df_percent.loc[df_percent.index == each, ['cuisines', 'Mean Rating', 'cost']].sample()
#             selected_data['name'] = each 
#             df_new = pd.concat([df_new, selected_data])
#         df_new = df_new.drop_duplicates(subset=['name', 'cuisines', 'Mean Rating', 'cost'], keep=False)
#         df_new = df_new.sort_values(by='Mean Rating', ascending=False).head(top_n)

#         print(f'TOP RESTAURANTS LIKE {name.upper()}: ')
#         # return df_new
#         return df_new[['name','cuisines','Mean Rating','cost']].to_dict("records")
#     except:
#         print('No restaurants with similar reviews.')
# def recommend_like(name, top_n=10, cosine_similarities=cosine_similarities):
#     recommend_restaurant = []
#     try:
#         idx = indices[indices == name].index[0]
#         score_series = pd.Series(cosine_similarities[idx])
#         top_indexes = list(score_series.iloc[1:top_n+1].index)

#         for each in top_indexes:
#             recommend_restaurant.append(list(df_percent.index)[each])

#         df_new = pd.DataFrame(columns=['name', 'cuisines', 'Mean Rating', 'cost'])
#         for each in recommend_restaurant:
#             # selected_data = df_percent.loc[df_percent.index == each, ['cuisines', 'Mean Rating', 'cost']].sample()
#             selected_data = df_percent.loc[df_percent.index == each, ['cuisines', 'Mean Rating', 'cost']].sample()
#             selected_data['name'] = each 
#             df_new = pd.concat([df_new, selected_data])
#             # df_new = pd.concat([df_new, selected_data.reset_index(drop=True)])
#             # df_new = pd.concat([df_new, selected_data], ignore_index=True)
#         df_new = df_new.drop_duplicates(subset=[ 'name','cuisines', 'Mean Rating', 'cost'], keep=False)
#         df_new = df_new.sort_values(by='Mean Rating', ascending=False).head(top_n)
#         # df_new = df_new.loc[:, ~df_new.columns.str.contains('^Unnamed')]
#         print(f'TOP RESTAURANTS LIKE {name.upper()}: ')
#         # df_new.style.hide_index()
#         # return df_new
#         df_new.reset_index(drop=True, inplace=True)
#         return df_new[['name','cuisines','Mean Rating','cost']].to_dict("records")
#     except:
#         print('No restaurants with similar reviews.')



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
            # selected_data = df_percent.loc[df_percent.index == each, ['cuisines', 'Mean Rating', 'cost']].sample()
            selected_data = df_percent.loc[df_percent.index == each, ['cuisines', 'Mean Rating', 'cost']].sample()
            selected_data['name'] = each 
            df_new = pd.concat([df_new, selected_data])
            # df_new = pd.concat([df_new, selected_data.reset_index(drop=True)])
            # df_new = pd.concat([df_new, selected_data], ignore_index=True)
        df_new = df_new.drop_duplicates(subset=[ 'name','cuisines', 'Mean Rating', 'cost'], keep=False)
        df_new = df_new.sort_values(by='Mean Rating', ascending=False).head(top_n)
        # df_new = df_new.loc[:, ~df_new.columns.str.contains('^Unnamed')]
        print(f'TOP RESTAURANTS LIKE {name.upper()}: ')
        # df_new.style.hide_index()
        # return df_new
        df_new.reset_index(drop=True, inplace=True)
        return df_new
    except:
        print('No restaurants with similar reviews.')


recommend_like('The Big Chill')
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
recommend_by_cuisine('Chinese')
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
    df_new.reset_index(drop=True, inplace=True)

    return df_new
recommend_by_cost(3000,4000)

model_functions_delhi = {
    'byRating': recommend_by_mean_rating,
    'byCuisine': recommend_by_cuisine,
    'byLike': recommend_like,
    'byCost': recommend_by_cost
}

with open('model_functions_delhi.pkl', 'wb') as f:
    pickle.dump(model_functions_delhi, f)