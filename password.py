import random
import string


def generate_password(length, use_letters, use_digits, use_symbols):
    char_pool = ""

    if use_letters:
        char_pool += string.ascii_letters
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not char_pool:
        return None

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1

    if score <= 1:
        return "Weak"
    elif score == 2 or score == 3:
        return "Medium"
    else:
        return "Strong"


def main():
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Length must be greater than 0.")
            return

        print("\nChoose options (y/n):")
        use_letters = input("Include letters? ").lower() == 'y'
        use_digits = input("Include numbers? ").lower() == 'y'
        use_symbols = input("Include symbols? ").lower() == 'y'

        password = generate_password(length, use_letters, use_digits, use_symbols)

        if password is None:
            print("You must select at least one character type!")
            return

        strength = check_strength(password)

        print("\nGenerated Password:", password)
        print("Password Strength:", strength)

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()