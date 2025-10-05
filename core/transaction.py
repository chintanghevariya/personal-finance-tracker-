# core/transaction.py
class Transaction:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

class Expense(Transaction):
    def __init__(self, amount, category, description):
        super().__init__(-abs(amount), category, description)

class Income(Transaction):
    def __init__(self, amount, category, description):
        super().__init__(abs(amount), category, description)
