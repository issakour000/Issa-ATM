transactions = []
balance = 10000

def withdraw(amount):
    global balance
    if amount > balance:
        print("  Insufficient balance!")
        return
    balance -= amount
    transactions.append((" Withdrawn  : Rs.",amount,'Balance Rs.',balance))
    print(amount," withdrawn successfully!")
def show_state():
    print("\n  Transaction Statement ")
    if not transactions:
        print("  No transactions yet.")
    else:
        for i, t in enumerate(transactions, 1):
            print(i,t)
    print(" __________________________________________")
    
def display_b():
    print("\n Current Balance: Rs. ",balance)
def deposit(amount):
    global balance
    balance += amount
    transactions.append((" Deposited : Rs.",amount, "Balance: Rs.",balance))
    print('Rs.',amount,'deposited successfully!')