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