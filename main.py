from pymongo.mongo_client import MongoClient
from getpass import getpass
from datetime import datetime
from pymongo import errors

# Connect to the Mongodb
uri = "" #Insert uri from your Mongo database to connect with the script.

# Function to get the most recent code from the Codes collection
def get_most_recent_code(db):
    try:
        codes_collection = db['Codes']
        result = codes_collection.find().sort('created_at', -1).limit(1)  # Get the most recent code
        for code in result:
            return code['code']  # Return the most recent code
        return None
    except errors.PyMongoError as err:
        print(f"Failed to retrieve the most recent code: {err}")
        return None

# Function to insert an attempt into the CodeAttempts collection
def insert_attempt(db, email, code):
    try:
        code_attempts_collection = db['CodeAttempts']
        attempt = {
            'email': email,
            'code': code,
            'attempted_at': datetime.now()
        }
        code_attempts_collection.insert_one(attempt)
        print("Attempt recorded successfully.")
    except errors.PyMongoError as err:
        print(f"Failed to insert attempt: {err}")

def record_attendance(db, id):
    try:
        students_collection = db['Students']
        attendance_collection = db['Attendance']

        # Fetch student information based on the email
        student = students_collection.find_one({'schoolID': id})
        if student:
            student_name = f"{student['firstname']} {student['surname_1']} {student['surname_2']}"  # Corrected
            attendance_record = {
                'schoolID': id,  # Assuming 'schoolID' field exists
                'student_name': student_name,  # Corrected
                'email': student['email'],
                'attended_at': datetime.now()
            }
            # Insert attendance record into the Attendance collection
            attendance_collection.insert_one(attendance_record)
            print(f"{student['firstname']} {student['surname_1']} is marked as attending class.")
        else:
            print("No student found with the given id.")

    except errors.PyMongoError as err:
        print(f"Failed to record attendance: {err}")


# Main function to run the script
def main():
    client = None
    try:
        # Connect to MongoDB
        client = MongoClient(uri)
        db = client['attendance_system']
        print("Connected to the database successfully.")
        
        # Prompt the user for email
        email = input("Enter your ID: ")
        
        # Prompt the user for code
        code = getpass("Enter the code (hidden): ")  # Using getpass to simulate hiding the input
        
        # Check if the entered code matches the most recent code
        most_recent_code = get_most_recent_code(db)
        if most_recent_code and most_recent_code == code:
            print("The code matches the most recent code.")
            # Record attendance since the code is correct
            record_attendance(db, email)
        else:
            print("The code does not match the most recent code.")
        
        # Insert the attempt regardless of the match
        insert_attempt(db, email, code)

    except errors.ConnectionFailure as err:
        print(f"Failed to connect to the database: {err}")
    finally:
        if client:
            client.close()
            print("Database connection closed.")
            
if __name__ == "__main__":
    main()
