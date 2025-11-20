
# Exercise: Student Membership Checker
students_list = ["Saul", "David", "James", "Moses"]
student_input = input("Enter the name of the student that you want to look up")

def student_name_checker(student):
  for i in range(len(students_list)):
    if student == students_list[i]:
      print("\nThe student you mentioned is found!")
      print(f"Student {i + 1} is {students_list[i]}")
      return
  print(f"\nThere's no student called {student} in the list.")
  
student_name_checker(student_input)

