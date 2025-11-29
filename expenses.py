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

