
# Attendance Management System

## Introduction

This Attendance Management System is designed to simplify and streamline the process of tracking student attendance for educational institutions. Utilizing Python's Bottle web framework and MongoDB, this system provides an easy-to-use interface for both teachers and students, ensuring efficient and accurate attendance management.

## Features

- **Teacher Interface**: Allows teachers to generate unique attendance codes, view attendance records, and manage student profiles.
- **Student Interface**: Enables students to submit attendance codes and view their attendance history.
- **Secure Authentication**: Ensures that only authorized users can access the system, with password protection for both teachers and students.
- **Real-Time Code Generation**: Teachers can generate new codes that students must use to mark their attendance within a specified timeframe.
- **Database Management**: Utilizes MongoDB for storing user data, attendance records, and generated codes, ensuring data integrity and ease of access.

## Installation and Setup

You will need to manually install the necessary Python packages.

### Prerequisites

- Python 3.x
- MongoDB
- Git (optional, for cloning the repository)

### Step-by-Step Installation

1. If you haven't already, install Python and MongoDB on your system.
2. Clone the repository to your local machine or download the source code:

   ```bash
   git clone [repository-url]
   cd [project-directory]
   ```

3. Install the required Python libraries:

   ```bash
   pip install bottle pymongo werkzeug
   ```

4. Ensure MongoDB is running on your system.
5. Update the MongoDB connection URI and other configuration settings in the Python files as necessary.

## Database Configuration

Before starting the application, it's essential to configure the database connection. The `tables.py`, `app.py`, `main.py`, and `authenticator.py` files contain an empty `uri` variable that must be filled with your MongoDB URI to establish a connection to your database. This is necessary because every MongoDB setup might have different credentials and connection strings. 

To connect your Attendance Management System to MongoDB, follow these steps:

1. Obtain your MongoDB connection URI from your MongoDB instance. This typically looks like `mongodb://username:password@host:port/databaseName`.

2. Open `tables.py`, `app.py`, `main.py`, and `authenticator.py` in your preferred text editor.

3. Locate the line `uri = ""` in each file.

4. Replace the empty quotes `""` with your MongoDB connection URI, ensuring to keep the URI within the quotes. For example:

   ```python
   uri = "mongodb://username:password@host:port/databaseName"
   ```

5. Save the changes to each file.

Please handle your MongoDB URI with care to maintain the security of your database, especially if your codebase is stored or shared publicly.

### Starting the Application

1. Navigate to the project directory if you're not already there.
2. Run the application:

   ```bash
   python app2.py
   ```

3. The system should now be running on `http://localhost:9000`. Open this URL in a web browser to start using the Attendance Management System.

## Usage

After starting the application, you will be presented with the home page where you can choose to log in as a teacher or a student:

- **Teachers** can log in to generate attendance codes, view and download attendance records, and manage student information.
- **Students** can log in to enter the attendance code provided by their teacher and view their own attendance history.

## Contributing

Contributions to this project are welcome! Please adhere to the following steps:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is distributed under the MIT License.

## Acknowledgments

- Special thanks to all contributors who have helped to improve this system.
- Gratitude to the Python and MongoDB communities.
unities for providing the tools and resources to build this project.
