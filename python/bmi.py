import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Index : 0 - Extremely Weak 1 - Weak 2 - Normal 3 - Overweight 4 - Obesity 5 - Extreme Obesity


def trained_model(fname):
    # Load data from CSV file
    df = pd.read_csv('bmi.csv')

    # Calculate BMI
    # df['bmi'] = df['weight'] / (df['height'] / 100) ** 2

    # Define input and output variables
    X = df[['Gender', 'Height', 'Weight', 'Index']]
    y = df['Nutritant']

    # Convert categorical variables to binary
    X = pd.get_dummies(X, columns=['Gender'])

    print(X)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = model.predict(X_test)

    # Evaluate model performance
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)

    # new_data = [[189, 110, 3, 0, 1]]
    y_pred = model.predict(fname)

    print('Predicted nutrition classifications:')
    print(y_pred)

    return y_pred
