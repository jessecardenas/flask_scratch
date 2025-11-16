import sqlite3
import getpass
from werkzeug.security import generate_password_hash
import config as cfg

def create_admin_user():
    """Interactively creates a new admin user."""
    print("Creating a new admin user...")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    password_confirm = getpass.getpass("Confirm password: ")

    if not username or not password:
        print("Username and password cannot be empty.")
        return

    if password != password_confirm:
        print("Passwords do not match.")
        return

    try:
        conn = sqlite3.connect(cfg.sqlite_file)
        c = conn.cursor()

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Insert the new user
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                  (username, hashed_password))

        conn.commit()
        print(f"Admin user '{username}' created successfully.")

    except sqlite3.IntegrityError:
        print(f"Error: User '{username}' already exists.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    create_admin_user()
