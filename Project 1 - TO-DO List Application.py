
# Project 1 - To-Do List Application
tasks = []
completed_tasks = []

def display_all_tasks():
  print("\n=== TO-DO LIST ===")
  if len(tasks) == 0:
    print(["No task has been added yet."])
  else: 
    print("Tasks to do")
    for i in range(len(tasks)):
      print(f"{i+1}. {tasks[i].capitalize()}")
  if len(completed_tasks) == 0:
    return
  else: 
    print("Completed tasks")
    for i in range(len(completed_tasks)):
      print(f"{i+1}. {completed_tasks[i].capitalize()}")
  
def add_new_tasks():
  user_input = input("\nEnter a task that you'd like to add")
  tasks.append(user_input.capitalize())
  display_all_tasks()
  print("Your task has been added, thank you!")
  
def remove_tasks():
  user_choice = input("\nType '1' if you want to remove a task by writing it or '2' if you want to remove it by its roll no.")
  if user_choice == "1":
    user_input_1 = input("\nEnter the task you want to remove")
    task_found = False
    for i in range(len(tasks)):
      if user_input_1.capitalize() == tasks[i]:
        tasks.remove(tasks[i])
        task_found = True
        display_all_tasks()
        print("Your task has been removed, thank you!")
        break
    if not task_found: 
      print("\nThere is no such task, please enter another one again")
  elif user_choice == "2":
    user_input_2 = input("\nEnter the roll no. of the task you want to remove")
    task_found = False
    for i in range(len(tasks)):
      if int(user_input_2) == (i+1):
        tasks.remove(tasks[i])
        task_found = True
        display_all_tasks()
        print("Your task has been removed, thank you!")
        break
    if not task_found: 
      print("\nThere is no such task, please enter another one again")
  else:
    print("\nPlease enter either 1 or 2")
  
def edit_existing_tasks():
  user_choice = input("\nType '1' if you want to edit a task by writing it it or '2' if you want to edit it by its roll no.")
  if user_choice == "1":
    user_input_1 = input("\nEnter the task you want to rewrite")
    task_found = False
    for i in range(len(tasks)):
      if user_input_1.capitalize() == tasks[i]:
        user_edited_version_1 = input("\nRewrite it here")
        tasks[i] = user_edited_version_1.capitalize()
        task_found = True
        display_all_tasks()
        print("Your task has been edited, thank you!")
        break
    if not task_found:
      print("\nThere is no such task, please enter another one again")
  elif user_choice == "2":
    user_input_2 = input("\nEnter the roll no. of the task you want to rewrite")
    task_found = False
    for i in range(len(tasks)):
      if int(user_input_2) == (i+1):
        user_edited_version_2 = input("\nRewrite it here")
        tasks[i] = user_edited_version_2.capitalize()
        task_found = True
        display_all_tasks()
        print("Your task has been edited, thank you!")
        break
    if not task_found: 
      print("\nThere is no such task, please enter another one again")
  else:
    print("\nPlease enter either 1 or 2")

def mark_tasks_as_completed():
  user_choice = input("\nType '1' if you want to complete it by writing it or '2' if you want to complete it by its roll no.")
  if user_choice == "1":
    user_input_1 = input("\nEnter the task you want to mark as done")
    task_found = False
    for i in range(len(tasks)):
      if user_input_1.capitalize() == tasks[i]:
        completed_tasks.append(tasks[i])
        tasks.remove(tasks[i])
        task_found = True
        display_all_tasks()
        print("Your task has been marked as done, thank you!")
        break
    if not task_found:
      print("\nThere is no such task, please enter another one again")
  elif user_choice == "2":
    user_input_2 = input("\nEnter the roll no. of the task you want to mark as done")
    task_found = False
    for i in range(len(tasks)):
      if int(user_input_2) == (i+1):
        completed_tasks.append(tasks[i])
        tasks.remove(tasks[i])
        task_found = True
        display_all_tasks()
        print("Your task has been marked as done, thank you!")
        break
    if not task_found:
      print("\nThere is no such task, please enter another one again")
  else:
    print("\nPlease enter either 1 or 2")

def exit_the_application():
  print("\nThank you, have a nice day!")
  
while True:
  display_all_tasks()
  print("\n=== MAIN MENU ===")
  print("1. Add new task")
  print("2. Remove task")
  print("3. Edit task")
  print("4. Mark task as completed")
  print("5. Exit")
  
  user_choice = input("\nEnter your choice (1-5):")
  if user_choice == "1":
    add_new_tasks()
  elif user_choice == "2":
    remove_tasks()
  elif user_choice == "3":
    edit_existing_tasks()
  elif user_choice == "4":
    mark_tasks_as_completed()
  elif user_choice == "5":
    exit_the_application()
    break
  else:
    print("\nPlease choose options only from 1-5!")
  
  
