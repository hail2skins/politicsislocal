import random
import string

def randomize_letters_and_numbers(value):
    # Check if the input value is None and return it immediately if so
    if value is None:
        return value

    # Proceed with randomization if the value is not None
    randomized = ''.join(
        random.choice(string.ascii_letters) if c.isalpha() else 
        random.choice(string.digits) if c.isdigit() else 
        c 
        for c in value
    )
    return randomized