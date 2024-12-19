from getpass import getpass
from models import get_db_connection

# Register a new user
def register_user():
    print("\nRegistration Process")
    email = input("Enter email: ")
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    confirm_password = getpass("Confirm password: ")

    if password == confirm_password:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('INSERT INTO users (email, username, password, balance) VALUES (?, ?, ?, ?)', 
                  (email, username, password, 0.0))
        conn.commit()
        conn.close()
        print(f"User {username} registered successfully!")
    else:
        print("Passwords do not match. Try again.")

# Login a user
def login_user():
    email = input("\nEnter your email: ")
    password = getpass("Enter your password: ")

    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
    user = c.fetchone()
    conn.close()

    if user:
        print(f"Welcome back, {user['username']}!")
        return user
    else:
        print("Invalid email or password. Try again.")
        return None
    
# View user account info
def view_account_info(user_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = c.fetchone()
    conn.close()

    if user:
        return f"Account Info: Email - {user['email']}, Username - {user['username']}, Balance - {user['balance']}"
    return "User not found."

# Deposit funds
def deposit_funds(user_id, amount):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('UPDATE users SET balance = balance + ? WHERE id = ?', (amount, user_id))
    c.execute('INSERT INTO account_activity (user_id, activity_type, amount) VALUES (?, ?, ?)', (user_id, 'deposit', amount))
    c.execute('INSERT INTO wallet_transactions (user_id, amount, transaction_type) VALUES (?, ?, ?)', (user_id, amount, 'deposit'))
    conn.commit()
    conn.close()
    return f"Deposited {amount} into your account."

# Withdraw funds
def withdraw_funds(user_id, amount):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
    balance = c.fetchone()['balance']

    if balance >= amount:
        c.execute('UPDATE users SET balance = balance - ? WHERE id = ?', (amount, user_id))
        c.execute('INSERT INTO account_activity (user_id, activity_type, amount) VALUES (?, ?, ?)', (user_id, 'withdrawal', amount))
        c.execute('INSERT INTO wallet_transactions (user_id, amount, transaction_type) VALUES (?, ?, ?)', (user_id, amount, 'withdrawal'))
        conn.commit()
        conn.close()
        return f"Withdrew {amount} from your account."
    conn.close()
    return "Insufficient balance."

# Place an order
def place_order(user_id, order_type, amount, price, cryptocurrency):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('INSERT INTO orders (user_id, order_type, amount, price, cryptocurrency) VALUES (?, ?, ?, ?, ?)', 
              (user_id, order_type, amount, price, cryptocurrency))
    conn.commit()
    conn.close()
    return f"{order_type.capitalize()} order for {amount} {cryptocurrency} at ${price} placed successfully."
