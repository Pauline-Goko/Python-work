class Account:
   
    category = "Finance"

    def __init__(self, account_no, account_name, balance):
        self.account_no = account_no
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"You have deposited {amount}. Your new balance is {self.balance}."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"You have withdrawn {amount}. Your new balance is {self.balance}."
        else:
            return "Insufficient funds."

    def get_balance(self):
        return f"Your current balance is {self.balance}."






