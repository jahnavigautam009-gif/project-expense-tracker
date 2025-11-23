def load_expenses():
    """Load expenses from file"""
    expenses = []  #intialise the expenses
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                expenses.append(line.strip())
    except FileNotFoundError:
        pass
    return expenses

def save_expenses(expenses):
    """Save expenses to file"""   #saving
    with open("expenses.txt", "w") as f:
        for e in expenses:

            f.write(e + "\n")
