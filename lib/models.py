import sqlite3

DATABASE = 'quick_trade_hub.db'

# Function to get DB connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Allows access to columns by name
    return conn