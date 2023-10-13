class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display_balance(self):
        print(f"Account balance for {self.__account_holder_name}: ${self.__account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("12345", "John Doe", 1000)

    # Test deposit and withdrawal functionality
    account.display_balance()
    account.deposit(500)
    account.withdraw(200)
    account.display_balance()class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
            else:
                print("Insufficient balance for withdrawal.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display_balance(self):
        print(f"Account balance for {self.__account_holder_name}: ${self.__account_balance}")


# Testing the BankAccount class
if __name__ == "__main__":
    # Create an instance of BankAccount
    account = BankAccount("12345", "John Doe", 1000)

    # Test deposit and withdrawal functionality
    account.display_balance()
    account.deposit(500)
    account.withdraw(200)
    account.display_balance()
