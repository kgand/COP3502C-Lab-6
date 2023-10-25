#Kovidh Gandreti

def encode(password):
  encoded = ""
  for i in range(len(password)):
    encoded += str(int(password[i]) + 3)
  return encoded

def decode(password):
    encoded_password = ""
    for i in password:
        i = int(i)
        i = i - 3
        i = str(i)
        encoded_password = encoded_password + i
    encoded_list = str(encoded_password)
    print(encoded_list)

def main():
    while True:
        option = int(input(f"Menu\n{'-' * 13}\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            if password:
                print(f"The encoded password is {encoded}, and the original password is {password}.")
            else:
                password = input("Please enter your password to decode: ")
                decoded = decode(password)
                print(f"The encoded password is {password}, and the original password is {decoded}.")
        elif option == 3:
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == '__main__':
    main()
