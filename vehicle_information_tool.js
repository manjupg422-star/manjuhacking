// vehicle_information_tool.js

/**
 * Validates Indian vehicle registration numbers and extracts details such as state, vehicle type, and registration year.
 */

class VehicleInformationTool {
    static validateRegistrationNumber(regNumber) {
        const regex = /^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$/;
        return regex.test(regNumber);
    }

    static extractState(regNumber) {
        const stateCodes = {
            'DL': 'Delhi',
            'MH': 'Maharashtra',
            'KA': 'Karnataka',
            // Add more states as necessary
        };
        const stateCode = regNumber.substring(0, 2);
        return stateCodes[stateCode] || 'Unknown State';
    }

    static identifyVehicleType(regNumber) {
        const typeCode = regNumber.substring(2, 4);
        switch (typeCode) {
            case '01': return 'Two-Wheeler';
            case '02': return 'Car';
            // More mappings can be added
            default: return 'Other';
        }
    }

    static extractRegistrationYear(regNumber) {
        const yearCode = regNumber.substring(4, 6);
        return `20${yearCode}`; // Assuming '00' is 2000, '99' is 1999, etc.
    }

    static getVehicleDetails(regNumber) {
        if (!this.validateRegistrationNumber(regNumber)) {
            throw new Error('Invalid registration number');
        }
        return {
            state: this.extractState(regNumber),
            type: this.identifyVehicleType(regNumber),
            year: this.extractRegistrationYear(regNumber)
        };
    }
}

// Example Usage:
try {
    const regNum = 'DL01AB1234'; // Change to any other registration number for testing
    const vehicleDetails = VehicleInformationTool.getVehicleDetails(regNum);
    console.log(vehicleDetails);
} catch (error) {
    console.error(error.message);
}