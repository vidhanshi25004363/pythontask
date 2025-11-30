class ExpensesSplitter:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, person, amount, ExpenseManager):
        share = amount / len(ExpenseManager)
        if person not in self.expenses:
            self.expenses[person] = 0
        self.expenses[person] += amount

        for p in ExpenseManager:
            if p != person:
                if p not in self.expenses:
                    self.expenses[p] = 0
                self.expenses[p] -= share

    def show_balances(self):
        print("\nCurrent Balances")
        for person, balance in self.expenses.items():
            print(f"{person}: {'Owes' if balance < 0 else 'GETS'} {abs(balance):,.2f}")

    def settle_expense(self):
        print("\nSettling Expense")
        sorted_balances = sorted(self.expenses.items(), key=lambda x: x[1])
        while sorted_balances and sorted_balances[0][1] < 0 and sorted_balances[-1][1] > 0:
            debtor, debt_amount = sorted_balances[0]
            creditor, credit_amount = sorted_balances[-1]
            amount_to_settle = min(-debt_amount, credit_amount)
            print(f"{debtor} pays {amount_to_settle:.2f} to {creditor}")
            self.expenses[debtor] += amount_to_settle
            self.expenses[creditor] -= amount_to_settle
            sorted_balances = sorted(self.expenses.items(), key=lambda x: x[1])

    def reset_balances(self):
        self.expenses.clear()
        print("\nAll balances have been reset.")

    def menu(self):
        while True:
            print("\nExpense Splitter Menu")
            print("1. Add Expense")
            print("2. Show Balances")
            print("3. Settle Expenses")
            print("4. Reset Balances")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                person = input("Enter the name of the person who paid: ")
                amount = float(input("Enter the amount paid: "))
                participants = input("Enter the names of participants (comma separated): ").split(',')
                self.add_expense(person.strip(), amount, [p.strip() for p in participants])
                print("Expense added successfully")
            elif choice == '2':
                self.show_balances()
            elif choice == '3':
                self.settle_expense()
            elif choice == '4':
                self.reset_balances()
            elif choice == '5':
                print("Exiting Expense Splitter.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ExpensesSplitter()
    app.menu()
