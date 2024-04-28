import random

def forward_reverse_number():
    number = random.randint(1000, 9999)
    
    # Convert the number to a string to make reversing easier
    number_str = str(number)
    
    print("Forward Number:", number)
    
    reverse_number = int(number_str[::-1])
    print("Reverse Number:", reverse_number)

forward_reverse_number()
