import pickle
from flask import Flask, request, jsonify
from bangalore import recommend_by_mean_rating
from bangalore import recommend_by_cost
from bangalore import recommend_by_cuisine
from bangalore import recommend_like
from delhi import recommend_by_mean_rating
from delhi import recommend_by_cost
from delhi import recommend_by_cuisine
from delhi import recommend_like
from flask_cors import CORS
import os
import json

current_directory = os.path.dirname(os.path.abspath(__file__))



with open(os.path.join(current_directory, 'model_functions.pkl'), 'rb') as file:
    loaded_function = pickle.load(file)
with open(os.path.join(current_directory, 'model_functions_delhi.pkl'), 'rb') as file_delhi:
    loaded_function_delhi = pickle.load(file_delhi)


app = Flask(__name__)
CORS(app)

@app.route('/get_recommendationsRating', methods=['POST'])
def get_recommendationsRating():
    user_data = request.json['user_data']  # Assuming user data is sent as JSON

    # recommendations = loaded_function['byRating'](user_data)
    byrating = loaded_function['byRating']
    recommendations = byrating(user_data)
    app.logger.info(recommendations)
    recommendations_json =  recommendations.to_json(orient='records')
    return jsonify({'recommendations': recommendations_json})
    # return jsonify({'recommendations': recommendations})

@app.route('/get_recommendationsRatingDelhi', methods=['POST'])
def get_recommendationsRatingDelhi():
    user_data = request.json['user_data']  # Assuming user data is sent as JSON

    # recommendations = loaded_function['byRating'](user_data)
    byrating = loaded_function_delhi['byRating']
    recommendations = byrating(user_data)
    app.logger.info(recommendations)
    recommendations_json =  recommendations.to_json(orient='records')
    # recommendations_json = json.dumps(recommendations)
    return jsonify({'recommendations': recommendations_json})
    # return jsonify({'recommendations': recommendations})













@app.route('/get_recommendationsCuisine', methods=['POST'])
def get_recommendationsCuisine():
    user_data = request.json['user_data']  # Assuming user data is sent as JSON

    # recommendations = loaded_function['byRating'](user_data)
    bycuisine = loaded_function['byCuisine']
    recommendations = bycuisine(user_data)
    app.logger.info(recommendations)
    recommendations_json =  recommendations.to_json(orient='records')
    return jsonify({'recommendations': recommendations_json})
    # return jsonify({'recommendations': recommendations})


@app.route('/get_recommendationsCuisineDelhi', methods=['POST'])
def get_recommendationsCuisineDelhi():
    user_data = request.json['user_data']  # Assuming user data is sent as JSON

    # recommendations = loaded_function['byRating'](user_data)
    bycuisine = loaded_function_delhi['byCuisine']
    recommendations = bycuisine(user_data)
    app.logger.info(recommendations)
    recommendations_json =  recommendations.to_json(orient='records')
    return jsonify({'recommendations': recommendations_json})
    # return jsonify({'recommendations': recommendations})












@app.route('/get_recommendationsLike', methods=['POST'])
def get_recommendationsLike():
    user_data = request.json['user_data']  # Assuming user data is sent as JSON

    # recommendations = loaded_function['byRating'](user_data)
    bylike = loaded_function['byLike']
    recommendations = bylike(user_data)

    selected_columns = ['name', 'cuisines', 'Mean Rating', 'cost']
    recommendations_selected = recommendations[selected_columns]

    app.logger.info(recommendations_selected)
    recommendations_json =  recommendations_selected.to_json(orient='records')
    return jsonify({'recommendations': recommendations_json})
    # return jsonify({'recommendations': recommendations})

@app.route('/get_recommendationsLikeDelhi', methods=['POST'])
def get_recommendationsLikeDelhi():
    user_data = request.json['user_data']  # Assuming user data is sent as JSON
    print(user_data)
    # recommendations = loaded_function['byRating'](user_data)
    bylike = loaded_function_delhi['byLike']
    recommendations = bylike(user_data)
    print(recommendations)
    recdata = recommendations[['name','cuisines','Mean Rating','cost']].to_dict("records")
    app.logger.info(recommendations)
    # recommendations_json =  recommendations.to_json(orient='records')
    recommendations_json = json.dumps(recdata)
    return jsonify({'recommendations': recommendations_json})

    # return jsonify({'recommendations': recommendations})

    # return jsonify({'recommendations': recommendations})





@app.route('/get_recommendationsCost', methods=['POST'])
def get_recommendationsCost():
    user_data1 = request.json['user_data1']  # Assuming user data is sent as JSON
    user_data2 = request.json['user_data2']
    # recommendations = loaded_function['byRating'](user_data)
    bycost = loaded_function['byCost']
    recommendations = bycost(user_data1,user_data2)
    app.logger.info(recommendations)
    recommendations_json =  recommendations.to_json(orient='records')
    return jsonify({'recommendations': recommendations_json})
    # return jsonify({'recommendations': recommendations})

@app.route('/get_recommendationsCostDelhi', methods=['POST'])
def get_recommendationsCostDelhi():
    user_data1 = request.json['user_data1']  # Assuming user data is sent as JSON
    user_data2 = request.json['user_data2']
    # recommendations = loaded_function['byRating'](user_data)
    bycost = loaded_function_delhi['byCost']
    recommendations = bycost(user_data1,user_data2)
    app.logger.info(recommendations)
    recommendations_json =  recommendations.to_json(orient='records')
    return jsonify({'recommendations': recommendations_json})
    # return jsonify({'recommendations': recommendations})




if __name__ == '__main__':
    app.run(debug=True)
















# from bangalore import recommend_by_cuisine
# from bangalore import recommend_like
# with open('model_functions.pkl', 'rb') as f:
#     loaded_data = pickle.load(f)

# loaded_data = pickle.load(open('C:/Users/Khush/Downloads/model_functions.pkl', 'rb'))
# your_function = getattr(bangalore, 'recommend_by_mean_rating', None)
# if your_function is not None and callable(your_function):
#     result = your_function('North Indian')
# else:
#     print("Function not found or not callable.")

# print("hiiii")

# print(dir(loaded_data))


# pickled_model = pickle.load(open('C:/Users/khush/Downloads/model_functions.pkl', 'rb'))
# pickled_model.model_functions('North Indian')


# user_data = 4
# recommendations = loaded_function(user_data)