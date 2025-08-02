import os
# file to store tasks

FILE_NAME = "task.txt"

# load tasks

def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                task_id,title,status = line.strip().split(" | ")
                tasks[int(task_id)] = {"title" : title, "status" : status}
    return tasks     

#  Save tasks in file

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task_id,task in tasks.items():
            file.write(f"{task_id} | {task["title"]} | {task["status"]}\n")
            
#  Add a new tasks
def add_task(tasks):
    title  = input("Enter a task title: ")
    task_id = max(tasks.keys(),default=0) + 1
    tasks[task_id] ={"title" : title, "status" : "incomplete"}
    print(f"Task '{title}' added.")


# View All Tasks

def view_tasks(tasks):
    if not tasks:
        print("Tasks not Available Yet.")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")
            
            
# Mark task as complete
def mark_task_complete(tasks):
    task_id = int(input("Enter task ID to mark as complete: ")) 
    if task_id in tasks:
        tasks[task_id]["status"] = "complete"
        print(f"'{tasks[task_id]['title']}' marked as complete. ")
    else:
        print("Task ID not found.")   
        
# Delete a task
def delete_task(tasks):
    task_id = int(input("Enter task ID to Delete: ")) 
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"'{tasks[task_id]['title']}' Deleted. ")
    else:
        print("Task ID not found.")
        
        
# Main Menu        
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice, please try again.")
            
# Run the main function to start the task manager                    
if __name__ == "__main__":
    main()