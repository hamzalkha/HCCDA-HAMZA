# banking_app/main.py

from banking_app import bankcore, accounts

def main():
    print("🏦 Welcome to Muhammad Hamza Khalid Banking Application 🏦")
    while True:
        print("\nSelect an option:")
        print("1. Create Account")
        print("2. Login to Account")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            name = input("Enter your name: ")
            password = input("Set a password: ")
            customer_id = bankcore.create_account(name, password)
            accounts.balance_record[customer_id] = 0

        elif choice == "2":
            customer_id = input("Enter your Customer ID: ")
            password = input("Enter your password: ")

            if bankcore.login(customer_id, password):
                while True:
                    print("\n--- Banking Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")

                    action = input("Choose an option: ")

                    if action == "1":
                        try:
                            amt = float(input("Enter amount to deposit: "))
                            accounts.deposit(customer_id, amt)
                        except ValueError:
                            print("❌ Invalid amount. Please enter a number.")

                    elif action == "2":
                        try:
                            amt = float(input("Enter amount to withdraw: "))
                            accounts.withdraw(customer_id, amt)
                        except ValueError:
                            print("❌ Invalid amount. Please enter a number.")

                    elif action == "3":
                        bal = accounts.check_balance(customer_id)
                        print(f"💰 Your balance is: {bal}")

                    elif action == "4":
                        print("👋 Logged out successfully.")
                        break
                    else:
                        print("❌ Invalid choice. Try again.")

        elif choice == "3":
            print("🙏 Thank you for using Muhammad Hamza Khalid Banking App. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
