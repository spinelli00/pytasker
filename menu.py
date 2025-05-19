from tasks import managetasks, viewtasks, removetasks, marktask
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print(" | Welcome to the PYTASKER |")
    print(" | 1. View tasks | \n | 2. Manage tasks | \n | 3. Remove tasks | \n | 4. Mark taks as done | \n | 5. Exit |")

    option: int = input("Choose your option >> ").strip()

    if option == '1':
        clear()
        viewtasks()
    elif option == '2':
        clear()
        managetasks()
    elif option == '3':
        clear()
        removetasks()
    elif option == '4':
        clear()
        marktask()
    elif option == '5':
        print("Exiting PYTASKER... Goodbye!")
        break
    else:
        print("Invalid option, try again!\n")

    input("\nPress ENTER to continue...")
