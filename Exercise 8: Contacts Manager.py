
# Exercise 8: Contacts Manager 
# The main exercise we were given was to just allow users to add, 
# remove, and view there contacts; however, I also included other 
# helpful things like while loop, for loop, etc... to make it more 
# beneficial and responsive.  

contacts = []

def add_contact():
  name = input("\nWhat is the person's name?")
  phone_num = input("\nWhat is their phone number?")
  contact_info = f"C{len(contacts) + 1}: {name}, {phone_num}"
  contacts.append(contact_info)
  print("\nContact added, thank you!")
  
def view_contacts():
  if not contacts:
    print("\nNo contacts found.")
  else:
    print("Here are your contacts:")
    for contact in contacts:
      print(f"  {contact}")

def remove_contact():
  entry = int(input("Which contact do you want to remove? Enter the ID number like 1 or 2"))
  while (entry > len(contacts)) or (entry <= 0):
    print("You can't remove a nonexistent contact")
    entry = int(input("Which contact do you want to remove? Enter the ID number like 1 or 2"))
  contacts.pop(entry - 1)
  print("\nContact removed, thank you!")
  

def reinitialize():
  while True:
    yes_no = input("\nDo you want to continue? (yes/no)")
    if yes_no.lower() == "no":
      print("\nHave a nice day!")
      return False
    elif yes_no.lower() == "yes":
      return True
    else:
      print("\nPlease enter either yes or no")
    
    
while True:
  user_input = input("\nWelcome! Press 1 to add a new contact, 2 to view your contacts, and 3 to remove a contact.")
  if user_input.isdigit():
    user_input = int(user_input)
  else:
    print("Please enter a valid number")
    continue
  
  if user_input == 1:
    add_contact()
  elif user_input == 2:
    view_contacts()
  elif user_input == 3:
    remove_contact()
  else: 
    print("\nPlease choose a correct option")
    
  if not reinitialize():
    break
  
