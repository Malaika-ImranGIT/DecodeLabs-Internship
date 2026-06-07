import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    
    password = ""
    for _ in range(length):
        password += random.choice(characters)
        
    return password

def run_password_engine():
    print("--- PASSWORD GENERATOR ---")
    
    while True:
        user_input = input("Enter password length (or 'quit'): ").strip()
        
        if user_input.lower() == 'quit':
            break
            
        try:
            length = int(user_input)
            
            if length <= 0:
                print("Length must be greater than 0.")
                continue
                
            password = generate_password(length)
            print(f"Generated Password: {password}\n")
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    run_password_engine()