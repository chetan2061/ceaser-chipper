def welcome():
    '''
    This function simply prints introduction to the program.
    '''
    print("Welcome to the Caesar Cipher", )
    print("This program encrypts and decrypts text with the Caesar Cipher.", )

def enter_message():
    '''
    This function is used to take input from the user about the choice of operation to be done.
    It also handles all the possible errors from the user inputs and controls the flow of command.
    '''
    try:
        choice = input("Would you like to encrypt (e) or decrypt (d): ").upper()
        if (choice == "E"):
            location = message_or_file()
            if (location == "C"):
                message = input("What message would you like to encrypt: ")
                sift_value = int(input("What is the shift number: "))
                result = encrypt(message, sift_value)
                print("Encrypted message: ", result)
            elif (location == "F"):
                message = process_file()
                sift_value = int(input("What is the shift number: "))
                final = encrypt(message, sift_value)
                write_messages(final)

        elif (choice == "D"):
            print("Performing decryption.")
            location = message_or_file()
            if (location == "C"):
                message = input("What message would you like to decrypt: ")
                sift_value = int(input("What is the shift number: "))
                result = decrypt(message, sift_value)
                print("decrypted message", result)
            elif (location == "F"):
                message = process_file()
                sift_value = int(input("What is the shift number: "))
                result = decrypt(message, sift_value)
                write_messages(result)

        else:
            print("Invalid Mode ")
            enter_message()

    except ValueError as e:
        print(f"Invalid input: {e}")
        enter_message()


def encrypt(message, sift_value):
    '''
    this function actually encrypts the given text by converting the actual text into the list if ASCII values of the text,
     and adding the sift value to it each element and again converting into the characters. which are further joined together.

    '''
    mylist = list(message)
    finallist = []
    for i in mylist:
        n_conv = ord(i)
        encryption = n_conv + sift_value
        finallist.append(chr(encryption))
    encrypted_message = "".join(finallist)
    return encrypted_message


def decrypt(message, sift_value):
    '''
    this function decrypts the message by subtracting the sift_value from ASCII value of each elements.
    '''
    mylist = list(message)
    finallist = []
    for i in mylist:
        n_conv = ord(i)
        decryption = n_conv - sift_value
        finallist.append(chr(decryption))
    decrypted_message = "".join(finallist)
    return decrypted_message


def message_or_file():
    '''
    this file controls the flow of code by taking the user input on the file_choice.
    '''
    while True:
        file_choice = input("Would you like to read from a file (f) or the console (c)? ").upper()
        if file_choice in ["F", "C"]:
            return file_choice
        else:
            print("Invalid input! ")


def is_file():
    '''
    this function checks that the existence of file and returns the file name.
    '''
    while True:
        try:
            file_name = input("Enter a filename: ")
            with open(file_name, "r") as file:
                return file_name
        except FileNotFoundError:
            print("Invalid Filename: ")


def process_file():
    '''
    this function reads the file, whose name is provided by the user and return the content in the file.
    '''
    name = is_file()
    with open(name, "r") as file:
        text = file.read()
    return text


def write_messages(final):
    '''
    this function writes the given content in result to "result.txt" file.
    '''
    with open("results.txt", "w") as e_file:
        e_file.write(final)
    print("Output written to results.txt ", )

def main():
    '''make the exit if reprocessing of the program.'''
    welcome()
    enter_message()
    while True:
        again = input("Would you like to encrypt or decrypt another message? (y/n): ").upper()
        if (again == "N"):
            print("Thanks for using the program, goodbye!")
            break
        elif (again == "Y"):
            print("START DOING AGAIN.")
            enter_message()
        else:
            print("You must choose either yes or no")
main()

