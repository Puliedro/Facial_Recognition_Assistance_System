-- Create a new database named 'attendance_system'.
CREATE DATABASE attendance_system;

-- Set the context to the 'attendance_system' database for subsequent operations.
USE attendance_system;

-- Create the 'Students' table with various attributes for student records.
CREATE TABLE Students (
  idUser INT NOT NULL AUTO_INCREMENT, -- A unique identifier for each student, automatically incremented.
  firstname VARCHAR(255) NOT NULL, -- The student's first name.
  surname_1 VARCHAR(255) NOT NULL, -- The student's first surname.
  surname_2 VARCHAR(255) NOT NULL, -- The student's second surname.
  email VARCHAR(255) NOT NULL, -- The student's email address.
  schoolID VARCHAR(255) NOT NULL, -- A unique school identification number for each student.
  school_grade VARCHAR(255) NOT NULL, -- The student's grade level.
  school_group VARCHAR(255) NOT NULL, -- The group or class the student belongs to.
  degree VARCHAR(255) NOT NULL, -- The degree program the student is enrolled in.
  CONSTRAINT pk_students_idUser PRIMARY KEY (idUser), -- Primary key constraint on 'idUser'.
  CONSTRAINT uk_students_matricula UNIQUE (schoolID), -- Unique constraint ensuring no duplicate school IDs.
  CONSTRAINT uk_students_correo UNIQUE (email) -- Unique constraint ensuring no duplicate emails.
);

-- Create the 'Attendance' table to track student attendance.
CREATE TABLE Attendance(
  idAttendance INT NOT NULL AUTO_INCREMENT, -- A unique identifier for each attendance record.
  idUser INT NOT NULL, -- The ID of the student from the Students table.
  attendance_time TIMESTAMP, -- The timestamp when the attendance was recorded.
  attendance_check BOOLEAN, -- A boolean value to check if the student attended.
  CONSTRAINT pk_attendance_idAttendance PRIMARY KEY (idAttendance), -- Primary key constraint on 'idAttendance'.
  CONSTRAINT fk_attendance_idUser FOREIGN KEY (idUser) REFERENCES Students(idUser) -- Foreign key constraint linking to the Students table.
);

-- Create the 'Codes' table to store codes used for attendance verification.
CREATE TABLE Codes (
  idCode INT AUTO_INCREMENT PRIMARY KEY, -- A unique identifier for each code.
  code VARCHAR(15) NOT NULL, -- The attendance code.
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- The timestamp when the code was created.
);

-- Create the 'CodeAttempts' table to track attempts by students to submit attendance codes.
CREATE TABLE CodeAttempts (
  idCodeAttempts INT NOT NULL AUTO_INCREMENT, -- A unique identifier for each code attempt.
  email VARCHAR(255) NOT NULL, -- The student's email, linked to the Students table.
  code VARCHAR(15) NOT NULL, -- The attendance code that was attempted.
  attempt_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- The timestamp when the attempt was made.
  PRIMARY KEY (idCodeAttempts), -- Primary key constraint on 'idCodeAttempts'.
  FOREIGN KEY (email) REFERENCES Students(email) -- Foreign key constraint linking to the Students table.
    ON DELETE CASCADE -- If a student record is deleted, their code attempts are also deleted.
    ON UPDATE CASCADE -- If a student's email is updated, the change reflects in their code attempts.
);

