def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            new_item = input("Enter the item to add: ")
            shopping_list.append(new_item)
        elif choice == '2':
            del_item = input("Enter the item to be removed: ")
            # Prompt for and remove an item
            if del_item not in shopping_list:
                print("Item not in list")
            else:
                shopping_list.remove(del_item)
        elif choice == '3':
            # Display the shopping list
            for i in shopping_list:
                print(i)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()