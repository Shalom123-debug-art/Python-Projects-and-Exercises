
# Exercise 5: Tax Calculator 
income = float(input("Enter your gross income"))
def tax_calculator(gross_income):
  if gross_income > 14000:
    tax_rate = 0.35
  elif gross_income > 10000:
    tax_rate = 0.3
  elif gross_income > 7000:
    tax_rate = 0.25
  elif gross_income > 4000:
    tax_rate = 0.2
  elif gross_income > 2000:
    tax_rate = 0.15
  elif gross_income >= 0:
    tax_rate = 0
  else: 
    print("\nPlease enter a correct income amount")
    return
  
  total_tax = gross_income * tax_rate
  net_income = gross_income - total_tax
  print(f"\nTotal tax deducted from your income is {total_tax} birr and your net income is {net_income} birr.")

tax_calculator(income)
