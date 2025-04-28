# Patient Registration and Insurance Verification Integration

## Overview
This integration connects the Patient Registration and Insurance Verification UI forms with backend API endpoints, ensuring proper data submission and response handling. The solution uses Flask for the backend and Tkinter for the frontend, with error handling and user feedback.

Related to: WBS Item 3.5 - Integrate Frontend with Backend APIs

## Files
- `patient_forms.py`: Contains the integrated UI forms and API connectivity logic.
- `patient_forms_integration.md`: This documentation.

## Backend API Endpoints
- **POST /api/patient/register**: Handles patient registration data.
- **POST /api/insurance/verify**: Verifies insurance information.

## Setup Instructions
1. **Install dependencies**:
   ```bash
   pip install flask requests tkinter
   ```
2. **Run the backend**:
   ```bash
   python patient_forms.py
   ```
3. The UI will launch automatically, and the Flask server will run on `http://localhost:5000`.

## Usage
- **Patient Registration Form**:
  - Fields: First Name, Last Name, Date of Birth, Email.
  - Submits data to `/api/patient/register`.
  - Displays success or error messages.
- **Insurance Verification Form**:
  - Fields: Insurance Provider, Policy Number.
  - Submits data to `/api/insurance/verify`.
  - Displays verification status.

## Error Handling
- Validates form inputs before submission.
- Handles API errors (e.g., 400, 500) with user-friendly messages.
- Catches network issues and displays appropriate alerts.

## Testing
- Test patient registration with valid/invalid data.
- Test insurance verification with sample policy numbers.
- Simulate API failures to ensure error messages display correctly.

## Notes
- The backend includes mock API responses for demonstration.
- For production, replace mock logic with actual database or external API calls.
- Ensure CORS is configured if the frontend and backend are hosted separately.