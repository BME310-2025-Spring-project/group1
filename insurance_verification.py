import logging
import re
from typing import Optional, Dict
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class InsuranceVerificationError(Exception):
    """Base exception for insurance verification errors"""
    pass

class InvalidInsuranceIdError(InsuranceVerificationError):
    """Raised when insurance ID format is invalid"""
    pass

class InsuranceNotFoundError(InsuranceVerificationError):
    """Raised when insurance record is not found"""
    pass

class InsuranceExpiredError(InsuranceVerificationError):
    """Raised when insurance is expired"""
    pass

class InsuranceVerifier:
    def __init__(self):
        self.max_retries = 3
        self.insurance_db: Dict[str, Dict] = {}  # Simulated database

    def validate_insurance_id_format(self, insurance_id: str) -> bool:
        """Validate insurance ID format (e.g., ABC123456789)"""
        pattern = r'^[A-Z]{3}\d{9}$'
        return bool(re.match(pattern, insurance_id))

    def verify_insurance(self, insurance_id: str, retry_count: int = 0) -> Dict[str, str]:
        """
        Verify insurance information with error handling
        Returns insurance details or raises appropriate exception
        """
        try:
            # Validate ID format
            if not self.validate_insurance_id_format(insurance_id):
                logger.error(f"Invalid insurance ID format: {insurance_id}")
                raise InvalidInsuranceIdError(
                    "The insurance ID format is incorrect. Please check and enter a valid ID (e.g., ABC123456789)."
                )

            # Check if insurance exists
            insurance_info = self.insurance_db.get(insurance_id)
            if not insurance_info:
                logger.warning(f"Insurance not found: {insurance_id}")
                raise InsuranceNotFoundError(
                    "We couldn't find your insurance information. Would you like to update your details?"
                )

            # Check expiration
            expiry_date = datetime.strptime(insurance_info['expiry_date'], '%Y-%m-%d')
            if expiry_date < datetime.now():
                logger.warning(f"Insurance expired: {insurance_id}")
                raise InsuranceExpiredError(
                    "Your insurance policy has expired. Please provide updated insurance information."
                )

            logger.info(f"Insurance verified successfully: {insurance_id}")
            return insurance_info

        except (InvalidInsuranceIdError, InsuranceNotFoundError, InsuranceExpiredError) as e:
            raise e
        except Exception as e:
            logger.error(f"System error during verification: {str(e)}")
            if retry_count < self.max_retries:
                return self.verify_insurance(insurance_id, retry_count + 1)
            raise InsuranceVerificationError(
                "We're experiencing technical difficulties. Please try again later or contact support."
            )

    def update_insurance_info(self, insurance_id: str, new_info: Dict) -> bool:
        """
        Update insurance information after verification failure
        Returns True if update successful
        """
        try:
            if not self.validate_insurance_id_format(insurance_id):
                raise InvalidInsuranceIdError(
                    "The new insurance ID format is invalid. Please use format ABC123456789."
                )

            # Validate required fields
            required_fields = ['provider', 'expiry_date', 'member_name']
            if not all(field in new_info for field in required_fields):
                raise InsuranceVerificationError(
                    "Missing required insurance information. Please provide all required fields."
                )

            # Update database
            self.insurance_db[insurance_id] = new_info
            logger.info(f"Insurance information updated: {insurance_id}")
            return True

        except Exception as e:
            logger.error(f"Error updating insurance: {str(e)}")
            raise InsuranceVerificationError(
                f"Failed to update insurance information: {str(e)}. Please try again or contact support."
            )

def main():
    verifier = InsuranceVerifier()
    
    while True:
        try:
            insurance_id = input("Enter insurance ID (or 'quit' to exit): ")
            if insurance_id.lower() == 'quit':
                break

            insurance_info = verifier.verify_insurance(insurance_id)
            print("Insurance verified successfully!")
            print(f"Details: {insurance_info}")

        except InsuranceVerificationError as e:
            print(f"Error: {str(e)}")
            
            if isinstance(e, (InsuranceNotFoundError, InsuranceExpiredError)):
                update_choice = input("Would you like to update your insurance information? (y/n): ")
                if update_choice.lower() == 'y':
                    new_info = {
                        'provider': input("Enter insurance provider: "),
                        'expiry_date': input("Enter expiry date (YYYY-MM-DD): "),
                        'member_name': input("Enter member name: ")
                    }
                    try:
                        verifier.update_insurance_info(insurance_id, new_info)
                        print("Insurance information updated successfully!")
                    except InsuranceVerificationError as update_error:
                        print(f"Update failed: {str(update_error)}")

if __name__ == "__main__":
    main()