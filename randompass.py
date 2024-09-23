import random
import string

def generate_password(length, letters, numbers, symbols):
    characters = ''

    if letters:
        characters += string.ascii_letters  # Add letters 
    if numbers:
        characters += string.digits  # Add digits (
    if symbols:
        characters += string.punctuation  # Add specia character

    # Generate password by randomly selecting characters 
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Password Generator")
    print("------------------")

    length = int(input("Enter password length: "))
    
    # Get user preferences for character types
    letters = input("Include letters? (y/n): ").lower() == 'y'
    numbers = input("Include numbers? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, letters, numbers, symbols)

    print("Generated Password:", password)

if __name__ == "__main__":
    main()
