from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random
import string
from datetime import datetime, timedelta
import time

uri = ''  #Insert uri from your Mongo database to connect with the script.

# Default settings can be adjusted as needed
timer = 30

def generate_code(length=4):
    """Generate a random alphanumeric code."""
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choice(characters) for _ in range(length))

def insert_code(db, code):
    """Insert the generated code into the MongoDB."""
    codes_collection = db['Codes']
    code_document = {
        'code': code,
        'created_at': datetime.now()
    }
    result = codes_collection.insert_one(code_document)
    print(f"Code {code} inserted at {datetime.now()} with ID: {result.inserted_id}")

def remove_expired_codes(db, lifespan=timer):
    """Remove codes that are older than 'lifespan' seconds from MongoDB."""
    codes_collection = db['Codes']
    expiry_time = datetime.now() - timedelta(seconds=lifespan)
    result = codes_collection.delete_many({'created_at': {'$lt': expiry_time}})
    print(f"Expired codes removed: {result.deleted_count}")

# Main function to run the authenticator
def run_authenticator():
    client = None  # Initialize client outside of try-except
    try:
        # Connect to MongoDB
        client = MongoClient(uri, server_api=ServerApi('1'))
        db = client['attendance_system']  # Select the database
        code = generate_code()
        print(f"Generated Code: {code}")
        insert_code(db, code)

        # Wait for 30 seconds before checking for expired codes
        time.sleep(timer)
        remove_expired_codes(db)

    except errors.ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
    finally:
        if client:  # Now client is always defined, so no UnboundLocalError
            client.close()

if __name__ == "__main__":
    run_authenticator()  # Run the authenticator function once
