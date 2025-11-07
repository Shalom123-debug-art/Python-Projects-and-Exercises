
# Exercise 7: BMI Health Analyzer 
body_weight = float(input("Enter your body weight in kg"))
body_height = float(input("\nEnter your body height in m"))

def body_mass_index(weight, height):
  if weight <= 0:
    print("\nPlease enter a correct body weight")
    return
  
  if height <= 0:
    print("\nPlease enter a correct body height")
    return
  
  bmi = round((weight / height ** 2), 2)
  print(f"\nYour BMI is {bmi} kg/m²")
  
  if bmi >= 30:
    print("Obese")
  elif bmi >= 25:
    print("Overweight")
  elif bmi >= 18.5:
    print("Normal weight")
  else:
    print("Underweight")
    
body_mass_index(body_weight, body_height)



