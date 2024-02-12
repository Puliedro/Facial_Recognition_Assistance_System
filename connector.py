import mysql.connector

# default address
default_host = "127.0.0.1"
default_user = "root"
default_password = "Umi15031706-"
default_db = "attendance_system"
default_port = "3306"

# Function to connect to the database
def connect(host=default_host, user=default_user, password=default_password, database=default_db, port=default_port):
    try:
        # Attempt to connect to the database
        cnx = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        print("Connected successfully.")
        return cnx
    except mysql.connector.Error as err:
        # Display an error message
        print(f"Error connecting to the database: {err}")

# Function to close the database connection
def close_connection(cnx):
    try:
        cnx.close()
        print("Connection closed successfully.")
    except mysql.connector.Error as err:
        # Display an error message if the connection couldn't be closed
        print(f"Error closing the connection: {err}")
        
