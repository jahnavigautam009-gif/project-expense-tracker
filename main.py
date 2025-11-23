from file_operations import load_expenses, save_expenses
from expense_operations import add_expense, view_expenses, calculate_total
from user_interface import show_menu, get_user_choice

def main():
    expenses = load_expenses()
    
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            expenses = add_expense(expenses)   #adding
        elif choice == "2":
            view_expenses(expenses)            #viewing
        elif choice == "3":
            total = calculate_total(expenses)   #calculating 
            print(f"\n--- Total Expenses ---")
            print(f"Total: ${total:.2f}")
        elif choice == "4":
            save_expenses(expenses)
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":

    main()
