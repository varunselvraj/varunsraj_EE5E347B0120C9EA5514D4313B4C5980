class BankAccount:
    def _init_(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print("Deposit successful. New balance: ${:.2f}".format(self.__account_balance))
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            print("Withdrawal successful. New balance: ${:.2f}".format(self.__account_balance))
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print("Account Balance: ${:.2f}".format(self.__account_balance))


# Example usage
account_number = input("Enter account number: ")
account_holder_name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

# Creating an instance of the BankAccount class
account = BankAccount(account_number, account_holder_name, initial_balance)

# Testing deposit and withdrawal functionality
account.deposit(1000)
account.withdraw(500)
account.display_balance()