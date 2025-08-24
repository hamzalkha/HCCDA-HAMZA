# banking_app/bankcore.py

branch_id = 2057
users_info = {}
user_counter = 0

def generate_customer_id():
    global user_counter
    user_counter += 1
    return f"{branch_id}-{user_counter}"

def create_account(name, password):
    customer_id = generate_customer_id()
    users_info[customer_id] = {"name": name, "password": password}
    print(f"✅ Account created successfully! Your Customer ID is: {customer_id}")
    return customer_id

def login(customer_id, password):
    if customer_id in users_info:
        if users_info[customer_id]["password"] == password:
            print(f"✅ Login successful! Welcome {users_info[customer_id]['name']}.")
            return True
        else:
            print("❌ Invalid login: Wrong password.")
            return False
    else:
        print("❌ Invalid login: Customer ID not found.")
        return False
