# Patient Registration Test Cases

## Test Suite: Patient Registration Flow
**Related WBS Item**: 4.1 - Create Test Cases for Registration Flow  
**Module**: Patient Registration  
**Objective**: Verify the functionality of the patient registration process, including validation of inputs and successful registration.

---

### Test Case 1: Successful Patient Registration
**Test ID**: PR-TC-001  
**Description**: Verify that a user can successfully register a patient with valid input data.  
**Preconditions**: 
- User is logged into the system with appropriate permissions.
- Registration form is accessible.  
**Test Steps**:  
1. Navigate to the patient registration form.  
2. Enter valid data in all required fields:  
   - First Name: John  
   - Last Name: Doe  
   - Date of Birth: 1990-05-15  
   - Email: john.doe@example.com  
   - Phone: +1-555-123-4567  
   - Address: 123 Main St, Springfield  
3. Click the "Submit" button.  
**Expected Result**:  
- Patient is successfully registered.  
- Success message is displayed: "Patient registered successfully."  
- Patient data is saved in the database.  
**Test Type**: Functional  
**Priority**: High  

---

### Test Case 2: Empty Required Fields
**Test ID**: PR-TC-002  
**Description**: Verify that the system prevents registration when required fields are left empty.  
**Preconditions**: 
- User is logged into the system with appropriate permissions.
- Registration form is accessible.  
**Test Steps**:  
1. Navigate to the patient registration form.  
2. Leave all required fields (First Name, Last Name, Date of Birth, Email) empty.  
3. Click the "Submit" button.  
**Expected Result**:  
- Form submission is prevented.  
- Error message is displayed for each empty required field, e.g., "First Name is required."  
- Patient is not registered.  
**Test Type**: Negative  
**Priority**: High  

---

### Test Case 3: Invalid Email Format
**Test ID**: PR-TC-003  
**Description**: Verify that the system rejects registration with an invalid email format.  
**Preconditions**: 
- User is logged into the system with appropriate permissions.
- Registration form is accessible.  
**Test Steps**:  
1. Navigate to the patient registration form.  
2. Enter the following data:  
   - First Name: Jane  
   - Last Name: Smith  
   - Date of Birth: 1985-10-22  
   - Email: invalid.email  
   - Phone: +1-555-987-6543  
   - Address: 456 Oak St, Springfield  
3. Click the "Submit" button.  
**Expected Result**:  
- Form submission is prevented.  
- Error message is displayed: "Invalid email format."  
- Patient is not registered.  
**Test Type**: Negative  
**Priority**: Medium  

---

### Test Case 4: Invalid Date of Birth Format
**Test ID**: PR-TC-004  
**Description**: Verify that the system rejects registration with an invalid date of birth format.  
**Preconditions**: 
- User is logged into the system with appropriate permissions.
- Registration form is accessible.  
**Test Steps**:  
1. Navigate to the patient registration form.  
2. Enter the following data:  
   - First Name: Alice  
   - Last Name: Brown  
   - Date of Birth: 2025-13-45 (invalid date)  
   - Email: alice.brown@example.com  
   - Phone: +1-555-555-5555  
   - Address: 789 Pine St, Springfield  
3. Click the "Submit" button.  
**Expected Result**:  
- Form submission is prevented.  
- Error message is displayed: "Invalid date of birth format."  
- Patient is not registered.  
**Test Type**: Negative  
**Priority**: Medium  

---

### Test Case 5: Invalid Phone Number Format
**Test ID**: PR-TC-005  
**Description**: Verify that the system rejects registration with an invalid phone number format.  
**Preconditions**: 
- User is logged into the system with appropriate permissions.
- Registration form is accessible.  
**Test Steps**:  
1. Navigate to the patient registration form.  
2. Enter the following data:  
   - First Name: Bob  
   - Last Name: Wilson  
   - Date of Birth: 1970-03-12  
   - Email: bob.wilson@example.com  
   - Phone: 12345 (invalid format)  
   - Address: 101 Maple St, Springfield  
3. Click the "Submit" button.  
**Expected Result**:  
- Form submission is prevented.  
- Error message is displayed: "Invalid phone number format."  
- Patient is not registered.  
**Test Type**: Negative  
**Priority**: Medium  

---

### Test Case 6: Duplicate Email Address
**Test ID**: PR-TC-006  
**Description**: Verify that the system prevents registration with an email already in use.  
**Preconditions**: 
- User is logged into the system with appropriate permissions.
- Registration form is accessible.  
- A patient with email "john.doe@example.com" already exists in the database.  
**Test Steps**:  
1. Navigate to the patient registration form.  
2. Enter the following data:  
   - First Name: John  
   - Last Name: Doe  
   - Date of Birth: 1990-05-15  
   - Email: john.doe@example.com  
   - Phone: +1-555-123-4567  
   - Address: 123 Main St, Springfield  
3. Click the "Submit" button.  
**Expected Result**:  
- Form submission is prevented.  
- Error message is displayed: "Email already in use."  
- Patient is not registered.  
**Test Type**: Negative  
**Priority**: High  

---

### Test Case 7: Maximum Field Length Validation
**Test ID**: PR-TC-007  
**Description**: Verify that the system rejects input exceeding maximum field length for First Name.  
**Preconditions**: 
- User is logged into the system with appropriate permissions.
- Registration form is accessible.  
**Test Steps**:  
1. Navigate to the patient registration form.  
2. Enter the following data:  
   - First Name: [A string longer than the maximum allowed length, e.g., 51 characters]  
   - Last Name: Taylor  
   - Date of Birth: 1988-07-19  
   - Email: chris.taylor@example.com  
   - Phone: +1-555-111-2222  
   - Address: 202 Birch St, Springfield  
3. Click the "Submit" button.  
**Expected Result**:  
- Form submission is prevented.  
- Error message is displayed: "First Name exceeds maximum length of 50 characters."  
- Patient is not registered.  
**Test Type**: Negative  
**Priority**: Medium  

---

## Notes
- All test cases assume a standard web-based patient registration form.
- Negative test cases focus on common validation errors (empty fields, invalid formats, duplicates).
- Test cases can be extended to cover additional edge cases, such as special characters or SQL injection attempts, based on requirements.
- These test cases are designed to be uploaded to GitHub as part of the project documentation.