# zentronex_password_gen.py
import secrets
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    alphabet = string.ascii_lowercase
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_+="

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

print("=== Zentronex Password Generator ===")
length = int(input("Password length (default 12): ") or 12)
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

password = generate_password(length, use_upper, use_digits, use_symbols)
print("\nGenerated Password:", password)