def add_expense(expenses):
    """Add a new expense"""
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    expenses.append(f"{amount} {category}")
    print("Expense Added!")
    return expenses

def view_expenses(expenses):
    """Display all expenses"""
    print("\n--- Expenses ---")
    if len(expenses) == 0:
        print("No expenses added yet")
    else:
        for i, e in enumerate(expenses, 1):
            print(f"{i}. {e}")

def calculate_total(expenses):
    """Calculate total of all expenses"""
    total = 0
    for e in expenses:
        try:
            amount = e.split()[0]
            total += float(amount)
        except (ValueError, IndexError):
            continue
    return total