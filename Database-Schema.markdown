# Database Schema for Patient, Insurance, and Appointment Management

## Overview
This document outlines the database schema for managing patient, insurance, and appointment data. The schema is designed to ensure data integrity, support efficient querying, and maintain relationships between entities. The schema is represented in a relational database structure, with an Entity-Relationship (ER) diagram provided for visualization.

## Tables and Columns

### 1. Patients
Stores information about patients.
- **patient_id**: `INT` (Primary Key, Auto-Increment)
- **first_name**: `VARCHAR(50)` (Not Null)
- **last_name**: `VARCHAR(50)` (Not Null)
- **date_of_birth**: `DATE` (Not Null)
- **gender**: `CHAR(1)` (M/F/O, Not Null)
- **phone**: `VARCHAR(15)`
- **email**: `VARCHAR(100)` (Unique)
- **address**: `TEXT`

### 2. Insurance
Stores insurance policy details for patients.
- **insurance_id**: `INT` (Primary Key, Auto-Increment)
- **patient_id**: `INT` (Foreign Key referencing Patients(patient_id))
- **provider_name**: `VARCHAR(100)` (Not Null)
- **policy_number**: `VARCHAR(50)` (Not Null, Unique)
- **start_date**: `DATE` (Not Null)
- **end_date**: `DATE`
- **coverage_details**: `TEXT`

### 3. Appointments
Stores appointment details for patients.
- **appointment_id**: `INT` (Primary Key, Auto-Increment)
- **patient_id**: `INT` (Foreign Key referencing Patients(patient_id))
- **appointment_date**: `DATETIME` (Not Null)
- **doctor_name**: `VARCHAR(100)` (Not Null)
- **status**: `ENUM('Scheduled', 'Completed', 'Cancelled')` (Not Null, Default: 'Scheduled')
- **notes**: `TEXT`

## Relationships
1. **Patients ↔ Insurance**:
   - **One-to-Many**: One patient can have multiple insurance policies (e.g., primary and secondary insurance), but each insurance policy belongs to exactly one patient.
   - **Foreign Key**: `Insurance.patient_id` references `Patients.patient_id`.
   - **On Delete**: Cascade (if a patient is deleted, their insurance records are also deleted).

2. **Patients ↔ Appointments**:
   - **One-to-Many**: One patient can have multiple appointments, but each appointment is associated with exactly one patient.
   - **Foreign Key**: `Appointments.patient_id` references `Patients.patient_id`.
   - **On Delete**: Cascade (if a patient is deleted, their appointment records are also deleted).

## Constraints
- **Primary Keys**: Ensure uniqueness for `patient_id`, `insurance_id`, and `appointment_id`.
- **Foreign Keys**: Enforce referential integrity between tables.
- **Unique Constraints**:
  - `Patients.email`: Ensures no two patients have the same email.
  - `Insurance.policy_number`: Ensures no duplicate policy numbers.
- **Not Null Constraints**: Ensure critical fields (e.g., `first_name`, `appointment_date`) are always populated.
- **Check Constraints**:
  - `Patients.gender`: Must be 'M', 'F', or 'O'.
  - `Appointments.status`: Must be one of 'Scheduled', 'Completed', or 'Cancelled'.

## ER Diagram
The ER diagram visualizes the relationships between the tables. Below is a textual representation of the ER diagram (to be converted into an image using a diagramming tool like Draw.io or Lucidchart for GitHub submission).

```
[Patients] ----(1:N)---- [Insurance]
   |                     |
   |                     |
   +----(1:N)---- [Appointments]
```

### ER Diagram Details
- **Entities**:
  - **Patients**: Rectangle with attributes (`patient_id`, `first_name`, etc.).
  - **Insurance**: Rectangle with attributes (`insurance_id`, `patient_id`, etc.).
  - **Appointments**: Rectangle with attributes (`appointment_id`, `patient_id`, etc.).
- **Relationships**:
  - **Patients-Insurance**: Diamond labeled "Has" (1:N).
  - **Patients-Appointments**: Diamond labeled "Books" (1:N).
- **Keys**:
  - Primary Keys: Underlined attributes (`patient_id`, `insurance_id`, `appointment_id`).
  - Foreign Keys: Indicated by arrows from `patient_id` in `Insurance` and `Appointments` to `Patients`.

## SQL Schema
Below is the SQL code to create the database schema.

```sql
CREATE TABLE Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    gender CHAR(1) NOT NULL CHECK (gender IN ('M', 'F', 'O')),
    phone VARCHAR(15),
    email VARCHAR(100) UNIQUE,
    address TEXT
);

CREATE TABLE Insurance (
    insurance_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    provider_name VARCHAR(100) NOT NULL,
    policy_number VARCHAR(50) NOT NULL UNIQUE,
    start_date DATE NOT NULL,
    end_date DATE,
    coverage_details TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE
);

CREATE TABLE Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    appointment_date DATETIME NOT NULL,
    doctor_name VARCHAR(100) NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Scheduled',
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id) ON DELETE CASCADE
);
```

## Notes
- The schema is designed to be extensible. For example, adding a `Doctors` table in the future could normalize `doctor_name` in the `Appointments` table.
- The ER diagram should be created using a tool like Draw.io and saved as `ER-Diagram.png` for GitHub submission.
- The schema supports basic CRUD operations and can be integrated with a healthcare application.

## Deliverables for GitHub Submission
1. **Database-Schema.md**: This document, containing the schema description, relationships, and SQL code.
2. **generate_er_diagram.py**: A Python script (provided below) to generate the ER diagram programmatically using `diagrams` library.
3. **ER-Diagram.png**: The generated ER diagram image (optional, to be generated by running the Python script).