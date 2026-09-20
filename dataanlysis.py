# pip install pandas
import pandas as pd

# Step 1: Create a sample employee.csv if you don't have Kaggle dataset

data = {
    'Name': ['Ravi', 'Teja', 'Priya', 'Asha', 'Vikram'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT'],
    'Salary': [60000, 45000, 75000, 50000, 80000]
}
df = pd.DataFrame(data)
df.to_csv('employee.csv', index=False)

# Step 2: Actual Project Code
df = pd.read_csv('employee.csv')
print(df)

# Calculate average salary
avg_salary = df['Salary'].mean()
print(f"\nAverage Salary: {avg_salary}")

# Department count
dept_count = df['Department'].value_counts()
print("\nDepartment Count:\n", dept_count)

# Filter employees above salary threshold (ex: 55000)
threshold = 55000
filtered = df[df['Salary'] > threshold]
print(f"\nEmployees with Salary > {threshold}:\n", filtered)

# Export results to new CSV
filtered.to_csv('high_salary_employees.csv', index=False)
print("\nExported to high_salary_employees.csv")