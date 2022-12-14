from operator import length_hint
import random
import csv
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import random
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



def training_validation(city_data):
    with open(f'DATA\weather_filled_training_{city_data}.csv') as csv_file:
        city = pd.read_csv(csv_file)

    with open(f'DATA\weather_test_{city_data}.csv') as csv_file:
        test_city = pd.read_csv(csv_file)
    city.drop("Unnamed: 0", inplace = True, axis = 1)


    print(city_data)
    for col in city.columns:
        print(col)
    X_COLS = [column for column in city.columns if (column != 'Date' and column != 'avg_demand')]
    X = city[X_COLS]
    y = city['avg_demand']
    X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=0.2, random_state=0)

    
    lm = LinearRegression()

    # Fit to the train dataset
    lm.fit(X_train, y_train)


    # HOW TO DETERMINE EFFECTIVENESS
    # alpha = intercept parameter (aka beta0)
    alpha = lm.intercept_

    # betas = coefficients
    betas = lm.coef_
    print('Intercept', alpha)
    print('Coefficients', betas)
    y_pred = lm.predict(X_validation)
    r2 = lm.score(X_validation, y_validation)
    mse = mean_squared_error(y_validation, y_pred)
    print('r2 = ', r2)
    print('mse = ', mse)


    print("\n\n================================================\n\n")

    # plotting true values against our predicted values
    plt.scatter(y_validation, y_pred, alpha=0.8)
    plt.grid()
    plt.title(f'Linear Regression Plot: {city_data}')
    plt.xlabel('Actual Energy Demand')
    plt.ylabel('Predicted Energy Demand')
    plt.savefig(f"Linear_Regression_Plot_{city_data}.png")
    plt.close() 

    # plot residuals
    residuals = y_validation - y_pred
    plt.scatter(y_pred, residuals, alpha=0.8)

    # plot the 0 line (we want our residuals close to 0)
    plt.plot([min(y_pred), max(y_pred)], [0,0], color='red')
    plt.grid()
    plt.title(f'Linear Regression Residual Plot: {city_data}')
    plt.xlabel('Fitted')
    plt.ylabel('Residual')

    plt.savefig(f"Residual_Plot_{city_data}.png")
    plt.close()
    
    return

training_validation('melbourne')
training_validation('sydney')
training_validation('brisbane')
