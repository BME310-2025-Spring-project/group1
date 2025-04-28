from flask import Flask, request, jsonify, render_template
from datetime import datetime
import uuid

app = Flask(__name__)

# Simulated insurance database (from Insurance Verification API)
insurance_db = {
    "INS456": {
        "patient_id": "P123",
        "first_name": "John",
        "last_name": "Doe",
        "date_of_birth": "1980-01-01",
        "eligibility_status": "active",
        "coverage_details": {
            "plan_name": "Gold Plan",
            "effective_date": "2024-01-01",
            "expiration_date": "2025-12-31",
            "copay": 20,
            "deductible": 500
        }
    },
    "INS789": {
        "patient_id": "P456",
        "first_name": "Jane",
        "last_name": "Smith",
        "date_of_birth": "1990-05-15",
        "eligibility_status": "inactive",
        "coverage_details": {
            "plan_name": "Silver Plan",
            "effective_date": "2023-01-01",
            "expiration_date": "2024-06-30",
            "copay": 30,
            "deductible": 1000
        }
    }
}

# Simulated doctors database
doctors_db = [
    {"doctor_id": "D001", "name": "Dr. Alice Brown", "specialty": "General Practice"},
    {"doctor_id": "D002", "name": "Dr. Bob Wilson", "specialty": "Cardiology"},
    {"doctor_id": "D003", "name": "Dr. Clara Lee", "specialty": "Pediatrics"}
]

# Simulated appointments database (in-memory)
appointments_db = []

# Available time slots (9:00 AM to 5:00 PM, 30-minute intervals)
default_time_slots = [
    "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
    "12:00", "12:30", "13:00", "13:30", "14:00", "14:30",
    "15:00", "15:30", "16:00", "16:30"
]

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_time(time_str):
    try:
        datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

def check_insurance_eligibility(patient_id, insurance_id):
    if insurance_id not in insurance_db:
        return False, "Insurance policy not found"
    record = insurance_db[insurance_id]
    if record['patient_id'] != patient_id:
        return False, "Patient ID does not match insurance record"
    if record['eligibility_status'] != "active":
        return False, "Insurance is not active"
    return True, "Insurance verified successfully"

@app.route('/appointment', methods=['GET'])
def appointment_page():
    return render_template('appointment_scheduling.html')

@app.route('/api/doctors', methods=['GET'])
def get_doctors():
    try:
        return jsonify(doctors_db), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/api/availability', methods=['GET'])
def get_availability():
    try:
        doctor_id = request.args.get('doctor_id')
        date = request.args.get('date')

        if not doctor_id or not date:
            return jsonify({"error": "doctor_id and date are required"}), 400

        if not validate_date(date):
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Check if doctor exists
        if not any(d['doctor_id'] == doctor_id for d in doctors_db):
            return jsonify({"error": "Doctor not found"}), 400

        # Get booked slots for the doctor on the specified date
        booked_slots = [
            appt['time'] for appt in appointments_db
            if appt['doctor_id'] == doctor_id and appt['date'] == date
        ]

        # Calculate available slots
        available_slots = [slot for slot in default_time_slots if slot not in booked_slots]

        return jsonify({
            "doctor_id": doctor_id,
            "date": date,
            "available_slots": available_slots
        }), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/api/appointments', methods=['POST'])
def book_appointment():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body is required"}), 400

        required_fields = ['patient_id', 'insurance_id', 'doctor_id', 'date', 'time']
        missing_fields = [field for field in required_fields if field not in data or not data[field]]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        patient_id = data['patient_id']
        insurance_id = data['insurance_id']
        doctor_id = data['doctor_id']
        date = data['date']
        time = data['time']

        # Validate inputs
        if not validate_date(date):
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
        if not validate_time(time):
            return jsonify({"error": "Invalid time format. Use HH:MM"}), 400
        if not any(d['doctor_id'] == doctor_id for d in doctors_db):
            return jsonify({"error": "Doctor not found"}), 400
        if time not in default_time_slots:
            return jsonify({"error": "Invalid time slot"}), 400

        # Verify insurance eligibility
        is_eligible, message = check_insurance_eligibility(patient_id, insurance_id)
        if not is_eligible:
            return jsonify({"error": message}), 400

        # Check if slot is already booked
        if any(appt['doctor_id'] == doctor_id and appt['date'] == date and appt['time'] == time
               for appt in appointments_db):
            return jsonify({"error": "Time slot already booked"}), 409

        # Book appointment
        appointment_id = str(uuid.uuid4())
        appointment = {
            "appointment_id": appointment_id,
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "date": date,
            "time": time,
            "status": "confirmed"
        }
        appointments_db.append(appointment)

        return jsonify({
            "appointment_id": appointment_id,
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "date": date,
            "time": time,
            "status": "confirmed",
            "message": "Appointment booked successfully"
        }), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)