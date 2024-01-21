 #import file from this pc
import os

# 1: Welcome the user to the Caesar Cipher program
def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")
   
# 2: Function to get the user's choice of mode and message to encrypt or decrypt
def enter_message():
    while True:
        crypt = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if crypt in ['e', 'd']:
            break
        else:
            print("Invalid crypt")

    message = input("What message would you like to encrypt or decript: ").upper()

    return crypt, message  # Return crypt and message as a tuple

# 3: Function to get the shift value from the user
def enter_shift():
    while True:
        try:
            shift = int(input("What is the shift number: "))
            break
        except ValueError:
            print("Invalid Shift")

    return shift

# 4: Function and formula to encrypt a message using the Caesar Cipher
def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
    
        if char.isalpha():
            shifted = ord(char) + shift
            if char.isupper():
                encrypted_message += chr((shifted - 65) % 26 + 65)
            else:
                encrypted_message += chr((shifted - 97) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message

# 5: Function to decrypt a message using the Caesar Cipher
def decrypt(message, shift):
    return encrypt(message, -shift)

# 6: Function to process messages from a file
def process_file(filename, crypt, shift):
    while not os.path.isfile(filename):
        print(f"Error: File '{filename}' not found.")
        filename = input("Enter the correct filename or type 'exit' to quit: ")
        if filename.lower() == 'exit':
            return []

    try:
        with open(filename, 'r') as file:
            messages = file.readlines()
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return []
    #according to users choice encript or decript text to the option given to user above from no.2
    processed_messages = []
    for message in messages:
        message = message.strip().upper()#strip remove the gap with in the text
        if crypt == 'e':
            processed_messages.append(encrypt(message, shift))
        elif crypt == 'd':
            processed_messages.append(decrypt(message, shift))
    return processed_messages

# 7: Function to write messages to a file
def write_messages(filename, messages):
    with open(filename, 'w') as file:
        for message in messages:
            file.write(message + '\n')

# 8: Function to check if a file exists
def is_file(filename):
    return os.path.isfile(filename)

# 9: Function to get user's choice of processing single message or a file
def message_or_file():
    while True:
        choice = input("Would you like to read from a file (f) or the console (c)?").lower()
        if choice in ['c', 'f']:
            return choice
        else:
            print("You can only choose 'c' or 'f'. 'c' to write text to convert or 'F' to take text from saved file.")

# 10: Simplified implementation of the main() function
def main():
    welcome()
#create a loop to run program again even after it ends and.
    while True:
        choice = message_or_file()

        if choice == 'c':
            # 10.1: If processing a single message, get crypt, message, and shift
            crypt, message = enter_message()
            shift = enter_shift()
            result = encrypt(message, shift) if crypt == 'e' else decrypt(message, shift)
            print(f'Result: {result}')
        else:
            # 10.2: If processing a file, get filename, crypt, and shift
            filename = input("Enter the filename (e.g., messages.txt): ")

            while not is_file(filename):
                print(f"Error: File '{filename}' not found.")
                filename = input("Enter the correct filename or type 'exit' to quit: ")
                if filename.lower() == 'exit':
                    return

            crypt = input("Would you like to encrypt (e) or decrypt (d): ").lower()
            shift = enter_shift()

            # 10.3: Process messages from the file
            encrypted_decrypted_messages = process_file(filename, crypt, shift)

            if encrypted_decrypted_messages:
                # 10.4: Display processed messages and ask if the user wants to save to a file
                print("\nProcessed Messages:")
                for idx, processed_message in enumerate(encrypted_decrypted_messages, 1):
                    print(f"{idx}. {processed_message}")

                save_choice = input("\nDo you want to save the processed messages to a file? (yes/no): ").lower()
                if save_choice == 'yes':
                    output_filename = input("Enter the output filename: ")
                    write_messages(output_filename, encrypted_decrypted_messages)
                    print(f"Processed messages saved to '{output_filename}'.")
        
        # 10.5: Ask the user if they want to encrypt or decrypt another message
        another_choice = input("\nWould you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_choice != 'y':
            print("Thanks for using the program, goodbye!")
            break

# 11: Run the main function if the script is executed
main()
