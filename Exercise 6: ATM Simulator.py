
# Exercise 6: ATM Simulator 
withdrawal_amount = float(input("Enter the amount you want to withdraw"))
def atm_withdrawal(amount):
  balance = 1000
  if amount > balance:
    print("\nYou can't withdraw more than what you have!")
    return
  elif amount < 0:
    print("\nYou can't withdraw negative amount of money!")
    return
  elif amount == 0:
    print("\nYou can't withdraw nothing!")
    return
  else:
    balance -= amount
    print(f"\nYou've withdrawn {amount} birr, and your current balance is {round(balance, 2)} birr.")

atm_withdrawal(withdrawal_amount)
