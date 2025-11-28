class ExpensesSplitter:
    def __init__(self):
        self.expenses = {}

    def add_expense(self,payer,amount,participants):
        share = amount / len(participants)
        if payer not in self.expenses:
            self.expenses[payer] += 0
            self.expenses[payer] += amount
            
            
            for person in participants:
                if person != payer:
                    if person not in self.expenses:
                        self.expenses[person] = 0
                        self.expenses[person] -= share
                        
                        def show_balances(self):
                            print("\nCurrent Balances")
                            
                            for person,balance in self.expenses.items():
                                print(f"{person}: {'Owes' if balance < 0 else 'GETS'} {abs(balance):,.2f}")
                            
                            