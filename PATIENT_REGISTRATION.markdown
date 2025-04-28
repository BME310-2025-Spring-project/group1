# Patient Registration Frontend

## WBS Item 3.1 - Develop Patient Registration Frontend

### Overview
This document describes the patient registration frontend implemented as a Python Tkinter desktop application. The application provides a form for collecting personal and insurance information with client-side input validation.

### Features
- **Personal Information Form**:
  - First Name (required)
  - Last Name (required)
  - Date of Birth (required, YYYY-MM-DD format)
  - Email (required, valid format)
  - Phone Number (required, 10-digit format)
  - Address (required)

- **Insurance Information Form**:
  - Insurance Provider (required)
  - Policy Number (required)
  - Group Number (optional)

- **Input Validation**:
  - Enforces required fields
  - Validates email format (e.g., user@domain.com)
  - Validates phone number (10 digits)
  - Validates date of birth (YYYY-MM-DD)
  - Displays error messages in a dialog box for invalid inputs

- **Styling**:
  - Clean, organized layout using Tkinter's grid system
  - Clear section headers for personal and insurance information
  - Responsive input fields and text area for address

### Technical Details
- **Language**: Python 3
- **Library**: Tkinter for GUI
- **Dependencies**: Standard Python library (tkinter, re)
- **Validation**: Client-side validation using regular expressions and string checks
- **Form Submission**: Displays success message and logs form data to console (ready for backend integration)

### Implementation Notes
- The application uses a class-based structure (`PatientRegistrationApp`) for modularity.
- Form data is managed using Tkinter's `StringVar` for reactive updates.
- Validation is performed on submission, with errors displayed in a message box.
- The address field uses a `Text` widget to accommodate multi-line input.

### Setup Instructions
1. Save the `patient_registration.py` file.
2. Ensure Python 3 is installed with Tkinter (included in standard Python distributions).
3. Run the script using `python patient_registration.py`.
4. The GUI will launch, allowing form input and submission.

### Future Enhancements
- Integrate with a backend API for data persistence
- Add server-side validation
- Enhance UI with custom Tkinter themes or styles
- Implement unit tests for validation logic
- Add accessibility features (e.g., keyboard navigation)

### Related Issues
- WBS Item 3.1 - Develop Patient Registration Frontend