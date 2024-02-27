from bottle import Bottle, run, template, redirect, request, route
from pymongo import MongoClient, errors
from werkzeug.security import generate_password_hash, check_password_hash
import threading
import json
from main import * # Import all functions from main module
from authenticator import * # Import all functions from authenticator module

app = Bottle()

# Set up the MongoDB client with the provided URI
client = MongoClient("") #Insert uri from your Mongo database to connect with the script.
db = client['attendance_system']  # Connect to the 'attendance_system' database
# Initialize collections from the database
students_collection = db['Students']  
attendance_collection = db['Attendance']
codes_collection = db['Codes']
code_attempts_collection = db['CodeAttempts']
teachers_collection = db['Teachers']

@app.route('/')
def home():
    # Render the home page with options to navigate to teacher or student login.
    return template('index.html')

@app.route('/teacher')
def teacher():
    # Render the teacher login page.
    return template('teacher_login.html')

@app.route('/teacher_login', method='POST')
def teacher_login():
    # Handle the login request for a teacher.
    teacher_email = request.forms.get('teacher_email')
    password = request.forms.get('password')
    # Find the teacher in the database by email.
    teacher = teachers_collection.find_one({'email': teacher_email})
    
    # If the teacher is found in the database
    if teacher:
     # Check if the password is correct
        if 'password' in teacher:
            if check_password_hash(teacher['password'], password):
                return redirect('/teacher_dashboard')
            else:
                return template('teacher_login.html', message="Invalid email or password.")
        else:
            # If there is no password associated with the email, add it to the database
            hashed_password = generate_password_hash(password)
            teachers_collection.update_one({'email': teacher_email}, {'$set': {'password': hashed_password}})
            
            # Redirect to the teacher dashboard after adding the password
            return redirect('/teacher_dashboard')
    else:
        # If teacher not found, show login error message
        return template('teacher_login.html', message="Invalid email or password.")

    redirect('/teacher_dashboard')

@app.route('/teacher_dashboard')
def teacher_dashboard():
    # Generate a random alphanumeric code
    code = generate_code()

    # Insert the generated code into the MongoDB
    insert_code(db, code)

    # Start a new thread to remove expired codes after 30 seconds
    threading.Timer(30, remove_expired_codes, [db]).start()

    # Render the teacher dashboard with the latest code
    return template('teacher_dashboard.html', latest_code=code)

@app.route('/latest_code')
def latest_code():
    # This route should return the most recent code from the database
    codes_collection = db['Codes']
    latest_code = codes_collection.find_one(sort=[('created_at', -1)])
    if latest_code:
        return json.dumps(latest_code['code'])
    else:
        return json.dumps("No code available")

@app.route('/student')
def student():
    # Render the student login page.
    return template('student_login.html')


@app.route('/student_login', method='POST')
def student_login():
    # Retrieve email and password from the form
    student_email = request.forms.get('student_email')
    password = request.forms.get('password')

    # Search for the student in the database
    student = students_collection.find_one({'email': student_email})

    # Check if the student is found in the database
    if student:
        # Check if the password is associated with the email
        if 'password' in student:
            # Verify the password
            if check_password_hash(student['password'], password):
                return redirect('/student_dashboard')
            else:
                return template('student_login.html', message="Invalid email or password.")
        else:
            # If there is no password associated with the email, add it to the database
            hashed_password = generate_password_hash(password)
            students_collection.update_one({'email': student_email}, {'$set': {'password': hashed_password}})
            # Redirect to the student dashboard after adding the password
            return redirect('/student_dashboard')
    else:
        # If student not found, redirect back to the login page or to an error page
        return template('student_login.html', message="Invalid email or password.")
    
@app.route('/student_dashboard', method=['GET', 'POST'])
def student_dashboard():
    if request.method == 'POST':
        # Retrieve code and email from the form
        code = request.forms.get('codeInput')
        student_id = request.forms.get('student_id')
        
        if not code or not student_id:  # Check if code or email is missing
            return template('student_dashboard.html', message="Please enter both code and email.")

        # Check if the entered code matches the most recent code
        most_recent_code = get_most_recent_code(db)
        if most_recent_code and most_recent_code == code:
            record_attendance(db, student_id)
            return template('student_dashboard.html', message="Attendance recorded successfully.")
        else:
            insert_attempt(db, student_id, code)
            return template('student_dashboard.html', message="Invalid code. Please try again.")
    else:
        # Just render the form when the request method is GET
        return template('student_dashboard.html')


if __name__ == '__main__':
    # Run the Bottle web server with the application
    run(app, host='localhost', port=9000, debug=True)
