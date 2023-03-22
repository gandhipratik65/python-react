from flask import Flask, jsonify, request
from bmi import *

app = Flask(__name__)


@app.route('/calculate-bmi', methods=['POST'])
def calculate_bmi():
    age = request.json['age']
    gender = request.json['gender']
    height = request.json['height']
    weight = request.json['weight']

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

    result = trained_model([[height, weight, index, femaleIndex, maleIndex]])

    # return results
    return jsonify({
        'result': result
    })


if __name__ == '__main__':
    app.run(debug=True)
