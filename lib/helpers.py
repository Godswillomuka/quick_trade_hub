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