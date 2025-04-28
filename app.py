from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database
patients_db = []

@app.route('/register', methods=['POST'])
def register_patient():
    data = request.get_json()

    # Basic validation
    required_fields = ['first_name', 'last_name', 'id_number', 'insurance_number', 'contact_info']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # Save to "database"
    patient_record = {
        "first_name": data['first_name'],
        "last_name": data['last_name'],
        "id_number": data['id_number'],
        "insurance_number": data['insurance_number'],
        "contact_info": data['contact_info']
    }
    patients_db.append(patient_record)

    return jsonify({"message": "Patient registered successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
