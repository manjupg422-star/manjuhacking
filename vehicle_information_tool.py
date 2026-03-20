import re

class VehicleInfoTool:
    def __init__(self, registration_number):
        self.registration_number = registration_number
        self.state_code = None
        self.vehicle_type = None
        self.registration_year = None
        self.details = None
        self.validate_registration_number()

    def validate_registration_number(self):
        pattern = re.compile(r'^[A-Z]{2}[0-9]{1,2}[A-Z]{1,2}[0-9]{4}$')  # Format: AB12CD1234
        if not pattern.match(self.registration_number):
            raise ValueError('Invalid registration number format.')
        self.extract_vehicle_details()

    def extract_vehicle_details(self):
        self.state_code = self.registration_number[0:2]  # First two letters indicate the state
        self.vehicle_type = self.registration_number[2:4]  # Next two characters indicate vehicle type
        self.registration_year = self.registration_number[4:8]  # Last four digits indicate the registration year
        self.details = {'state_code': self.state_code, 'vehicle_type': self.vehicle_type, 'registration_year': self.registration_year}

    def get_vehicle_info(self):
        return self.details

# Example Usage:
# vehicle = VehicleInfoTool('KA01MH1234')
# print(vehicle.get_vehicle_info())
