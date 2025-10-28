# Python Exercises

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
      
# Exercise 2: Time of the day Determiner
time = int(input("Enter the time of the day"))
def time_classifier(time):
  match age:
    case _ if (21 <= time <= 24) or (1 <= time <= 4):
      print("\nNight")
    case _ if 17 <= time <= 20:
      print("\nEvening")
    case _ if 12 <= time <= 16:
      print("\nAfternoon")
    case _ if 5 <= time <= 11:
      print("\nMorning")
    case _:
      print("\nThe time can't be out of the 24 hours structure!")
time_classifier(time)

# Excerice 3: Divisbility Check Program
num = int(input("Enter a number"))
def divisibility_by_5_Checker(num):
  if (num % 5 == 0):
    print("\nDivisible by 5")
  else:
    print("\nNot divisible by 5")
divisibility_by_5_Checker(num)
  
