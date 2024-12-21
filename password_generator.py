import random
import string

def generate_password(length):
  
    if length < 4:
        print("Password length should be at least 4 for strong passwords.")
        return None

    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one character from each category
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to randomize character order
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    print("--- Password Generator ---")
    try:
        length = int(input("Enter the desired password length: "))
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
