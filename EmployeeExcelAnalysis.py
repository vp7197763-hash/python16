import pandas as pd

# Load Excel file
df = pd.read_excel("employee.xlsx")

print("\n--- Employee Data ---")
print(df)

# a) Employees in Automotive domain
print("\nEmployees in Automotive Department:")
print(df[df['Department'] == 'Automotive'])

# b) Details of employee by ID
emp_id = int(input("\nEnter Employee ID: "))
print("\nEmployee Details:")
print(df[df['Employee ID'] == emp_id])

# c) List of Developers
print("\nList of Developers:")
print(df[df['Designation'] == 'Developer'])