import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import config as cfg

def check_auth(usr, pwd):
    conn = sqlite3.connect(cfg.sqlite_file)
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (usr,))
    user = c.fetchone()
    conn.close()
    if user and check_password_hash(user[0], pwd):
        return True
    return False


