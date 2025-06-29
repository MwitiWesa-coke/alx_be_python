def display_menu():
    print(f"Shopping List Manager")
    print(f"1.Add Item")
    print(f"2. Remove Item")
    print(f"3. View List")
    print(f"4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("ENter the item to add: ").strip()
            if item in shopping_list:
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")

            elif choice == '2':
                item = input("Enter the item to remove: ").strip()
                if item in shopping list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' was not found in your shopping list.")

            elif choice == '3':
                if shopping_list:
                    print(f"\nYour Shopping List:")
                    for i, item in enumerate(shopping_list, start=1):
                        print(f"{i}. {item}")

                    else:
                        print(f"Your shopping list is empty.")

                    elif choice == '4':
                        print(f"Goodbye!")
                        break
                    else:
                        print(f"Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
