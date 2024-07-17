import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_special):
    # Define possible characters for the password
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be included.")

    # Ensure the password contains at least one of each required character type
    password = []
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if include_digits:
        password.append(random.choice(string.digits))
    if include_special:r
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random characters
    remaining_length = length - len(password)
    if remaining_length < 0:
        raise ValueError("Length is too short to include one of each required character type.")

    password.extend(random.choice(characters) for _ in range(remaining_length))

    # Shuffle the password list to ensure randomness and convert it to a string
    random.shuffle(password)
    return ''.join(password)

if __name__ == "__main__":
    try:
        # Ask the user for the desired password length
        length = int(input("Enter the desired length for your password: "))
        if length < 4:
            raise ValueError("Length must be at least 4 to include all character types.")

        # Ask the user for character type preferences
        include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        include_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

        # Generate and print the password
        password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_special)
        print("Your random password is:", password)

    except ValueError as e:
        print("Error:", e)

