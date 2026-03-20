# India Phone Number Information Tool

## Features
- Validate Indian phone numbers
- Format numbers into standard formats
- Check for telecom operators

## Usage Examples

### Python
```python
from phone_info import PhoneNumber

number = PhoneNumber("+919876543210")
if number.is_valid():
    print(f"{number} is valid")
else:
    print(f"{number} is not valid")
```

### JavaScript
```javascript
const phoneInfo = require('phone-info');

const number = '+919876543210';
phoneInfo.validate(number).then(result => {
    if(result.isValid) {
        console.log(`${number} is valid`);
    } else {
        console.log(`${number} is not valid`);
    }
});
```

## Validating Numbers
- Use the `is_valid()` method in Python or the `validate()` function in JavaScript for checking the validity of phone numbers.