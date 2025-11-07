
# Exercise 4: Simple Unit Converter
temp_input = float(input("What is the temperature?"))
unit_input = input("\nWhat is the unit? (type either 'C' or 'F')")

def temp_unit_converter(temp, unit):
  if unit.lower() == "f":
    new_value = round(((5/9) * (temp - 32)), 2)
    print(f"\nYour temperature ({temp}°F) is equal to {new_value}°C.")
  elif unit.lower() == "c":
    new_value = round(((9/5) * (temp) + 32), 2)
    print(f"\nYour temperature ({temp}°C) is equal to {new_value}°F.")
  else: 
    print("\nEnter a correct unit")

temp_unit_converter(temp_input, unit_input)  
