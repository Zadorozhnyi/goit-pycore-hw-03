import re

def normalize_phone(phone_number: str) -> str:
    # Remove all characters except "+" and numbers
    cleaned_phone = re.sub(r'[^+\d]', '', phone_number.strip())
    
    if not cleaned_phone.startswith('+'):
        if cleaned_phone.startswith('380'):
            # Add '+' if number starts with 38
            cleaned_phone = '+' + cleaned_phone
        else:
            # Add international code if number starts with 0
            cleaned_phone = '+38' + cleaned_phone
    
    return cleaned_phone


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)