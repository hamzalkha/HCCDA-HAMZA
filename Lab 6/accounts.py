# banking_app/accounts.py

balance_record = {}

def check_balance(customer_id):
    return balance_record.get(customer_id, 0)

def deposit(customer_id, amount):
    if customer_id not in balance_record:
        balance_record[customer_id] = 0
    balance_record[customer_id] += amount
    print(f"✅ Deposit successful! New Balance: {balance_record[customer_id]}")

def withdraw(customer_id, amount):
    if customer_id not in balance_record:
        balance_record[customer_id] = 0
    if balance_record[customer_id] >= amount:
        balance_record[customer_id] -= amount
        print(f"✅ Withdrawal successful! New Balance: {balance_record[customer_id]}")
    else:
        print("❌ Insufficient balance.")
