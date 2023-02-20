import pandas as pd

# What columns are in this dataset?
# Are there any missing values?
# What are the different types of values in each column?

df = pd.read_csv("chicago.csv")
print(df.head())  # start by viewing the first few rows of the dataset!

print()
print(df.columns)

print()
print(df.isnull().any())

print()
print(df.describe())

print()
print(df.info())


df['Start Time'] = pd.to_datetime(df['Start Time'])

print(df.head()) 
print(df['Start Time'].head()) 

df['hour'] = df['Start Time'].dt.hour
print()
print(df['hour'].head())

print()
print(df['Start Time'].head()) 


print()
print(df.head())  

print()
most_common_hour = df['hour'].mode()
print(most_common_hour)



# print value counts for each user type
user_types = df['User Type'].value_counts()

print(user_types)