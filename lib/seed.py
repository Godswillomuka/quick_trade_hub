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