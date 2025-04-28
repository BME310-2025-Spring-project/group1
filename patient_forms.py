from flask import Flask, request, jsonify
import tkinter as tk
from tkinter import messagebox
import requests
import threading
import json

app = Flask(__name__)

# Mock backend API endpoints
@app.route('/api/patient/register', methods=['POST'])
def register_patient():
    data = request.get_json()
    if not all(key in data for key in ['first_name', 'last_name', 'dob', 'email']):
        return jsonify({'error': 'Missing required fields'}), 400
    # Mock successful registration
    return jsonify({'message': 'Patient registered successfully', 'patient_id': '12345'}), 201

@app.route('/api/insurance/verify', methods=['POST'])
def verify_insurance():
    data = request.get_json()
    if not all(key in data for key in ['provider', 'policy_number']):
        return jsonify({'error': 'Missing required fields'}), 400
    # Mock insurance verification
    if data['policy_number'].startswith('POL'):
        return jsonify({'message': 'Insurance verified', 'status': 'valid'}), 200
    return jsonify({'error': 'Invalid policy number'}), 400

# Tkinter UI
class PatientApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Management System")
        self.base_url = "http://localhost:5000/api"

        # Patient Registration Form
        tk.Label(root, text="Patient Registration").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(root, text="First Name").grid(row=1, column=0, sticky="e")
        self.first_name = tk.Entry(root)
        self.first_name.grid(row=1, column=1)
        tk.Label(root, text="Last Name").grid(row=2, column=0, sticky="e")
        self.last_name = tk.Entry(root)
        self.last_name.grid(row=2, column=1)
        tk.Label(root, text="Date of Birth (YYYY-MM-DD)").grid(row=3, column=0, sticky="e")
        self.dob = tk.Entry(root)
        self.dob.grid(row=3, column=1)
        tk.Label(root, text="Email").grid(row=4, column=0, sticky="e")
        self.email = tk.Entry(root)
        self.email.grid(row=4, column=1)
        tk.Button(root, text="Register", command=self.submit_registration).grid(row=5, column=0, columnspan=2, pady=10)

        # Insurance Verification Form
        tk.Label(root, text="Insurance Verification").grid(row=6, column=0, columnspan=2, pady=10)
        tk.Label(root, text="Insurance Provider").grid(row=7, column=0, sticky="e")
        self.provider = tk.Entry(root)
        self.provider.grid(row=7, column=1)
        tk.Label(root, text="Policy Number").grid(row=8, column=0, sticky="e")
        self.policy_number = tk.Entry(root)
        self.policy_number.grid(row=8, column=1)
        tk.Button(root, text="Verify", command=self.verify_insurance).grid(row=9, column=0, columnspan=2, pady=10)

    def submit_registration(self):
        data = {
            'first_name': self.first_name.get(),
            'last_name': self.last_name.get(),
            'dob': self.dob.get(),
            'email': self.email.get()
        }
        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            response = requests.post(f"{self.base_url}/patient/register", json=data)
            if response.status_code == 201:
                messagebox.showinfo("Success", response.json()['message'])
            else:
                messagebox.showerror("Error", response.json().get('error', 'Registration failed'))
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Network error: {str(e)}")

    def verify_insurance(self):
        data = {
            'provider': self.provider.get(),
            'policy_number': self.policy_number.get()
        }
        if not all(data.values()):
            messagebox.showerror("Error", "All fields are required")
            return
        try:
            response = requests.post(f"{self.base_url}/insurance/verify", json=data)
            if response.status_code == 200:
                messagebox.showinfo("Success", response.json()['message'])
            else:
                messagebox.showerror("Error", response.json().get('error', 'Verification failed'))
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Network error: {str(e)}")

# Run Flask server in a separate thread
def run_flask():
    app.run(debug=False, use_reloader=False)

if __name__ == "__main__":
    # Start Flask server
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Start Tkinter UI
    root = tk.Tk()
    app = PatientApp(root)
    root.mainloop()