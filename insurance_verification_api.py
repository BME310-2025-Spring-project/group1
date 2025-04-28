from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# Simulated insurance database (in-memory)
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

def validate_date(date_str):
    try:
        if date_str:
            datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

@app.route('/api/insurance/eligibility', methods=['GET'])
def get_eligibility():
    try:
        patient_id = request.args.get('patient_id')
        insurance_id = request.args.get('insurance_id')
        service_date = request.args.get('service_date')

        if not patient_id or not insurance_id:
            return jsonify({"error": "patient_id and insurance_id are required"}), 400

        if service_date and not validate_date(service_date):
            return jsonify({"error": "Invalid service_date format. Use YYYY-MM-DD"}), 400

        if insurance_id not in insurance_db:
            return jsonify({
                "patient_id": patient_id,
                "insurance_id": insurance_id,
                "eligibility_status": "not_found",
                "coverage_details": {},
                "message": "Insurance policy not found"
            }), 200

        record = insurance_db[insurance_id]
        if record['patient_id'] != patient_id:
            return jsonify({
                "patient_id": patient_id,
                "insurance_id": insurance_id,
                "eligibility_status": "not_found",
                "coverage_details": {},
                "message": "Patient ID does not match insurance record"
            }), 200

        return jsonify({
            "patient_id": patient_id,
            "insurance_id": insurance_id,
            "eligibility_status": record['eligibility_status'],
            "coverage_details": record['coverage_details'],
            "message": "Eligibility verified successfully"
        }), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/api/insurance/eligibility', methods=['POST'])
def post_eligibility():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Request body is required"}), 400

        required_fields = ['patient_id', 'insurance_id', 'first_name', 'last_name', 'date_of_birth']
        missing_fields = [field for field in required_fields if field not in data or not data[field]]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        patient_id = data['patient_id']
        insurance_id = data['insurance_id']
        service_date = data.get('service_date')

        if not validate_date(data['date_of_birth']):
            return jsonify({"error": "Invalid date_of_birth format. Use YYYY-MM-DD"}), 400
        if service_date and not validate_date(service_date):
            return jsonify({"error": "Invalid service_date format. Use YYYY-MM-DD"}), 400

        if insurance_id not in insurance_db:
            return jsonify({
                "patient_id": patient_id,
                "insurance_id": insurance_id,
                "eligibility_status": "not_found",
                "coverage_details": {},
                "message": "Insurance policy not found"
            }), 200

        record = insurance_db[insurance_id]
        if (record['patient_id'] != patient_id or
            record['first_name'].lower() != data['first_name'].lower() or
            record['last_name'].lower() != data['last_name'].lower() or
            record['date_of_birth'] != data['date_of_birth']):
            return jsonify({
                "patient_id": patient_id,
                "insurance_id": insurance_id,
                "eligibility_status": "not_found",
                "coverage_details": {},
                "message": "Patient information does not match insurance record"
            }), 200

        return jsonify({
            "patient_id": patient_id,
            "insurance_id": insurance_id,
            "eligibility_status": record['eligibility_status'],
            "coverage_details": record['coverage_details'],
            "message": "Eligibility verified successfully"
        }), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)