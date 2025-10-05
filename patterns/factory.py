# patterns/factory.py
from core.transaction import Expense, Income

class TransactionFactory:
    def create_transaction(self, t_type, amount, category, description):
        if t_type == "expense":
            return Expense(amount, category, description)
        elif t_type == "income":
            return Income(amount, category, description)
        else:
            raise ValueError("Invalid transaction type")
