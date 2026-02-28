import pymysql
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('../backend/.env')

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': int(os.getenv('DB_PORT', 3306))
}

print("Connecting to MySQL server...")
print(f"Host: {DB_CONFIG['host']}")
print(f"User: {DB_CONFIG['user']}")

try:
    # Connect without specifying database
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    print("✓ Connected successfully!")
    
    # Create database
    print("\nCreating database 'app_db'...")
    cursor.execute("CREATE DATABASE IF NOT EXISTS app_db")
    print("✓ Database created!")
    
    # Use the database
    cursor.execute("USE app_db")
    
    # Create table
    print("\nCreating 'items' table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    print("✓ Table created!")
    
    # Insert sample data
    print("\nInserting sample data...")
    cursor.execute("""
        INSERT INTO items (name) VALUES 
            ('Sample Item 1'),
            ('Sample Item 2'),
            ('Sample Item 3')
    """)
    conn.commit()
    print("✓ Sample data inserted!")
    
    # Verify
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    print(f"\n✓ Setup complete! Found {len(items)} items in database.")
    
    cursor.close()
    conn.close()
    
    print("\n✅ Database setup successful! You can now run the Flask app.")
    
except pymysql.err.OperationalError as e:
    print(f"\n❌ Connection failed: {e}")
    print("\nPlease check:")
    print("1. Your RDS endpoint is correct")
    print("2. Your username and password are correct")
    print("3. Your RDS security group allows your IP address")
    print("4. Your RDS instance is publicly accessible (if connecting from outside VPC)")
except Exception as e:
    print(f"\n❌ Error: {e}")
