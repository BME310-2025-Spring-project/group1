# Insurance Verification API Documentation

## Overview
This API provides endpoints to verify patient insurance eligibility by simulating a connection to an insurance database. It supports checking eligibility status and retrieving coverage details based on patient and insurance information.

Related to WBS Item 3.3 - Develop Insurance Verification API.

## Endpoints

### 1. GET /api/insurance/eligibility
- **Description**: Retrieves insurance eligibility status for a patient using query parameters.
- **Query Parameters**:
  - `patient_id` (string, required): Unique patient identifier.
  - `insurance_id` (string, required): Insurance policy number.
  - `service_date` (string, optional): Date of service (format: YYYY-MM-DD).
- **Response**:
  - **200 OK**: Eligibility details.
    ```json
    {
      "patient_id": "string",
      "insurance_id": "string",
      "eligibility_status": "active|inactive|not_found",
      "coverage_details": {
        "plan_name": "string",
        "effective_date": "string",
        "expiration_date": "string",
        "copay": number,
        "deductible": number
      },
      "message": "string"
    }
    ```
  - **400 Bad Request**: Missing or invalid parameters.
  - **500 Internal Server Error**: Server error.

### 2. POST /api/insurance/eligibility
- **Description**: Verifies insurance eligibility using a JSON payload.
- **Request Body**:
  ```json
  {
    "patient_id": "string",
    "insurance_id": "string",
    "first_name": "string",
    "last_name": "string",
    "date_of_birth": "string",
    "service_date": "string" // Optional, format: YYYY-MM-DD
  }
  ```
- **Response**:
  - **200 OK**: Eligibility details (same structure as GET response).
  - **400 Bad Request**: Missing or invalid fields.
  - **500们 Internal Server Error**: Server error.

## Simulated Insurance Database
- The API uses an in-memory dictionary to simulate an insurance database.
- Contains sample insurance records with eligibility details.
- In a production environment, this would be replaced with a real database connection.

## Setup and Running
1. Install dependencies:
   ```bash
   pip install flask
   ```
2. Save the Python script as `insurance_verification_api.py`.
3. Run the API:
   ```bash
   python insurance_verification_api.py
   ```
4. The API will be available at `http://localhost:5000`.

## Example Usage
### GET Request
```bash
curl "http://localhost:5000/api/insurance/eligibility?patient_id=P123&insurance_id=INS456&service_date=2025-04-28"
```

### POST Request
```bash
curl -X POST http://localhost:5000/api/insurance/eligibility \
-H "Content-Type: application/json" \
-d '{
  "patient_id": "P123",
  "insurance_id": "INS456",
  "first_name": "John",
  "last_name": "Doe",
  "date_of_birth": "1980-01-01",
  "service_date": "2025-04-28"
}'
```

## Error Handling
- Validates input parameters and request body.
- Returns appropriate error messages for missing or invalid data.
- Logs errors for debugging (console output in this implementation).

## Notes
- This is a simplified implementation for demonstration purposes.
- In production, add:
  - Authentication and authorization.
  - Rate limiting.
  - Input sanitization.
  - Connection to a real insurance database or third-party eligibility service.
  - Proper logging and monitoring.