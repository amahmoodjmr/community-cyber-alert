import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()

# Add the last_login column to the user table
try:
    cursor.execute('ALTER TABLE user ADD COLUMN last_login DATETIME')
    print("Column 'last_login' added successfully.")
except sqlite3.OperationalError as e:
    print(f"Error: {e}")

# Commit the changes and close the connection
conn.commit()
conn.close()
