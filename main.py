
default_host = "127.0.0.1"
default_user = "root"
default_password = "Umi15031706-"
default_db = "attendance_system"
default_port = "3306"


timer = 30

import mysql.connector
import random
import string
from datetime import datetime, timedelta
import time
from connector import connect, close_connection

def generate_code(length=4):
    """Generate a random alphanumeric code."""
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choice(characters) for _ in range(length))

def insert_code(cnx, code):
    """Insert the generated code into the database."""
    cursor = cnx.cursor()
    query = "INSERT INTO Codes (code) VALUES (%s)"
    cursor.execute(query, (code,))
    cnx.commit()
    cursor.close()
    print(f"Code {code} inserted at {datetime.now()}")

def remove_expired_codes(cnx, lifespan=timer):
    """Remove codes that are older than 'lifespan' seconds."""
    cursor = cnx.cursor()
    query = "DELETE FROM Codes WHERE created_at < %s"
    expiry_time = datetime.now() - timedelta(seconds=lifespan)
    cursor.execute(query, (expiry_time,))
    cnx.commit()
    cursor.close()

# Main function to run the authenticator
def run_authenticator():
    cnx = connect()
    if cnx is not None:
        code = generate_code()
        print(f"Generated Code: {code}")
        insert_code(cnx, code)

        # Wait for 30 seconds before checking for expired codes
        time.sleep(timer)
        remove_expired_codes(cnx)

        close_connection(cnx)

if __name__ == "__main__":
    while True:
        run_authenticator()
        #time.sleep(1)
