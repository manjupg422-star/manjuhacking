import re

# Define test cases for Indian phone numbers
valid_phone_numbers = [
    '9876543210',  # Valid 10-digit number
    '91 9876543210',  # Valid international format
    '+91 9876543210'  # Valid international format with +
]

invalid_phone_numbers = [
    '123456',  # Too short
    '98765abcde',  # Invalid characters
    '987654321012',  # Too long
    '91 98765abcde'  # Invalid international format
]

# Define test cases for vehicle registration numbers
valid_vehicle_registration_numbers = [
    'MH12AB1234',  # Valid format
    'KA01AB1234',  # Valid format
    'TN07CD5678'  # Valid format
]

invalid_vehicle_registration_numbers = [
    'MH12AB',  # Too short
    'KA01AB12345',  # Too long
    '1234AB1234',  # Invalid state code
    'MH12 AB1234'  # Invalid format with space
]

# Define test cases for weather cities
valid_weather_cities = [
    'Mumbai',
    'Delhi',
    'Bangalore',
]

invalid_weather_cities = [
    'CityThatDoesNotExist',  # Non-existent city
    ' ',  # Empty string
    '12345',  # Numeric input only
]


def test_phone_numbers():
    for number in valid_phone_numbers:
        assert re.match(r'^(\+91[\s]?)?[0]?[6789]\d{9}$', number), f'Failed for valid phone number: {number}'
    for number in invalid_phone_numbers:
        assert not re.match(r'^(\+91[\s]?)?[0]?[6789]\d{9}$', number), f'Failed for invalid phone number: {number}'


def test_vehicle_registration_numbers():
    for number in valid_vehicle_registration_numbers:
        assert re.match(r'^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$', number), f'Failed for valid vehicle registration number: {number}'
    for number in invalid_vehicle_registration_numbers:
        assert not re.match(r'^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$', number), f'Failed for invalid vehicle registration number: {number}'


def test_weather_cities():
    for city in valid_weather_cities:
        assert isinstance(city, str) and len(city.strip()) > 0, f'Failed for valid weather city: {city}'
    for city in invalid_weather_cities:
        assert not (isinstance(city, str) and len(city.strip()) > 0), f'Failed for invalid weather city: {city}'


def run_tests():
    test_phone_numbers()
    test_vehicle_registration_numbers()
    test_weather_cities()
    print('All tests passed!')

if __name__ == '__main__':
    run_tests()