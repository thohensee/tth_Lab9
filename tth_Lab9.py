
# Tristan Hohensee - Lab 9 - Password Encode/Decode GitHub Practice

def printMenu():
    print("\nMenu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")

def encode(password):
    encoded = ""

    for i in range(len(password)):
        encoded += str(int(password[i]) + 3)

    return encoded

def decode(password):
    decoded = ""

    for i in range(len(password)):
        decoded += str(int(password[i]) + 3)

    return decoded

while True:
    printMenu()
    option = input("Please enter an option: ")

    match option:
        case "1":
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        case "2":
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")
        case "3":
            exit()
