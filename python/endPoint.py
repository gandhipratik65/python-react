from flask import Flask, jsonify, request
from bmi import *
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/get/ingredient', methods=['POST'])
def calculate_bmi():
    uuid = request.json['uuid']
    mealPreference = request.json['mealPreference']
    gender = request.json['gender']
    height = int(request.json['height'])
    weight = int(request.json['weight'])

    # perform calculations
    bmi = weight / ((height/100) ** 2)

    index = 0
    if bmi <= 17:
        index = 0
    elif bmi > 17 and bmi <= 18.5:
        index = 1
    elif bmi > 18.5 and bmi <= 23:
        index = 2
    elif bmi > 23 and bmi <= 30:
        index = 3
    elif bmi > 30 and bmi <= 35:
        index = 4
    elif bmi > 35:
        index = 5

    maleIndex = 0
    femaleIndex = 0
    if gender == 'Male':
        maleIndex = 1
        femaleIndex = 0
    elif gender == 'Female':
        femaleIndex = 1
        maleIndex = 0

    prediction = trained_model(
        [[height, weight, index, femaleIndex, maleIndex]])
    ingrdient = []
    if (mealPreference == 'Veg'):

        if prediction == 0:
            ingrdient = ['Apple', 'Tofu']
        elif prediction == 1:
            ingrdient = ['Brown Rice', 'Oats', 'Milk', 'Sweet Potatoes']
        elif prediction == 2:
            ingrdient = ['Gavar Aur Masoor Ki Dal', 'Jowar Methi Roti']
        elif prediction == 3:
            ingrdient = ['A Vegie Burger With made with a whole grain bun']
        elif prediction == 4:
            ingrdient = ['whole grains', 'legumes',
                         'nuts & seeds', 'avocado', 'olive oil']
        elif prediction == 5:
            ingrdient = ['beans', 'lentils', 'quinoa', 'tofu', 'nuts', 'seeds']

    elif (mealPreference == 'Non Veg'):
        if prediction == 0:
            ingrdient = ['Chicken Nuggets', 'Eggs']
        elif prediction == 1:
            ingrdient = ['Eggs', 'Chicken Breast', 'Shrimp']
        elif prediction == 2:
            ingrdient = ['Egg Omelete', 'Chicken Breast',
                         'Shrimp', 'Eggs', 'Turkey Breast']
        elif prediction == 3:
            ingrdient = ['Grilled Chicken Breast',
                         'Eggs Omelete', 'A grilled salmon']
        elif prediction == 4:
            ingrdient = ['poultry', 'fish & lean cuts of red meat']
        elif prediction == 5:
            ingrdient = ['chicken', 'fish', 'turkey', 'lean cuts of beef']

    # return results
    return jsonify({
        'ingrdient': ingrdient,
        'uuid': uuid,
        'mealPreference': mealPreference

    })


if __name__ == '__main__':
    app.run(debug=True)
