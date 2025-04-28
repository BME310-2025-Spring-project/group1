import unittest
from unittest.mock import patch
from datetime import datetime
from patient_registration import PatientRegistration

class TestPatientRegistration(unittest.TestCase):
    def setUp(self):
        self.registration = PatientRegistration()

    def test_successful_registration(self):
        """Test Case PR-TC-001: Successful Patient Registration"""
        patient_data = {
            "first_name": "John",
            "last_name": "Doe",
            "dob": "1990-05-15",
            "email": "john.doe@example.com",
            "phone": "+1-555-123-4567",
            "address": "123 Main St, Springfield"
        }
        result = self.registration.register_patient(patient_data)
        self.assertTrue(result["success"])
        self.assertEqual(result["message"], "Patient registered successfully.")

    def test_empty_required_fields(self):
        """Test Case PR-TC-002: Empty Required Fields"""
        patient_data = {
            "first_name": "",
            "last_name": "",
            "dob": "",
            "email": "",
            "phone": "+1-555-123-4567",
            "address": "123 Main St, Springfield"
        }
        result = self.registration.register_patient(patient_data)
        self.assertFalse(result["success"])
        self.assertIn("First Name is required", result["message"])
        self.assertIn("Last Name is required", result["message"])
        self.assertIn("Date of Birth is required", result["message"])
        self.assertIn("Email is required", result["message"])

    def test_invalid_email_format(self):
        """Test Case PR-TC-003: Invalid Email Format"""
        patient_data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "dob": "1985-10-22",
            "email": "invalid.email",
            "phone": "+1-555-987-6543",
            "address": "456 Oak St, Springfield"
        }
        result = self.registration.register_patient(patient_data)
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Invalid email format.")

    def test_invalid_dob_format(self):
        """Test Case PR-TC-004: Invalid Date of Birth Format"""
        patient_data = {
            "first_name": "Alice",
            "last_name": "Brown",
            "dob": "2025-13-45",
            "email": "alice.brown@example.com",
            "phone": "+1-555-555-5555",
            "address": "789 Pine St, Springfield"
        }
        result = self.registration.register_patient(patient_data)
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Invalid date of birth format.")

    def test_invalid_phone_format(self):
        """Test Case PR-TC-005: Invalid Phone Number Format"""
        patient_data = {
            "first_name": "Bob",
            "last_name": "Wilson",
            "dob": "1970-03-12",
            "email": "bob.wilson@example.com",
            "phone": "12345",
            "address": "101 Maple St, Springfield"
        }
        result = self.registration.register_patient(patient_data)
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Invalid phone number format.")

    @patch('patient_registration.PatientRegistration.check_email_exists')
    def test_duplicate_email(self, mock_check_email):
        """Test Case PR-TC-006: Duplicate Email Address"""
        mock_check_email.return_value = True
        patient_data = {
            "first_name": "John",
            "last_name": "Doe",
            "dob": "1990-05-15",
            "email": "john.doe@example.com",
            "phone": "+1-555-123-4567",
            "address": "123 Main St, Springfield"
        }
        result = self.registration.register_patient(patient_data)
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Email already in use.")

    def test_maximum_field_length(self):
        """Test Case PR-TC-007: Maximum Field Length Validation"""
        patient_data = {
            "first_name": "A" * 51,  # Exceeds max length of 50
            "last_name": "Taylor",
            "dob": "1988-07-19",
            "email": "chris.taylor@example.com",
            "phone": "+1-555-111-2222",
            "address": "202 Birch St, Springfield"
        }
        result = self.registration.register_patient(patient_data)
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "First Name exceeds maximum length of 50 characters.")

if __name__ == '__main__':
    unittest.main()