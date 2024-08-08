
import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 4:
                print("Password length should be at least 4 characters.")
                continue
            password = generate_password(length)
            print(f"Generated password: {password}")
            break
        except ValueError:
            print("Invalid input, please enter a numerical value.")

if __name__ == "__main__":
    main()