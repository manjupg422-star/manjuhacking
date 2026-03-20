// india_phone_validator.js

/**
 * Validates Indian phone numbers, detects telecom providers,
 * analyzes number properties, and provides alternate SIM information.
 */

class IndiaPhoneValidator {
    constructor(number) {
        this.number = number;
        this.telecomProviders = {
            'Airtel': /^\+91-?([6789]\d{9})$/,  
            'Jio': /^\+91-?([789]\d{9})$/,  
            'Vodafone': /^\+91-?([6789]\d{9})$/,
            'BSNL': /^\+91-?([789]\d{9})$/
        };
    }

    validate() {
        const regex = /^\+91-?\d{10}$/;
        return regex.test(this.number);
    }

    getTelecomProvider() {
        for (let provider in this.telecomProviders) {
            if (this.telecomProviders[provider].test(this.number)) {
                return provider;
            }
        }
        return 'Unknown Provider';
    }

    analyzeNumber() {
        return {
            isValid: this.validate(),
            provider: this.getTelecomProvider()
        };
    }

    static alternateSIMInfo() {
        return {
            suggestions: ['Airtel', 'Jio', 'Vodafone', 'BSNL'],
            info: 'Consider checking offers from these providers for better pricing.'
        };
    }
}

// Example usage:
const phoneNumber = '+91-9876543210';
const validator = new IndiaPhoneValidator(phoneNumber);
console.log(validator.analyzeNumber());
console.log(IndiaPhoneValidator.alternateSIMInfo());