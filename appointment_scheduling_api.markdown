# Appointment Scheduling Module Documentation

## Overview
This module provides a web interface and backend API for patients to schedule appointments after registration and insurance verification. It includes date selection, doctor selection, and time slot confirmation features.

Related to WBS Item 3.4 - Implement Appointment Scheduling Module.

## Components

### 1. Frontend: Appointment Scheduling Page
- **File**: `templates/appointment_scheduling.html`
- **Description**: A responsive webpage allowing patients to:
  - Input patient ID and insurance ID for verification.
  - Select an appointment date.
  - Choose a doctor from a list.
  - Pick an available time slot.
  - Confirm the appointment.
- **Technologies**: HTML, Tailwind CSS, JavaScript (Fetch API for backend communication).
- **Features**:
  - Form validation for patient and insurance IDs.
  - Dynamic loading of available doctors and time slots.
  - Real-time feedback on insurance verification and appointment booking.
  - Responsive design for desktop and mobile.

### 2. Backend: Appointment Scheduling API
- **File**: `appointment_scheduling_api.py`
- **Endpoints**:
  #### GET /api/doctors
  - **Description**: Retrieves a list of available doctors.
  - **Response**:
    ```json
    [
      {
        "doctor_id": "string",
        "name": "string",
        "specialty": "string"
      }
    ]
    ```
    - **200 OK**: List of doctors.
    - **500 Internal Server Error**: Server error.

  #### GET /api/availability
  - **Description**: Retrieves available time slots for a doctor on a specific date.
  - **Query Parameters**:
    - `doctor_id` (string, required): Doctor identifier.
    - `date` (string, required): Appointment date (format: YYYY-MM-DD).
  - **Response**:
    ```json
    {
      "doctor_id": "string",
      "date": "string",
      "available_slots": ["HH:MM", ...]
    }
    ```
    - **200 OK**: Available time slots.
    - **400 Bad Request**: Missing or invalid parameters.
    - **500 Internal Server Error**: Server error.

  #### POST /api/appointments
  - **Description**: Books an appointment after verifying insurance eligibility.
  - **Request Body**:
    ```json
    {
      "patient_id": "string",
      "insurance_id": "string",
      "doctor_id": "string",
      "date": "string",
      "time": "string"
    }
    ```
  - **Response**:
    ```json
    {
      "appointment_id": "string",
      "patient_id": "string",
      "doctor_id": "string",
      "date": "string",
      "time": "string",
      "status": "confirmed",
      "message": "string"
    }
    ```
    - **200 OK**: Appointment booked successfully.
    - **400 Bad Request**: Missing or invalid fields, or insurance verification failed.
    - **409 Conflict**: Time slot already booked.
    - **500 Internal Server Error**: Server error.

## Simulated Data
- **Doctors**: In-memory list of doctors with IDs, names, and specialties.
- **Appointments**: In-memory store for booked appointments.
- **Insurance Database**: Reuses the simulated insurance database from the Insurance Verification API (assumes integration).
- **Time Slots**: Simulated availability (e.g., 9:00 AM to 5:00 PM, 30-minute intervals, excluding booked slots).

## Setup and Running
1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Save the Python script as `appointment_scheduling_api.py`.
3. Ensure the `templates` folder contains `appointment_scheduling.html`.
4. Run the API:
   ```bash
   python appointment_scheduling_api.py
   ```
5. Access the scheduling page at `http://localhost:5000/appointment`.

## Example Usage
### Accessing the Scheduling Page
- Open `http://localhost:5000/appointment` in a browser.
- Enter patient ID and insurance ID, select a date, doctor, and time slot, then submit.

### API Requests
#### Get Doctors
```bash
curl http://localhost:5000/api/doctors
```

#### Get Available Time Slots
```bash
curl "http://localhost:5000/api/availability?doctor_id=D001&date=2025-05-01"
```

#### Book Appointment
```bash
curl -X POST http://localhost:5000/api/appointments \
-H "Content-Type: application/json" \
-d '{
  "patient_id": "P123",
  "insurance_id": "INS456",
  "doctor_id": "D001",
  "date": "2025-05-01",
  "time": "09:00"
}'
```

## Error Handling
- Validates all input fields (patient ID, insurance ID, date, time, doctor ID).
- Checks insurance eligibility before booking (integrates with Insurance Verification logic).
- Prevents double-booking of time slots.
- Returns clear error messages for invalid inputs or conflicts.
- Logs errors to console for debugging.

## Notes
- This is a simplified implementation for demonstration purposes.
- In production, add:
  - Authentication (e.g., JWT for patient login).
  - Database integration (e.g., PostgreSQL for doctors and appointments).
  - Email/SMS notifications for appointment confirmation.
  - Rate limiting and input sanitization.
  - Proper logging and monitoring.
- Assumes the Insurance Verification API's simulated database is available.