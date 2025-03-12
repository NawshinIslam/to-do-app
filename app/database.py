# database.py
import mysql.connector
import os

# Database configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),  # Default to 'localhost' if not set
    "user": os.getenv("DB_USER", "root"),       # Default to 'root' if not set
    "password": os.getenv("DB_PASSWORD", "12345"),  # Default to '12345' if not set
    "database": os.getenv("DB_NAME", "todoapp")    # Default to 'todoapp' if not set
}

def get_db_connection():
    """Establish a database connection."""
    conn = mysql.connector.connect(**DB_CONFIG)
    return conn

def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the tasks table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task_desc VARCHAR(255) NOT NULL,
        status ENUM('Pending', 'Done') DEFAULT 'Pending'  -- Add status column
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()