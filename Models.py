import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, MultiTaskLasso
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the dataset
dataset_path = "C:/Users/harra/Desktop/Term-3-AI/Car_Purchasing_Data.xlsx"
df = pd.read_excel(dataset_path)

# Features: Gender, Age, Annual Salary
X = df[['Gender', 'Age', 'Annual Salary']]
y = df['Car Purchase Amount']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)
linear_pred = linear_reg.predict(X_test)
linear_mse = mean_squared_error(y_test, linear_pred)

# Ridge Regression
ridge_reg = Ridge(alpha=1.0)
ridge_reg.fit(X_train, y_train)
ridge_pred = ridge_reg.predict(X_test)  
ridge_mse = mean_squared_error(y_test, ridge_pred)

# Lasso Regression
lasso_reg = Lasso(alpha=1.0)
lasso_reg.fit(X_train, y_train)
lasso_pred = lasso_reg.predict(X_test)
lasso_mse = mean_squared_error(y_test, lasso_pred)

# Multi-task Lasso Regression
multi_task_lasso_reg = MultiTaskLasso(alpha=1.0)
multi_task_lasso_reg.fit(X_train, np.column_stack((y_train, y_train)))  # Duplicate y_train for demonstration
multi_task_lasso_pred = multi_task_lasso_reg.predict(X_test)
multi_task_lasso_mse = mean_squared_error(y_test, multi_task_lasso_pred[:, 0])  # Use only one of the tasks

# Polynomial Regression
degree = 2  # Set the degree of the polynomial
poly = PolynomialFeatures(degree=degree)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train)
poly_pred = poly_reg.predict(X_test_poly)
poly_mse = mean_squared_error(y_test, poly_pred)

# Create subplots for each regression model
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('Regression Model Comparisons', fontsize=16)

# Linear Regression Plot
axs[0, 0].scatter(y_test, linear_pred)
axs[0, 0].set_title('Linear Regression')
axs[0, 0].set_xlabel('True Values')
axs[0, 0].set_ylabel('Predicted Values')

# Ridge Regression Plot
axs[0, 1].scatter(y_test, ridge_pred)
axs[0, 1].set_title('Ridge Regression')
axs[0, 1].set_xlabel('True Values')
axs[0, 1].set_ylabel('Predicted Values')

# Lasso Regression Plot
axs[0, 2].scatter(y_test, lasso_pred)
axs[0, 2].set_title('Lasso Regression')
axs[0, 2].set_xlabel('True Values')
axs[0, 2].set_ylabel('Predicted Values')

# Multi-task Lasso Regression Plot
axs[1, 0].scatter(y_test, multi_task_lasso_pred[:, 0])
axs[1, 0].set_title('Multi-task Lasso Regression')
axs[1, 0].set_xlabel('True Values')
axs[1, 0].set_ylabel('Predicted Values')

# Polynomial Regression Plot
axs[1, 1].scatter(y_test, poly_pred)
axs[1, 1].set_title(f'Polynomial Regression (degree={degree})')
axs[1, 1].set_xlabel('True Values')
axs[1, 1].set_ylabel('Predicted Values')

# Remove empty subplot
fig.delaxes(axs[1, 2])

# Adjust layout for better spacing
plt.tight_layout()
plt.subplots_adjust(top=0.9)

# Show all the plots
plt.show()