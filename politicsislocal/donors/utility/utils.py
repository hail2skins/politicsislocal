import random
import string

def randomize_letters_and_numbers(value):
    randomized = ''.join(
        random.choice(string.ascii_letters) if c.isalpha() else 
        random.choice(string.digits) if c.isdigit() else 
        c 
        for c in value
    )
    return randomized