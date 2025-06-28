# daily_reminder.py

# Prompt user for the task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Provide a customized reminder using match case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task."
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task. Handle it after high priority ones."
    case "low":
        message = f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        message = f"Reminder: '{task}' has an unknown priority."

# Adjust if time-bound
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# Print the reminder in the expected format
print(message)
