import requests

class VehicleAPI:
    def __init__(self, use_mock_db=True):
        self.use_mock_db = use_mock_db
        self.mock_db = self.mock_vehicle_data() if use_mock_db else None

    def mock_vehicle_data(self):
        return [
            {'vehicle_id': '1', 'make': 'Honda', 'model': 'Civic', 'year': 2020},
            {'vehicle_id': '2', 'make': 'Toyota', 'model': 'Camry', 'year': 2021},
            {'vehicle_id': '3', 'make': 'Ford', 'model': 'Mustang', 'year': 2022}
        ]

    def get_vehicle_info(self, vehicle_id):
        if self.use_mock_db:
            return self._get_mock_vehicle_info(vehicle_id)
        else:
            return self._get_real_vehicle_info(vehicle_id)

    def _get_mock_vehicle_info(self, vehicle_id):
        for vehicle in self.mock_db:
            if vehicle['vehicle_id'] == vehicle_id:
                return vehicle
        return None

    def _get_real_vehicle_info(self, vehicle_id):
        # Here you would implement the call to the real RTO API.
        # For example purposes, the implementation is mocked.
        rto_api_url = f'https://api.example.com/vehicles/{vehicle_id}'
        response = requests.get(rto_api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

# Example usage:
# vehicle_api = VehicleAPI(use_mock_db=True)
# vehicle_info = vehicle_api.get_vehicle_info('1')
# print(vehicle_info)
