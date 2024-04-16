#######################################################################################
# Author: Waibhav Jha								
# Description: SafeBox is a secure repository designed to safeguard sensitive data,
#          including passwords, bank details, and important phone numbers.
# Design: Crafted with my own encryption algorithm, this program enables me to
#         protect my passwords according to my preferences. While it's primarily
#         tailored for personal use, feel free to explore it for your own needs.			
# Contact: For inquiries, reach out to me at: waibhavjha.contact@gmail.com						
#######################################################################################

from Encrypt import UniqueCipher

# Dictionary to store user data
users = {}

# Function to encrypt data
def encrypt_data(data, key):
    cipher = UniqueCipher(key)
    encrypted_data = cipher.encrypt(data)
    return encrypted_data

# Function to decrypt data
def decrypt_data(data, key):
    cipher = UniqueCipher(key)
    decrypted_data = cipher.decrypt(data)
    return decrypted_data

# Function to sign up
def signup():
    name = input("Enter your name: ")
    password = input("Set your password: ")
    key = int(input("Set your encryption key (an integer): "))  # Unique cipher key
    users[name] = {'password': password, 'key': key, 'data': ''}

# Function to login
def login():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    if name in users and users[name]['password'] == password:
        return name
    else:
        print("Invalid credentials.")
        return None

# Function to save data
def save_data(name):
    data = input("Enter your data to save: ")
    key = users[name]['key']
    encrypted_data = encrypt_data(data, key)
    users[name]['data'] = encrypted_data

# Function to reload saved data
def reload_data(name):
    if users[name]['data']:
        key = users[name]['key']
        decrypted_data = decrypt_data(users[name]['data'], key)
        print("Your saved data:", decrypted_data)
    else:
        print("No data saved yet.")

# Main program
while True:
    print("\nWelcome to SafeBox!")
    print("\n1. Login\n2. Sign up\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        user = login()
        if user:
            while True:
                print("\n1. Save Data\n2. Reload Data\n3. Logout")
                user_choice = input("Enter your choice: ")
                if user_choice == '1':
                    save_data(user)
                elif user_choice == '2':
                    reload_data(user)
                elif user_choice == '3':
                    break
                else:
                    print("Invalid choice.")
    elif choice == '2':
        signup()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice.")