import sqlite3

DATABASE = 'quick_trade_hub.db'

# Function to get DB connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows access to columns by name
    return conn

# Function to create the necessary tables
def create_tables():
    conn = get_db_connection()
    c = conn.cursor()

    # Users table (added balance column for user funds)
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            balance REAL DEFAULT 0.0
        )
    ''')

    # Orders table
    c.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            order_type TEXT NOT NULL,
            amount REAL NOT NULL,
            price REAL NOT NULL,
            cryptocurrency TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

# Trades table
    c.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            buy_order_id INTEGER,
            sell_order_id INTEGER,
            trade_amount REAL NOT NULL,
            price REAL NOT NULL,
            total REAL NOT NULL,
            trade_type TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (buy_order_id) REFERENCES orders (id),
            FOREIGN KEY (sell_order_id) REFERENCES orders (id)
        )
    ''')

# Account Activity table (for tracking deposits and withdrawals)
    c.execute('''
        CREATE TABLE IF NOT EXISTS account_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            activity_type TEXT NOT NULL,
            amount REAL NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

 # Wallet Transactions table (for fund transactions)
    c.execute('''
        CREATE TABLE IF NOT EXISTS wallet_transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            transaction_type TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()  # Create tables when this file is run
