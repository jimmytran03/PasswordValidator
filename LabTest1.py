# Jimmy Tran C22733065

import random
import string

# Part 1
def is_valid(password):
    """Checks if the password meets the criteria."""
    if len(password) < 10:
        return False

    if not any(char in string.digits for char in password):
        return False

    if not any(char in string.ascii_uppercase for char in password):
        return False

    if not any(char in string.punctuation for char in password):
        return False

    return True

# Part 2
def strengthen_password(password):
    """Strengthens the password if it doesn't meet the criteria."""
    while len(password) < 10:
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

    if not any(char in string.digits for char in password):
        password += random.choice(string.digits)

    if not any(char in string.ascii_uppercase for char in password):
        password += random.choice(string.ascii_uppercase)

    if not any(char in string.punctuation for char in password):
        password += random.choice(string.punctuation)

    # Shuffle password to mix newly added characters
    password = ''.join(random.sample(password, len(password)))

    return password

# Main scope
if __name__ == "__main__":
    while True:
        secure = input("Enter a password for evaluation (or type 'exit' to quit): ")
        if secure.lower() == 'exit':
            break

        if is_valid(secure):
            print("Password is valid.")
        else:
            print("Password is not valid.")
            new_password = strengthen_password(secure)
            print(f"New suggested password: {new_password}")




