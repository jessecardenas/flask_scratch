import sqlite3
import config as cfg

# Create and connect to the database
conn = sqlite3.connect(cfg.sqlite_file)
c = conn.cursor()

# Create users table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database initialized.")
