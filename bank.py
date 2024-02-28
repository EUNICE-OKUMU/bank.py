class BankAccount:
    def __init__(self, account_number, customer_name, opening_date, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.opening_date = opening_date
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        self.balance -= amount
        return amount

    def check_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

    def customer_details(self):
        print(f"""
Customer Name: {self.customer_name}
Account Number: {self.account_number}
Date of Opening: {self.opening_date}
Balance: ${self.balance:.2f}
""")

# Example usage
account1 = BankAccount("12345678", "Gladies wanga", "2022-10-26", 1000)

# Deposit
deposit_amount = account1.deposit(500)
print(f"Deposited: ${deposit_amount:.2f}")

# Withdraw successful
withdrawal_amount = account1.withdraw(200)
print(f"Withdrawn: ${withdrawal_amount:.2f}")

# Withdraw insufficient balance
withdrawal_amount = account1.withdraw(1500)
print(withdrawal_amount)

# Check balance
account1.check_balance()

# Customer details
account1.customer_details()










