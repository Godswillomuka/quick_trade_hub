from models import get_db_connection, create_tables

def seed_data():
    """Populate the database with initial data for testing."""
    conn = get_db_connection()
    c = conn.cursor()

    # Seed users table
    c.execute('''
        INSERT INTO users (email, username, password, balance)
        VALUES 
        ('alice@example.com', 'alice', 'password1', 5000.0),
        ('bob@example.com', 'bob', 'password2', 3000.0),
        ('charlie@example.com', 'charlie', 'password3', 7000.0)
    ''')

     # Seed orders table
    c.execute('''
        INSERT INTO orders (user_id, order_type, amount, price, cryptocurrency)
        VALUES
        (1, 'buy', 0.5, 30000.0, 'BTC'),
        (2, 'sell', 1.0, 28000.0, 'ETH'),
        (3, 'buy', 2.0, 1500.0, 'ETH')
    ''')
