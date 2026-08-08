class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining Balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate  # የወለድ መጠን

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print(f"Adding interest: {interest}")
        self.deposit(interest)


# Example usage
if __name__ == "__main__":
    # Create a savings account for Yeshu with 1000 initial balance and 5% interest
    acc = SavingsAccount("Yeshu Molla", 1000, 5)

    acc.deposit(500)      # Balance becomes 1500
    acc.add_interest()    # Adds 5% interest (75) -> Balance becomes 1575
    acc.withdraw(200)     # Balance becomes 1375
      
