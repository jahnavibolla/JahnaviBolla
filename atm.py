class ATMMachine:
    def __init__(self, initial_balance=0, pin="1234"):
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []
        self.is_authenticated = False

    def authenticate(self, input_pin):
        """Authenticate user by checking the provided PIN."""
        if input_pin == self.pin:
            self.is_authenticated = True
            print("Authentication successful!")
        else:
            print("Incorrect PIN. Try again.")

    def inquire_balance(self):
        """Display the current account balance."""
        if self.is_authenticated:
            print(f"Your current balance is: ${self.balance}")
            self.transaction_history.append(f"Balance inquiry: ${self.balance}")
        else:
            print("Please authenticate first.")

    def deposit_cash(self, amount):
        """Deposit the given amount to the account."""
        if self.is_authenticated:
            if amount > 0:
                self.balance += amount
                print(f"${amount} deposited successfully.")
                self.transaction_history.append(f"Deposited: ${amount}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Please authenticate first.")

    def withdraw_cash(self, amount):
        """Withdraw the given amount from the account."""
        if self.is_authenticated:
            if amount > 0:
                if self.balance >= amount:
                    self.balance -= amount
                    print(f"${amount} withdrawn successfully.")
                    self.transaction_history.append(f"Withdrawn: ${amount}")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        else:
            print("Please authenticate first.")

    def change_pin(self, old_pin, new_pin):
        """Change the PIN if the old PIN matches."""
        if self.is_authenticated:
            if old_pin == self.pin:
                if new_pin.isdigit() and len(new_pin) == 4:
                    self.pin = new_pin
                    print("PIN changed successfully.")
                    self.transaction_history.append("PIN changed.")
                else:
                    print("New PIN must be a 4-digit number.")
            else:
                print("Incorrect old PIN.")
        else:
            print("Please authenticate first.")

    def view_transaction_history(self):
        """Display the transaction history."""
        if self.is_authenticated:
            if self.transaction_history:
                print("Transaction History:")
                for transaction in self.transaction_history:
                    print(transaction)
            else:
                print("No transactions made yet.")
        else:
            print("Please authenticate first.")

# Sample usage:
atm = ATMMachine(initial_balance=1000)  # Initialize ATM with a starting balance

# Authenticate the user
atm.authenticate(input("Enter PIN: "))

# Perform ATM operations
atm.inquire_balance()
atm.deposit_cash(500)
atm.withdraw_cash(200)
atm.change_pin("1234", "5678")
atm.view_transaction_history()
