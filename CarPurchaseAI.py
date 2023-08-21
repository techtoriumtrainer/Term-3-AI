import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import the data
dataset_path = "C:/Users/harra/Desktop/Term-3-AI/Car_Purchasing_Data.xlsx"
data = pd.read_excel(dataset_path)

# Display the first 5 rows of the dataset
print("First 5 rows:")
print(data.head())

# Display the last 5 rows of the dataset
print("\nLast 5 rows:")
print(data.tail())

# Determine the shape of the dataset (rows, columns)
rows, columns = data.shape
print("\nNumber of rows:", rows)
print("Number of columns:", columns)

# Display the concise summary of the dataset
print("\nConcise summary:")
print(data.info())

# Check for null values in the dataset
print("\nNull values:")
print(data.isnull().sum())

# Get overall statistics about the dataset
print("\nOverall statistics:")
print(data.describe())

#Matplotlib section

# Get overall statistics about the dataset
print("\nOverall statistics:")
print(data.describe())



# loading dataset 
data = sns.load_dataset("iris") 
  
# draw lineplot 
sns.lineplot(x="sepal_length", y="sepal_width", data=data) 
  
# setting the title using Matplotlib
plt.title('Title using Matplotlib Function')

plt.show()