

# Student Grade Analyzer
def initialize():
  user_desire = input("\nDo you want to analyze students' scores? (yes/no)")
  if user_desire.lower() == "yes":
    return True
  elif user_desire.lower() == "no":
    return False
  else:
    print("\nPlease enter either yes/no")
    return False
  
def get_grades():
  while True:
    try:
      num_of_grades = int(input("\nHow many students?"))
      while num_of_grades <= 0:
        print("\nPlease enter a correct number")
        num_of_grades = int(input("How many students?"))
      list_of_grades = []
      for grade in range(num_of_grades):
        single_grade = int(input(f"\nEnter grade for student {grade + 1}"))
        while (single_grade < 0) or (single_grade > 100):
          print("\nPlease enter a correct grade")
          single_grade = int(input(f"Enter grade for student {grade + 1}"))
        list_of_grades.append(single_grade)
      return list_of_grades
    except ValueError:
      print("Please type numerical values")

def analyze_and_display_grades(grades):
  if len(grades) > 0:
    average = round(sum(grades)/len(grades), 2)
  else:
    average = 0
  maximum = max(grades)
  minimum = min(grades)
  above_average = 0
  for i in range(len(grades)):
    if grades[i] > average:
      above_average+=1
  sorted_grades_list = sorted(grades)
  print("\n.....Results.....")
  print(f"Grades (sorted in ascending order): {sorted_grades_list}")
  print(f"Average Grade: {average}")
  print(f"Highest Grade: {maximum}")
  print(f"Lowest Grade: {minimum}")
  print(f"Students above average: {above_average}")
  print("\n==============")
  
if initialize():
  while True:
    grades = get_grades()
    if not grades:
      break
    analyze_and_display_grades(grades)
else:
  print("\nProgram ended. Goodbye!")
