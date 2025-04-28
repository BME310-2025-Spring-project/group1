# Patient Registration and Insurance Verification Integration Guide

This guide outlines the integration of the Patient Registration and Insurance Verification UI forms with backend API endpoints. The solution uses a React frontend with Tailwind CSS and a Flask backend.

## Overview
- **Frontend**: React app with two forms (Patient Registration and Insurance Verification).
- **Backend**: Flask API with endpoints `/api/patient/register` and `/api/insurance/verify`.
- **Communication**: Forms send data to the backend via HTTP POST requests using `fetch`. Responses are handled to display success or error messages.
- **Deliverable**: Working UI forms integrated with backend APIs, with graceful error handling.

## Setup Instructions

### Backend Setup
1. **Install Dependencies**:
   - Python 3.8+
   - Install Flask: `pip install flask`
2. **Run the Backend**:
   - Save the backend code in `backend_api.py`.
   - Run the server: `python backend_api.py`.
   - The API will be available at `http://localhost:5000`.

### Frontend Setup
1. **Create React App**:
   - Use Create React App or a similar setup.
   - Install dependencies: `npm install`.
2. **Add Tailwind CSS**:
   - Follow Tailwind CSS CDN setup (included in the HTML below).
3. **Add Frontend Code**:
   - Copy the provided React code into your project (see below).
4. **Run the Frontend**:
   - Start the React app: `npm start`.
   - The app will be available at `http://localhost:3000`.

## API Endpoints

### 1. Patient Registration
- **Endpoint**: `POST /api/patient/register`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "dob": "1990-01-01",
    "email": "john@example.com"
  }
  ```
- **Response**:
  - Success (200):
    ```json
    {
      "message": "Patient registered successfully",
      "patient_id": "12345"
    }
    ```
  - Error (400):
    ```json
    {
      "error": "Missing required fields"
    }
    ```

### 2. Insurance Verification
- **Endpoint**: `POST /api/insurance/verify`
- **Request Body**:
  ```json
  {
    "provider": "Blue Cross",
    "policy_number": "ABC123456"
  }
  ```
- **Response**:
  - Success (200):
    ```json
    {
      "message": "Insurance verified successfully",
      "status": "valid"
    }
    ```
  - Error (400):
    ```json
    {
      "error": "Invalid policy number"
    }
    ```

## Frontend Code

Below is the React frontend code for the forms, integrated with the backend APIs. Save this as `index.html` in your React project.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Patient Registration & Insurance Verification</title>
  <script src="https://cdn.jsdelivr.net/npm/react@18.2.0/umd/react.development.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/react-dom@18.2.0/umd/react-dom.development.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/babel-standalone@7.22.9/babel.min.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel">
    function PatientForm() {
      const [formData, setFormData] = React.useState({ name: '', dob: '', email: '' });
      const [message, setMessage] = React.useState('');

      const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
      };

      const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage('');
        try {
          const response = await fetch('http://localhost:5000/api/patient/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
          });
          const data = await response.json();
          if (response.ok) {
            setMessage(`Success: ${data.message} (Patient ID: ${data.patient_id})`);
          } else {
            setMessage(`Error: ${data.error}`);
          }
        } catch (error) {
          setMessage('Error: Failed to connect to the server');
        }
      };

      return (
        <div className="max-w-md mx-auto p-4">
          <h2 className="text-2xl font-bold mb-4">Patient Registration</h2>
          <div>
            <div className="mb-4">
              <label className="block text-gray-700">Name</label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                className="w-full p-2 border rounded"
                required
              />
            </div>
            <div className="mb-4">
              <label className="block text-gray-700">Date of Birth</label>
              <input
                type="date"
                name="dob"
                value={formData.dob}
                onChange={handleChange}
                className="w-full p-2 border rounded"
                required
              />
            </div>
            <div className="mb-4">
              <label className="block text-gray-700">Email</label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                className="w-full p-2 border rounded"
                required
              />
            </div>
            <button
              onClick={handleSubmit}
              className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
            >
              Register
            </button>
            {message && <p className="mt-4 text-center">{message}</p>}
          </div>
        </div>
      );
    }

    function InsuranceForm() {
      const [formData, setFormData] = React.useState({ provider: '', policy_number: '' });
      const [message, setMessage] = React.useState('');

      const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
      };

      const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage('');
        try {
          const response = await fetch('http://localhost:5000/api/insurance/verify', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
          });
          const data = await response.json();
          if (response.ok) {
            setMessage(`Success: ${data.message} (Status: ${data.status})`);
          } else {
            setMessage(`Error: ${data.error}`);
          }
        } catch (error) {
          setMessage('Error: Failed to connect to the server');
        }
      };

      return (
        <div className="max-w-md mx-auto p-4">
          <h2 className="text-2xl font-bold mb-4">Insurance Verification</h2>
          <div>
            <div className="mb-4">
              <label className="block text-gray-700">Insurance Provider</label>
              <input
                type="text"
                name="provider"
                value={formData.provider}
                onChange={handleChange}
                className="w-full p-2 border rounded"
                required
              />
            </div>
            <div className="mb-4">
              <label className="block text-gray-700">Policy Number</label>
              <input
                type="text"
                name="policy_number"
                value={formData.policy_number}
                onChange={handleChange}
                className="w-full p-2 border rounded"
                required
              />
            </div>
            <button
              onClick={handleSubmit}
              className="w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
            >
              Verify
            </button>
            {message && <p className="mt-4 text-center">{message}</p>}
          </div>
        </div>
      );
    }

    function App() {
      return (
        <div className="min-h-screen bg-gray-100">
          <h1 className="text-3xl font-bold text-center py-6">Healthcare Portal</h1>
          <PatientForm />
          <InsuranceForm />
        </div>
      );
    }

    ReactDOM.render(<App />, document.getElementById('root'));
  </script>
</body>
</html>
```

## Backend Code
The backend code is provided in `backend_api.py`. It includes:
- Flask server setup.
- Two endpoints: `/api/patient/register` and `/api/insurance/verify`.
- Basic validation and simulated processing.

## Testing the Integration
1. Start the backend server (`python backend_api.py`).
2. Start the frontend app (`npm start`).
3. Open `http://localhost:3000` in a browser.
4. Fill out and submit the Patient Registration form:
   - Enter name, DOB, and email.
   - Check for a success message with a patient ID or an error message.
5. Fill out and submit the Insurance Verification form:
   - Enter provider and policy number.
   - Check for a success message with verification status or an error message.
6. Test error cases:
   - Submit empty forms to trigger validation errors.
   - Stop the backend server and submit a form to test network error handling.

## Error Handling
- **Frontend**:
  - Displays error messages for invalid inputs, server errors, or network failures.
  - Success messages include relevant data (e.g., patient ID, verification status).
- **Backend**:
  - Validates required fields.
  - Returns appropriate HTTP status codes (200 for success, 400 for errors).

## Deployment Notes
- Ensure CORS is enabled on the backend for cross-origin requests (handled in `backend_api.py`).
- For production, use a proper database instead of simulated responses.
- Secure the API with authentication and HTTPS.

## Related WBS Item
- **WBS Item 3.5**: Integrate Frontend with Backend APIs.

This integration provides a fully functional system for patient registration and insurance verification, with robust error handling and user feedback.