class AccountHolder:
    def __init__(self, fname, mname, lname, account_type, balance):
        self.fname = fname
        self.mname = mname 
        self.lname = lname 
        self.account_type = account_type 
        self.balance = balance  
        self.status = open
    

class Bank:
    def __init__(self, name, address):
        self.name = name 
        self.address = address
        self.accounts = []
    
    def openAccount(self, fname, mname, lname, account_type, balance):
        temp = AccountHolder(fname, mname, lname, account_type, balance)
        if balance >= 100:
            self.accounts.append(temp)
            print(f"Congratulations {fname} {mname} {lname}! You have a new account with {self.name}. Thanks for trusting {self.name} with your money.")
        else: 
            print("Sorry, you must start an account with an inital balance of at least $100.")
    def showMembers(self):
        for accounts in self.accounts:
            print(f"{accounts.fname} {accounts.lname} balance: {accounts.balance}")
    def transferFunds(self, your_account, recipient_account, amount):
        for accounts in self.accounts:
            if accounts.fname == your_account:
                accounts.balance -= amount
        for accounts in self.accounts:
            if accounts.fname == recipient_account:
                accounts.balance += amount



def main(): 
    Big_Boy_Banking = Bank("Big Boy Banking", "69420 Street Avenue")
    action = 1
    while action != 6:
        print(f"""
        What are you trying to do this fine day at {Big_Boy_Banking.name}? Where you matter.
        1. Open an Account.
        2. Print list of all account holders. 
        3. Transfer funds. 
        6. Exit Big Boy Banking.""")
        action = int(input(">"))
        if action == 1:
            fname = input("First name:")
            mname = input("Middle name:")
            lname = input("Last name:")
            account_type = input("Account type (checking or saving): ")
            balance = int(input("Inital deposit: "))
            Big_Boy_Banking.openAccount(fname, mname, lname, account_type, balance)
        elif action == 2:
            Big_Boy_Banking.showMembers()
        elif action == 3:
            your_account = input("Your first name: ")
            recipient_account = input("Recipient first name: ")
            amount = int(input("Transfer amount: "))
            Big_Boy_Banking.transferFunds(your_account, recipient_account, amount)
        elif action == 6:
            print("See you soon.")
            break

main()

