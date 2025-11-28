class ExpensesSplitter:
    def __init__(self):
        self.expenses = {}

    def add_expense(self,person,amount,ExpenseManager):
        share = amount / len(ExpenseManager)
        if person not in self.expenses:
            self.expenses[person] += 0
            self.expenses[person] += amount
            
            
            for person in ExpenseManager:
                if person != person:
                    if person not in self.expenses:
                        self.expenses[person] = 0
                        self.expenses[person] -= share
                        
                        def show_balances(self):
                            print("\nCurrent Balances")
                            
                            for person,balance in self.expenses.items():
                                print(f"{person}: {'Owes' if balance < 0 else 'GETS'} {abs(balance):,.2f}")
                            
                            
