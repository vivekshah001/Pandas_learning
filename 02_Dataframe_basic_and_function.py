
# 📍 Section 1: Creating & Inspecting DataFrames

# Create a DataFrame from:
# a list of lists
# a dictionary
# a CSV file (create a small dummy CSV yourself)
# Then print:.shape, .dtypes, .index, .columns, .values


import numpy as np
import pandas as pd

a=[1,2,3,4,45]
student={
    "name":["vivek","mannu","raj","sachin","dhannu","golu"],
    "Rollno":[11,22,33,44,55,66],
    "package":[8,3,5,3,5,3]
}


from_list=pd.DataFrame(a)
dictionary=pd.DataFrame(student)
print(from_list)


print(pd.read_csv("my_data.csv"))

print(dictionary.shape)
print(dictionary.dtypes)
print(dictionary.index)
print(dictionary.columns)
print(dictionary.values)
print(dictionary.rename(columns={"name":"Name","Rollno":"roll_no","package":"Package"}))



"""           # Show the first 3 and last 2 rows.
# Randomly sample 4 rows using sample()"""

print(dictionary.head(3))
print(dictionary.tail(2))
print(dictionary.sample(4))



''' Select:
A single column (df['col'])
Multiple columns (df[['col1', 'col2']])'''


print(dictionary["name"])
print(dictionary[["name","package"]])


''' Select:
1st, 3rd, 5th rows using iloc
rows with index labels 'a', 'c', 'e' using loc'''


print(dictionary.iloc[0::2])


# to get row by loc we need to first set name as index
print(dictionary.set_index("name"))
print(dictionary.loc[:3,"name":"Rollno"])



''' Select both rows and specific columns using .loc & .iloc combos.
Example: only rows 2-5 and columns Age, City.'''


# print(dictionary.iloc[1:4,"name"])
