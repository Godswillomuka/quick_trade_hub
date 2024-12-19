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

    # Seed trades table
    c.execute('''
        INSERT INTO trades (user_id, buy_order_id, sell_order_id, trade_amount, price, total, trade_type)
        VALUES
        (1, 1, 2, 0.5, 29000.0, 14500.0, 'buy'),
        (2, 3, 2, 1.0, 1500.0, 1500.0, 'sell')
    ''')

    # Seed account_activity table
    c.execute('''
        INSERT INTO account_activity (user_id, activity_type, amount)
        VALUES
        (1, 'deposit', 1000.0),
        (2, 'withdrawal', 500.0),
        (3, 'deposit', 2000.0)
    ''')

    # Seed wallet_transactions table
    c.execute('''
        INSERT INTO wallet_transactions (user_id, amount, transaction_type)
        VALUES
        (1, 1000.0, 'deposit'),
        (2, -500.0, 'withdrawal'),
        (3, 2000.0, 'deposit')
    ''')

    conn.commit()
    conn.close()

    print("Database seeded successfully.")

if __name__ == '__main__':
    create_tables()  # Ensure tables exist before seeding
    seed_data()
