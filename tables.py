from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#Connect to the server 
client = MongoClient("") #Insert uri from your Mongo database to connect with the script.

# Selecting the attendance_system database
db = client['attendance_system']

# Creating or getting the collection (similar to SQL tables)
students_collection = db['Students']
attendance_collection = db['Attendance']
codes_collection = db['Codes']
code_attempts_collection = db['CodeAttempts']
teachers_collection = db['Teachers']

# List of student records as provided
students_records = [
    {'firstname': 'Hageo Juda', 'surname_1': 'Balam', 'surname_2': 'Mendez', 'email': '2109012@upy.edu.mx', 'schoolID': '2109012', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'Miguel Angel', 'surname_1': 'Bastarrachea', 'surname_2': 'Carballo', 'email': '2009009@upy.edu.mx', 'schoolID': '2009009', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'Angel Adrian', 'surname_1': 'Campos', 'surname_2': 'Borges', 'email': '2109021@upy.edu.mx', 'schoolID': '2109021', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'Samantha', 'surname_1': 'Castro', 'surname_2': 'Echeverria', 'email': '2109028@upy.edu.mx', 'schoolID': '2109028', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'Karla', 'surname_1': 'Delgado', 'surname_2': 'Avendaño', 'email': '2109050@upy.edu.mx', 'schoolID': '2109050', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'Julio Ernesto', 'surname_1': 'Dzul', 'surname_2': 'Dzib', 'email': '2009048@upy.edu.mx', 'schoolID': '2009048', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'Carlo Alejandro', 'surname_1': 'Ek', 'surname_2': 'Palomo', 'email': '2109058@upy.edu.mx', 'schoolID': '2109058', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'Juan Antonio', 'surname_1': 'Fernandez', 'surname_2': 'Cruz', 'email': '2109061@upy.edu.mx', 'schoolID': '2109061', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'Hector Emiliano', 'surname_1': 'Gonzalez', 'surname_2': 'Martinez', 'email': '2109077@upy.edu.mx', 'schoolID': '2109077', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'Sonia Estefania', 'surname_1': 'Mendia', 'surname_2': 'Martinez', 'email': '2109104@upy.edu.mx', 'schoolID': '2109104', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'Juliana Alejandra', 'surname_1': 'Ramayo', 'surname_2': 'Cardoso', 'email': '2109128@upy.edu.mx', 'schoolID': '2109128', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'Angel David', 'surname_1': 'Sansores', 'surname_2': 'Cruz', 'email': '2109139@upy.edu.mx', 'schoolID': '2109139', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
    {'firstname': 'José Manuel', 'surname_1': 'Solano', 'surname_2': 'Ochoa', 'email': '2009127@upy.edu.mx', 'schoolID': '2009127', 'school_grade': '4°', 'school_group': 'A', 'degree': 'Ingeniería de Datos'},
]


teacher_records=[
    {'firstname': 'Adrian Roberto', 'surname_1': 'Carmona', 'surname_2': 'Rodriguez', 'email': 'adrian.carmona@upy.edu.mx', 'class': 'Internet of Things'}
]
# Inserting the records into the Students collection
students_collection.insert_many(students_records)

teachers_collection.insert_many(teacher_records)
# If you have attendance records, codes, and code attempts data,
# you can add them using the insert_one() or insert_many() methods in a similar manner.

print("Data inserted successfully!")