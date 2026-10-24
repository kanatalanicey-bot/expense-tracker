import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    title = input("Enter expense name: ").strip()
    if not title:
        print("Name cannot be empty.")
        return

    try:
        amount = float(input("Enter amount in Rs.: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Enter a valid number.")
        return

    category = input("Enter category: ").strip() or "Other"

    expenses.append({
        "title": title,
        "amount": amount,
        "category": category
    })

    save_expenses(expenses)
    print("Expense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['title']} - "
            f"Rs. {expense['amount']:.2f} "
            f"({expense['category']})"
        )


def show_total(expenses):
    total = sum(item["amount"] for item in expenses)
    print(f"Total expenses: Rs. {total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total expenses")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
