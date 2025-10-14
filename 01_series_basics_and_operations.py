
import numpy as np
import pandas as pd


# Create a Pandas Series from this list: [10, 20, 30, 40, 50].
# Check its data type and index.
# Change the index to ['a','b','c','d','e'].

series1=pd.Series([10, 20, 30, 40, 50],index=['a','b','c','d','e'])
print(type(series1))
print(series1)





# Given a Series of temperatures in Celsius: [0, 10, 20, 30, 40], convert it to Fahrenheit using vectorized operations.

series2=pd.Series([0, 10, 20, 30, 40])
farrenheit=  (9/5 *series2)+32
print(farrenheit)



# Create a Series of 10 random integers between 1 and 100.
# Find the maximum, minimum, and mean.
# Check which values are above 50.

series3=pd.Series(np.random.randint(1,100,size=10))
print(series3)
print("mean is :",series3.mean())
print("min :",series3.min())
print("max:",series3.max())
print(series3>50)





# Create a Series from this dictionary: {'Math': 90, 'Physics': 80, 'Chemistry': 85, 'Biology': 70}.
# Select only subjects where marks are above 80.
# Increase all marks by 5 using vectorized addition.


series4=pd.Series({'Math': 90
                   , 'Physics': 80
                   , 'Chemistry': 85
                   , 'Biology': 70}

)

print(series4[series4>80])
print(series4 +5)





# Given a Series of numbers [5, 10, 15, 20, 25], do the following:
# Multiply every number by 2.
# Subtract 3 from every number.
# Filter numbers that are divisible by 5.

series5=pd.Series([5, 10, 15, 20, 25])
print(series5*2)
print(series5 -3)
print(series5 % 5==0)



# Create a Series of 15 random integers and:
# Sort it in descending order.
# Reset its index after sorting.
# Identify the top 3 values.


series6=pd.Series(np.random.randint(1,100,size=15))
# print(series6)
print(series6.sort_values())
print(series6.head())





# Create a Series with 20 numbers where 5 are duplicates.
# Find the duplicate values.
# Count the occurrences of each number.



series7=pd.Series([1,2,3,4,5,6,6,7,7,8,8,9,9,10,10,11,23,45,67,43])
print(series7.duplicated())
print(series7.value_counts())



# Create a Series of 10 floats and round them to 2 decimal places.
# Replace values greater than 0.5 with 1.
# Replace values less than or equal to 0.5 with 0.



series8=pd.Series([0.2332,2.7325,2.2652,0.27223,9.4563,0.3736,9.3636])
print(series8.round(2))
print(np.where(series8>0.5,1))