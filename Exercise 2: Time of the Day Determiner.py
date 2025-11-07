
# Exercise 2: Time of the day Determiner
time = int(input("Enter the time of the day"))
def time_classifier(time):
  match time:
    case _ if (21 <= time < 24) or (0 <= time <= 4):
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
