import uuid
from datetime import datetime

class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}
        self.transactions = []

    def create_account(self, customer_name, initial_balance=0.0):
        account_id = str(uuid.uuid4())
        self.customers[customer_name] = account_id
        self.accounts[account_id] = {'owner': customer_name, 'balance': initial_balance}
        print(f"Account created for {customer_name} (ID: {account_id})")

    def find_account(self, identifier):
        if identifier in self.customers:
            return self.customers[identifier]
        elif identifier in self.accounts:
            return identifier
        raise ValueError("Account not found.")

    def deposit(self, account_id, amount):
        self.accounts[account_id]['balance'] += amount
        self.record_transaction(account_id, 'Deposit', amount)

    def withdraw(self, account_id, amount):
        if self.accounts[account_id]['balance'] < amount:
            raise ValueError("Insufficient funds.")
        self.accounts[account_id]['balance'] -= amount
        self.record_transaction(account_id, 'Withdrawal', amount)

    def get_balance(self, account_id):
        return self.accounts[account_id]['balance']

    def record_transaction(self, account_id, transaction_type, amount):
        self.transactions.append({
            'id': str(uuid.uuid4()),
            'account_id': account_id,
            'type': transaction_type,
            'amount': amount,
            'date': datetime.now().isoformat()
        })

    def get_transaction_history(self, account_id):
        return [tx for tx in self.transactions if tx['account_id'] == account_id]

def get_user_input(prompt, input_type=str):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Please enter a valid {input_type.__name__}.")

def perform_action(bank, action):
    identifier = input("Enter account ID or customer name: ")
    try:
        account_id = bank.find_account(identifier)
    except ValueError as e:
        print(e)
        return

    if action == "deposit":
        amount = get_user_input("Enter deposit amount: ", float)
        bank.deposit(account_id, amount)

    elif action == "withdraw":
        amount = get_user_input("Enter withdrawal amount: ", float)
        bank.withdraw(account_id, amount)

    elif action == "balance":
        print(f"Balance: ${bank.get_balance(account_id)}")

    elif action == "history":
        transactions = bank.get_transaction_history(account_id)
        if not transactions:
            print("No transactions found.")
        else:
            for tx in transactions:
                print(f"{tx['type']}: ${tx['amount']} on {tx['date']}")

def main():
    bank = Bank()
    menu_actions = {
        1: lambda: bank.create_account(input("Enter customer name: "), get_user_input("Enter initial deposit: ", float)),
        2: lambda: perform_action(bank, "deposit"),
        3: lambda: perform_action(bank, "withdraw"),
        4: lambda: perform_action(bank, "balance"),
        5: lambda: perform_action(bank, "history"),
        6: lambda: exit()
    }

    while True:
        print("\n1. Create account\n2. Deposit\n3. Withdraw\n4. Check balance\n5. View history\n6. Exit")
        choice = get_user_input("Choose an option: ", int)
        menu_actions.get(choice, lambda: print("Invalid choice"))()

if __name__ == "__main__":
    main()
