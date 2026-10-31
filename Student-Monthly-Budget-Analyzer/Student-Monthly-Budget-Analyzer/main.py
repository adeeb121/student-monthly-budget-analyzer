# Student Monthly Budget Analyzer

name = input("Enter your name: ")
Monthly_income  = int(input("Enter your Monthly income : "))
Rent = int(input("Enter your Rent: "))
Food_expenses = int(input("Enter your Food expenses: "))
Travel_expenses = int(input("Enter your Travel expenses: "))
Study_materials = int(input("Enter your Entertainment expenses: "))
Other_expenses = int(input("Enter your Other expenses: "))
Total_expenses = Rent + Food_expenses + Travel_expenses + Study_materials + Other_expenses 
Remaining_money = Monthly_income - Total_expenses
Saving_percentage = (Remaining_money/Monthly_income)*100

print("===== MONTHLY EXPENSE REPORT ===== ")
print("Name:",name)
print("Monthly Income:",Monthly_income)
print("Total Expenses:",Total_expenses  )
print("Remaining Money:",Remaining_money)
print("Savings Percentage:",Saving_percentage)