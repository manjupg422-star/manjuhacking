# Mock Vehicle Database

"""
This file contains a mock vehicle database for educational testing purposes.
It includes details such as registration number, owner details, vehicle details,
finance status, insurance, and pollution certificate information.
"""

# Sample Data
mock_vehicle_data = [
    {
        "registration_number": "ABC1234",
        "owner_details": {
            "name": "John Doe",
            "address": "123 Elm Street, Springfield",
            "contact_number": "123-456-7890"
        },
        "vehicle_details": {
            "make": "Toyota",
            "model": "Camry",
            "year": 2021,
            "color": "Blue"
        },
        "finance_status": {
            "loan_amount": 20000,
            "monthly_installment": 400,
            "pending_amount": 8000
        },
        "insurance": {
            "provider": "Best Insurance Co.",
            "policy_number": "INS123456",
            "expiry_date": "2026-12-31"
        },
        "pollution_certificate": {
            "certificate_number": "PC789056",
            "expiry_date": "2026-06-30"
        }
    },
    {
        "registration_number": "XYZ5678",
        "owner_details": {
            "name": "Jane Smith",
            "address": "456 Oak Avenue, Metropolis",
            "contact_number": "987-654-3210"
        },
        "vehicle_details": {
            "make": "Honda",
            "model": "Civic",
            "year": 2020,
            "color": "Red"
        },
        "finance_status": {
            "loan_amount": 18000,
            "monthly_installment": 350,
            "pending_amount": 5000
        },
        "insurance": {
            "provider": "Secure Insurance LLC",
            "policy_number": "INS654321",
            "expiry_date": "2025-11-30"
        },
        "pollution_certificate": {
            "certificate_number": "PC654321",
            "expiry_date": "2025-09-15"
        }
    }
]