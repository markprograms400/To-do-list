tasks = []

while True:
    print("""
Choose the following options: 
1. Add Task
2. View Tasks
3. Delete Task
4. Exit""")

    option_input = int(input("Enter option (1-4): "))
    
    if option_input == 1: 
         ask_task = input("Enter task needed to be done: ")
         tasks.append(ask_task)

    elif option_input == 2:
         print("Here are all the tasks needed to be done:")
         for x in tasks: 
              print(x)
    elif option_input == 3:
         remove_task = input("Which task would you like to remove? ")
         tasks.remove(remove_task)
    elif option_input == 4: 
         break
