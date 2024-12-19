from helpers import register_user, login_user, deposit_funds, withdraw_funds, execute_trade, view_account_info, place_order
from models import create_tables

def logged_in_menu(user):
    user_id = user['id']
    username = user['username']

    while True:
        print("\nLogged In Menu")
        print("1. View Account Info")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Place Order")
        print("5. Execute Trade")
        print("6. Log Out")
        choice = input("Choose an option: ")

        if choice == '1':
            print(view_account_info(user_id))
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            print(deposit_funds(user_id, amount))
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            print(withdraw_funds(user_id, amount))
        elif choice == '4':
            print("\nPlace Order")
            order_type = input("Enter order type (buy/sell): ").lower()
            amount = float(input("Enter amount: "))
            price = float(input("Enter price per unit: "))
            cryptocurrency = input("Enter cryptocurrency (e.g., BTC, ETH): ").upper()
            print(place_order(user_id, order_type, amount, price, cryptocurrency))
        elif choice == '5':
            print(execute_trade(user_id))
        elif choice == '6':
            print(f"Logged out successfully. Goodbye, {username}!")
            break
        else:
            print("Invalid option. Please choose again.")