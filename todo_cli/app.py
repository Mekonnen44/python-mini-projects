import json
import os

FILE = "data.json"

def load_data():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"id": len(tasks)+1, "title": title})
    
def update_task(tasks):
    task_id = int(input("Enter task id to update: "))
    for task in tasks:
        if task["id"] == task_id:
            new_title = input("New title: ")
            task["title"] = new_title
            
def delete_task(tasks):
    task_id = int(input("Enter task id to delete: "))
    tasks[:] = [t for t in tasks if t["id"] != task_id]

def main():
    tasks = load_data()

    while True:
        print("\n1.Add 2.Update 3.Delete 4.View 5.Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            update_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print(tasks)
        elif choice == "5":
            save_data(tasks)
            break

main()