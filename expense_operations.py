from ml_model.train_model import predict_category
def add_expense(expenses):
    """Add a new expense"""
    amount = input("Enter amount: ")
    description = input("Enter expense description: ")

    category = predict_category(description)
    print("Predicted category:", category)

    expenses.append(f"{amount} - {description} - {category}")
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
def analyze_expenses(expenses):
    category_totals = {}

    for expense in expenses:
        parts = expense.split(" - ")
        amount = float(parts[0])
        category = parts[2]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\n--- Expense Analysis ---")
    for cat, total in category_totals.items():
        print(f"{cat}: ₹{total}")

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
