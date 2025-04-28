import tkinter as tk
from tkinter import messagebox
import re

class PatientRegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Patient Registration")
        self.root.geometry("600x700")
        
        # Form data
        self.form_data = {
            'first_name': tk.StringVar(),
            'last_name': tk.StringVar(),
            'dob': tk.StringVar(),
            'email': tk.StringVar(),
            'phone': tk.StringVar(),
            'address': tk.StringVar(),
            'insurance_provider': tk.StringVar(),
            'policy_number': tk.StringVar(),
            'group_number': tk.StringVar()
        }
        
        # Create form
        self.create_form()
        
    def create_form(self):
        # Main frame
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Title
        tk.Label(main_frame, text="Patient Registration", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Personal Information
        tk.Label(main_frame, text="Personal Information", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)
        
        # First Name
        tk.Label(main_frame, text="First Name *").pack(anchor="w")
        tk.Entry(main_frame, textvariable=self.form_data['first_name']).pack(fill="x", pady=2)
        
        # Last Name
        tk.Label(main_frame, text="Last Name *").pack(anchor="w")
        tk.Entry(main_frame, textvariable=self.form_data['last_name']).pack(fill="x", pady=2)
        
        # Date of Birth
        tk.Label(main_frame, text="Date of Birth (YYYY-MM-DD) *").pack(anchor="w")
        tk.Entry(main_frame, textvariable=self.form_data['dob']).pack(fill="x", pady=2)
        
        # Email
        tk.Label(main_frame, text="Email *").pack(anchor="w")
        tk.Entry(main_frame, textvariable=self.form_data['email']).pack(fill="x", pady=2)
        
        # Phone
        tk.Label(main_frame, text="Phone Number (10 digits) *").pack(anchor="w")
        tk.Entry(main_frame, textvariable=self.form_data['phone']).pack(fill="x", pady=2)
        
        # Address
        tk.Label(main_frame, text="Address *").pack(anchor="w")
        tk.Text(main_frame, height=3).pack(fill="x", pady=2)
        
        # Insurance Information
        tk.Label(main_frame, text="Insurance Information", font=("Arial", 12, "bold")).pack(anchor="w", pady=10)
        
        # Insurance Provider
        tk.Label(main_frame, text="Insurance Provider *").pack(anchor="w")
        tk.Entry(main_frame, textvariable=self.form_data['insurance_provider']).pack(fill="x", pady=2)
        
        # Policy Number
        tk.Label(main_frame, text="Policy Number *").pack(anchor="w")
        tk.Entry(main_frame, textvariable=self.form_data['policy_number']).pack(fill="x", pady=2)
        
        # Group Number
        tk.Label(main_frame, text="Group Number").pack(anchor="w")
        tk.Entry(main_frame, textvariable=self.form_data['group_number']).pack(fill="x", pady=2)
        
        # Submit Button
        tk.Button(main_frame, text="Submit Registration", command=self.validate_and_submit, bg="#4f46e5", fg="white", pady=5).pack(pady=20)
    
    def validate_and_submit(self):
        errors = []
        
        # Validation rules
        if not self.form_data['first_name'].get().strip():
            errors.append("First Name is required")
        if not self.form_data['last_name'].get().strip():
            errors.append("Last Name is required")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", self.form_data['dob'].get()):
            errors.append("Date of Birth must be in YYYY-MM-DD format")
        if not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", self.form_data['email'].get()):
            errors.append("Valid Email is required")
        if not re.match(r"^\d{10}$", self.form_data['phone'].get()):
            errors.append("Phone Number must be 10 digits")
        if not self.form_data['address'].get().strip():
            errors.append("Address is required")
        if not self.form_data['insurance_provider'].get().strip():
            errors.append("Insurance Provider is required")
        if not self.form_data['policy_number'].get().strip():
            errors.append("Policy Number is required")
        
        if errors:
            messagebox.showerror("Validation Error", "\n".join(errors))
        else:
            messagebox.showinfo("Success", "Registration submitted successfully!")
            print("Form Data:", {key: var.get() for key, var in self.form_data.items()})

if __name__ == "__main__":
    root = tk.Tk()
    app = PatientRegistrationApp(root)
    root.mainloop()