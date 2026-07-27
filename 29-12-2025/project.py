import calendar
import datetime


class Expense:
    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f}>"


def main():
    print("🎯 Running Expense Tracker!")
    expense_file_path = "expenses.csv"
    budget = 2000

    expense = get_user_expense()
    save_expense_to_file(expense, expense_file_path)
    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print("🎯 Getting User Expense")

    expense_name = input("Enter expense name: ")

    # Safe amount input
    while True:
        try:
            expense_amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("❌ Please enter a valid number!")

    expense_categories = [
        "🍔 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        try:
            selected_index = int(
                input(f"Enter a category number [1 - {len(expense_categories)}]: ")
            ) - 1

            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                return Expense(
                    name=expense_name,
                    category=selected_category,
                    amount=expense_amount,
                )
            else:
                print("❌ Invalid category number.")
        except ValueError:
            print("❌ Please enter a valid number!")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving Expense: {expense}")

    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    print("🎯 Summarizing Expenses")

    expenses = []

    try:
        with open(expense_file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                expense_name, expense_amount, expense_category = line.strip().split(",")

                expenses.append(
                    Expense(
                        name=expense_name,
                        amount=float(expense_amount),
                        category=expense_category,
                    )
                )
    except FileNotFoundError:
        print("⚠ No expenses found yet.")
        return

    if not expenses:
        print("⚠ No expenses recorded.")
        return

    amount_by_category = {}

    for expense in expenses:
        amount_by_category[expense.category] = (
            amount_by_category.get(expense.category, 0) + expense.amount
        )

    print("\nExpenses By Category 📈:")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")

    total_spent = sum(x.amount for x in expenses)
    print(f"\n💵 Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
    else:
        daily_budget = remaining_budget

    print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))


def green(text):
    return f"\033[92m{text}\033[0m"


if __name__ == "__main__":
    main()
