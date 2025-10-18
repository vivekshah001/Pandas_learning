
import pandas as pd

# Employee Info
employees = pd.DataFrame({
    "EmpID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Riya", "Vikram", "Sara", "Anil"],
    "Dept": ["IT", "HR", "IT", "Finance", "HR"]
})

# Salary Info
salaries = pd.DataFrame({
    "EmpID": [1, 2, 4, 6],
    "Salary": [50000, 60000, 70000, 80000]
})

# Project Assignments
projects = pd.DataFrame({
    "ProjectID": [101, 102, 103, 104],
    "EmpID": [1, 3, 4, 5],
    "Project": ["Alpha", "Beta", "Gamma", "Delta"]
})

# Bonus Data (different column name)
bonus = pd.DataFrame({
    "EmployeeID": [2, 3, 5, 6],
    "Bonus": [5000, 4000, 3000, 2000]
})

# New Employees (for concat)
new_employees = pd.DataFrame({
    "EmpID": [6, 7],
    "Name": ["Karan", "Neha"],
    "Dept": ["IT", "Finance"]
})


# print(employees)
# print(salaries)
# print(projects)
# print(bonus)
# print(new_employees)


#-------------------------------------------------------------------------------------------------------------------------
# Merge Practice --------------------------------------------------------------------------------------------------------

# Merge employees and salaries inner join on EmpID.

# print(pd.merge(employees,salaries,on="EmpID",how="inner"))



# Merge employees and salaries left join on EmpID.

# print(pd.merge(employees,salaries,on="EmpID",how="left"))



# Merge employees and projects to get all employees, even if they have no projects (hint: left join).

# print(pd.merge(employees,projects,on="EmpID",how="left"))


# Merge employees and bonus where EmpID in employees matches EmployeeID in bonus.

# print(pd.merge(employees,bonus,left_on="EmpID",right_on="EmployeeID"))


# Merge employees, salaries, and projects into one DataFrame — keep all employees, fill missing values with 0.

# print(pd.merge(employees,salaries,on="EmpID",how="left").merge(projects,on="EmpID"))



#-------------------------------------------------------------------------------------------------------------------------
#Concat Practice-----------------------------------------------------------------------------------------------------

# Vertically concatenate employees and new_employees.

# print(pd.concat([employees,new_employees],axis=0))


# Horizontally concatenate employees and salaries — watch out for index mismatch.

# print(pd.concat([employees,salaries],axis=1,ignore_index=False))

# Concat employees and projects row-wise, notice the missing columns.

# print(pd.concat([employees,projects],axis=0))
# notice kya change karna hai kya

# Combine employees, new_employees, and salaries vertically, then reset index.

print(pd.concat([employees,new_employees,salaries],axis=0,ignore_index=True))