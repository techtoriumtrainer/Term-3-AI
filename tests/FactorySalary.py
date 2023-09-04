import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from joblib import dump, load
import numpy as np

class ModelFactory:
    @staticmethod
    def get_model(model_name):
        if model_name == 'Linear Regression':
            return LinearRegression()
        elif model_name == 'Support Vector Machine':
            return SVR()
        elif model_name == 'Random Forest':
            return RandomForestRegressor()
        elif model_name == 'Gradient Boosting Regressor':
            return GradientBoostingRegressor()
        elif model_name == 'XGBRegressor':
            return XGBRegressor()
        else:
            raise ValueError(f"Model '{model_name}' not recognized!")

def load_data(file_name):
    return pd.read_excel(file_name)

def preprocess_data(data):
    X = data.drop(['Customer Name', 'Customer e-mail', 'Country', 'Car Purchase Amount'], axis=1)
    Y = data['Car Purchase Amount']
    
    sc = MinMaxScaler()
    X_scaled = sc.fit_transform(X)
    
    sc1 = MinMaxScaler()
    y_reshape = Y.values.reshape(-1, 1)
    y_scaled = sc1.fit_transform(y_reshape)
    
    return X_scaled, y_scaled, sc, sc1

def split_data(X_scaled, y_scaled):
    return train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

def train_models(X_train, y_train):
    model_names = [
        'Linear Regression',
        'Support Vector Machine',
        'Random Forest',
        'Gradient Boosting Regressor',
        'XGBRegressor'
    ]
    
    models = {}
    for name in model_names:
        model = ModelFactory.get_model(name)
        model.fit(X_train, y_train.ravel())
        models[name] = model
        
    return models

def evaluate_models(models, Test_X, Test_Y):
    rmse_values = {}
    
    for name, model in models.items():
        preds = model.predict(Test_X)
        rmse_values[name] = mean_squared_error(Test_Y, preds, squared=False)
        
    return rmse_values

def plot_model_performance(rmse_values):
    plt.figure(figsize=(10,7))
    models = list(rmse_values.keys())
    rmse = list(rmse_values.values())
    bars = plt.bar(models, rmse, color=['blue', 'green', 'red', 'purple', 'orange'])

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.00001, round(yval, 5), ha='center', va='bottom', fontsize=10)

    plt.xlabel('Models')
    plt.ylabel('Root Mean Squared Error (RMSE)')
    plt.title('Model RMSE Comparison')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def save_best_model(models, rmse_values):
    best_model_name = min(rmse_values, key=rmse_values.get)
    best_model = models[best_model_name]
    dump(best_model, "car_model.joblib")

def predict_new_data(loaded_model, sc, sc1):
    Test_X1 = sc.transform(np.array([[0,42,62812.09301,11609.38091,238961.2505]]))
    pred_value = loaded_model.predict(Test_X1)
    print(pred_value)
    
    # Ensure pred_value is a 2D array before inverse transform
    if len(pred_value.shape) == 1:
        pred_value = pred_value.reshape(-1, 1)

    print("Predicted output: ", sc1.inverse_transform(pred_value))

if __name__ == "__main__":
    data = load_data('C:/Users/harra/Documents/Term-3-AI/Car_Purchasing_Data.xlsx')
    X_scaled, y_scaled, sc, sc1 = preprocess_data(data)
    X_train, Test_X, y_train, Test_Y = split_data(X_scaled, y_scaled)
    models = train_models(X_train, y_train)
    rmse_values = evaluate_models(models, Test_X, Test_Y)
    plot_model_performance(rmse_values)
    save_best_model(models, rmse_values)
    loaded_model = load("car_model.joblib")
    predict_new_data(loaded_model, sc, sc1)
