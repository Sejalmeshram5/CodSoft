import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    try:
        length = int(input("Enter the desired length for the password (or 0 to exit): "))
        if length == 0:
            print("Exiting...")
            break
        elif length < 0:
            print("Please enter a positive number.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")
