task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yess/no): ")

match priority:
    case "high":
        message = f"{task} is a high priority task that requires immediate attention today!"
        case "medium":
            message = f"{task} is a medium priority that requires your action after high priority tasks are finished."
            case "low":
                message = f"{task} is a low priority task. Consider completing it when you have free time."
                case _:
                    message = f"{task} had an UNKOWNK priority. Please check."

                    if time_bound == "yes":
                        message += "This task requires imediate attention today!"

                        print(message)
