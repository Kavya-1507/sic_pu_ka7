# Input
name = input("Enter name: ")
emp_id = input("Enter EmpID: ")
basic = float(input("Enter basic monthly salary: "))
allowance = float(input("Enter special allowance per month: "))
bonus_percent = float(input("Enter annual bonus percentage: "))

# Gross Salary Calculation
gross_monthly = basic + allowance
annual_gross = gross_monthly * 12
bonus = (bonus_percent / 100) * annual_gross
annual_gross += bonus

# Taxable Income
standard_deduction = 50000
taxable_income = annual_gross - standard_deduction

# Tax Slab Calculation
tax = 0
if taxable_income <= 300000:
    tax = 0
elif taxable_income <= 600000:
    tax = (taxable_income - 300000) * 0.05
elif taxable_income <= 900000:
    tax = 15000 + (taxable_income - 600000) * 0.10
elif taxable_income <= 1200000:
    tax = 45000 + (taxable_income - 900000) * 0.15
elif taxable_income <= 1500000:
    tax = 90000 + (taxable_income - 1200000) * 0.20
else:
    tax = 150000 + (taxable_income - 1500000) * 0.30

# Rebate
if taxable_income <= 700000:
    tax = 0

# Cess
cess = tax * 0.04
total_tax = tax + cess

# Net Salary
net_salary = annual_gross - total_tax

# Output
print("\n--- Employee Tax Report ---")
print("Name:", name)
print("EmpID:", emp_id)
print("Gross Monthly Salary: ₹", gross_monthly)
print("Annual Gross Salary: ₹", annual_gross)
print("Taxable Income: ₹", taxable_income)
print("Tax Payable: ₹", tax)
print("Cess (4%): ₹", cess)
print("Total Tax: ₹", total_tax)
print("Annual Net Salary: ₹", net_salary)
