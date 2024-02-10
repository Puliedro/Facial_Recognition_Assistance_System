# CREATE DATABASE attendance_system;
USE attendance_system;

# Create the students table

create table Students (
  idUser INT NOT NULL AUTO_INCREMENT,
  firstname VARCHAR(255) NOT NULL,
  surname_1 VARCHAR(255) NOT NULL,
  surname_2 VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  schoolID VARCHAR(255) NOT NULL,
  school_grade VARCHAR(255) NOT NULL,
  school_group VARCHAR(255) NOT NULL,
  degree VARCHAR(255) NOT NULL,
  CONSTRAINT pk_students_idUser PRIMARY KEY (idUser),
  CONSTRAINT uk_students_matricula UNIQUE (schoolID),
  CONSTRAINT uk_students_correo UNIQUE (email)
  );

# Create the attendance table
CREATE TABLE Attendance(
  idAttendance INT NOT NULL AUTO_INCREMENT,
  idUser INT NOT NULL,
  attendance_time TIMESTAMP,
  attendance_check BOOLEAN,
  CONSTRAINT pk_attendance_idAttendance PRIMARY KEY (idAttendance),
  CONSTRAINT fk_attendance_idUser FOREIGN KEY (idUser) REFERENCES Students(idUser)
  );
  
# Create the codes table
CREATE TABLE Codes (
  idCode INT AUTO_INCREMENT PRIMARY KEY,
  code VARCHAR(15) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

# Create the students' code attempts table
CREATE TABLE CodeAttempts (
  idCodeAttempts INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  code VARCHAR(15) NOT NULL,
  attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (idCodeAttempts),
  FOREIGN KEY (email) REFERENCES Students(email)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);