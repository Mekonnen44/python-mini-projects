import json

FILE = "tasks.json"

def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

tasks = load_tasks()

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks(tasks)
    elif choice == "2":
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t}")
    elif choice == "3":
        break