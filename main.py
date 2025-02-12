
import datetime
import json
import os
import sys



class Task:
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt
    
    
    def Add():
    

        # Load existing tasks from the file
        if os.path.exists("data.json"):
            with open("data.json", mode="r", encoding="utf-8") as read_file:
                existing_tasks = json.load(read_file)
                
        else:
            existing_tasks = []
        
        # Ensure existing_tasks is a list
        if not isinstance(existing_tasks, list):
            existing_tasks = []

        
        if os.path.exists("data.json"):
            with open("data.json", mode="r", encoding="utf-8") as read_file:
                tasks = json.load(read_file)
                if isinstance(tasks, list) and tasks:  # Check if it's a non-empty list
                    last_task = tasks[-1]  # Get the last task in the list
                    last_id = last_task["id"]
                    index = last_id +1 
                
                else:
                    index = 1
        else:
            index = 1
    
        task = Task(index, input("\nType a description for the task, please: "), 
                    input("\nClassified as todo, in-progress, or completed?:"), 
                    datetime.datetime.now(), datetime.datetime.now())
        print("\nThe task was created perfectly!")
        
        jsonTask = {

        "id": task.id ,
        "description" : task.description ,
        "status" : task.status,
        "createdAt" : task.createdAt.isoformat() ,
        "updatedAt" :task.updatedAt.isoformat()
        }
        # Append the new task and save back to the file
        existing_tasks.append(jsonTask)
        with open("data.json", mode="w", encoding="utf-8") as write_file:
            json.dump(existing_tasks, write_file, indent=4)

    def SeeData():
        task_id = int(input("\nWhich is the task's ID you want to consult? \n Answer:"))


        if os.path.exists("data.json"):
            with open("data.json", mode="r", encoding="utf-8") as read_file:
                dataReadTasks = json.load(read_file)
                
                # Ensure dataReadTasks is a list
                if isinstance(dataReadTasks, list):
                    # Find the task with the specified ID
                    for task in dataReadTasks:
                        if task["id"] == task_id:
                            print("Task found:")
                            print(f"ID: {task['id']}")
                            print(f"Description: {task['description']}")
                            print(f"Status: {task['status']}")
                            print(f"Created At: {task['createdAt']}")
                            print(f"Updated At: {task['updatedAt']}")
                            return
                    
                    print(f"No task found with ID {task_id}")
                else:
                    print("Invalid data format in JSON file. Expected a list of tasks.")
        else:
            print("No tasks found. Please add a task first.")

    def Delete():
        task_id = int(input("\nWhich is the task's ID you want to delete? \n\nAnswer: "))

        if os.path.exists("data.json"):
            with open("data.json", mode="r", encoding="utf-8") as read_file:
                dataReadTasks = json.load(read_file)
                updated_tasks = []

                # Ensure dataReadTasks is a list
                if isinstance(dataReadTasks, list):
                    task_found = False
                    # Find the task with the specified ID
                    for task in dataReadTasks:
                        if task["id"] == task_id:
                            task_found = True
                            print("\nTask found:")
                            print(f"ID: {task['id']}")
                            print(f"Description: {task['description']}")
                            print(f"Status: {task['status']}")
                            print(f"Created At: {task['createdAt']}")
                            print(f"Updated At: {task['updatedAt']}")
                            print("\nAre you sure you want to delete this task?")
                            decision = input("\nYes. \nNo.\n\nAnswer: ").strip().lower()

                            if decision == "yes":
                                print("\nTask found and deleted.")
                            else:
                                updated_tasks.append(task)  # Keep the task if the user says "No"
                        else:
                            updated_tasks.append(task)  # Keep tasks that don't match the ID

                    if not task_found:
                        print(f"\nNo task found with ID {task_id}")
                else:
                    print("\nInvalid data format in JSON file. Expected a list of tasks.")
        else:
            print("\nNo tasks found. Please add a task first.")
            return

        # Save the updated list back to the JSON file
        with open("data.json", mode="w", encoding="utf-8") as write_file:
            json.dump(updated_tasks, write_file, indent=4)

    def Edit():
        task_id = int(input("\nWhich is the task's ID you want to edit? \n \nAnswer: "))

        if os.path.exists("data.json"):
            with open("data.json", mode="r", encoding="utf-8") as read_file:
                dataReadTasks = json.load(read_file)
                updated_tasks = []

                # Ensure dataReadTasks is a list
                if isinstance(dataReadTasks, list):
                    task_found = False
                    # Find the task with the specified ID
                    for task in dataReadTasks:
                        if task["id"] == task_id:
                            task_found = True
                            print("\nTask found:")
                            print(f"ID: {task['id']}")
                            print(f"Description: {task['description']}")
                            print(f"Status: {task['status']}")
                            print(f"Created At: {task['createdAt']}")
                            print(f"Updated At: {task['updatedAt']}")
                            print("\nDo you want to edit this task?")
                            decision = input("\nYes. \nNo.\n\nAnswer: ").strip().lower()

                            if decision == "yes":
                                task["description"] = input("\nInsert your new description.\n\nAnswer:")
                                task["status"] = input("\nWhat is the current status of the task? (todo, in-progress or completed)\n\nAnswer:")
                                task["updatedAt"] = datetime.datetime.now().isoformat()
                                updated_tasks.append(task)
                            else:
                                updated_tasks.append(task)  
                        else:
                            updated_tasks.append(task)  # Keep tasks that don't match the ID

                    if not task_found:
                        print(f"\nNo task found with ID {task_id}")
                else:
                    print("\nInvalid data format in JSON file. Expected a list of tasks.")
        else:
            print("\nNo tasks found. Please add a task first.")
            return

        # Save the updated list back to the JSON file
        with open("data.json", mode="w", encoding="utf-8") as write_file:
            json.dump(updated_tasks, write_file, indent=4)

        pass
def Menu():
   
    while True:  # Use an infinite loop to keep the menu running 
        decision = input(f"Welcome! What are you looking for here?\n \n1. Create Tasks;\n2. See Tasks; \n3. Delete Tasks; \n4. Update Tasks. \n5. Quit.\n\nAnswer:")
        """
        The while True loop keeps the menu running until the user chooses to quit 

        print and input Misuse:

        The print function is used to display output, but it returns None. When you wrap input inside print, the value entered by the user is not assigned to decision. Instead, decision is assigned the return value of print, which is None.

        This means decision will always be None, and your while loop will never execute because None != "5".

        The input function is used directly to capture user input, and its result is assigned to decision.
        """
        if decision == "1":
            Task.Add()
        elif decision == "2":
            Task.SeeData()
        elif decision == "3":
            Task.Delete()
        elif decision == "4":
            Task.Edit()
        elif decision == "5":
            print("\nExiting exited. See you!")
            sys.exit(0)
        else:
            print("Invalid format choice. Try again.")
   

Menu()