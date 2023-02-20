import numpy as np
import pandas as pd


# We load Google stock data in a DataFrame
Google_stock = pd.read_csv('./goog-1.csv')

# We print some information about Google_stock
print('Google_stock is of type:', type(Google_stock))
print('Google_stock has shape:', Google_stock.shape)


print(Google_stock.head())
print(Google_stock.tail())
print(Google_stock.isnull().any())

# We get descriptive statistics on our stock data
print(Google_stock.describe())

# We get descriptive statistics on a single column of our DataFrame
print(Google_stock['Adj Close'].describe())


# We print information about our DataFrame  
print()
print('Maximum values of each column:\n', Google_stock.max())
print()
print('Minimum Close value:', Google_stock['Close'].min())
print()
print('Average value of each column:\n', Google_stock.mean())



# We display the correlation between columns
Google_stock.corr()


# We load fake Company data in a DataFrame
data = pd.read_csv('./fake-company.csv')

print(data)


# We display the total amount of money spent in salaries each year
print(data.groupby(['Year'])['Salary'].sum())



# We display the average salary per year
print(data.groupby(['Year'])['Salary'].mean())



# We display the total salary each employee received in all the years they worked for the company
print(data.groupby(['Name'])['Salary'].sum())


# We display the salary distribution per department per year.
print(data.groupby(['Year', 'Department'])['Salary'].sum())