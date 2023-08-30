import random
import string

def generate_password(name):
    uppercase = random.choice(name).upper()
    lowercase = random.choice(name).lower()
    special = random.choice(string.punctuation)
    digit = random.choice(string.digits)
    
    remaining_length = 10 - (len(uppercase) + len(lowercase) + len(special) + len(digit))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = (
        uppercase + lowercase + special + digit +
        ''.join(random.choice(characters) for _ in range(remaining_length))
    )
    
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

num_passwords = 5
name = input("Enter your name: ")

passwords = [generate_password(name) for _ in range(num_passwords)]

print("Generated Passwords:")
for idx, password in enumerate(passwords, start=1):
    print(f"Password {idx}: {password}")
