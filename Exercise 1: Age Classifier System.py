
# Exercise 1: Age Classifier System
age = int(input("Enter your age"))
def classify_person(age):
  match age:
    case _ if 65 <= age:
      print("\nSenior")
    case _ if 18 <= age <= 64:
      print("\nAdult")
    case _ if 13 <= age <= 17:
      print("\nTeenager")
    case _ if 0 <= age <= 12:
      print("\nChild")
    case _:
      print("\nYou're not born yet")
classify_person(age)

