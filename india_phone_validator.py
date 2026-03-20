import re

class IndiaPhoneValidator:
    TELECOM_PROVIDERS = {
        'Airtel': '720, 721, 738, 740, 742',
        'Vodafone': '730, 731, 732',
        'Jio': '700, 701, 702',
        'BSNL': '800, 801, 802',
        'MTNL': '900, 901, 902'
    }

    @staticmethod
    def validate_number(number):
        pattern = re.compile(r'^[6789]\d{9}$')
        return bool(pattern.match(number))

    @classmethod
    def get_provider(cls, number):
        if not cls.validate_number(number):
            return None
        prefix = number[:4]  # Analyze the first few digits
        for provider, ranges in cls.TELECOM_PROVIDERS.items():
            if prefix in ranges.split(', '):
                return provider
        return 'Unknown Provider'

    @staticmethod
    def number_properties(number):
        return {
            'length': len(number), 
            'is_valid': IndiaPhoneValidator.validate_number(number)
        }

    @staticmethod
    def alternate_sim_info(number):
        properties = IndiaPhoneValidator.number_properties(number)
        if properties['is_valid']:
            return f'This number seems valid and belongs to {IndiaPhoneValidator.get_provider(number)}.'
        else:
            return 'This number is not valid.'

# Example usage
if __name__ == "__main__":
    phone_number = input("Enter an Indian phone number: ")
    validator = IndiaPhoneValidator()
    if validator.validate_number(phone_number):
        print(validator.alternate_sim_info(phone_number))
    else:
        print("Invalid phone number format.")