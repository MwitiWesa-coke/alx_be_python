# daily_reminder.py

# Ensure user gives non-empty task
while True:
    task = input("Enter your task: ").strip()
    if task:
        break
    print("Task cannot be empty. Please enter your task.")

# Ensure user gives valid priority
while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ("high", "medium", "low"):
        break
    print("Please enter priority as 'high', 'medium', or 'low'.")

# Ask if task is time-bound
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ("yes", "no"):
        break
    print("Please answer with 'yes' or 'no'.")

# Use match case for priority handling
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task."
    case "medium":
        message = f"Note: '{task}' is a medium priority task. Handle it after high priority ones."
    case "low":
        message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        message = f"Task '{task}' has an unknown priority."

# Use if to adjust for time sensitivity
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# Print the customized reminder
print(message)

