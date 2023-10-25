#Kovidh Gandreti

def encode(password):
  encoded = ""
  for i in range(len(password)):
    encoded += str(int(password[i]) + 3)
  return encoded

def main():
    while True:
        option = int(input(f"Menu\n{'-' * 13}\n1. Encode\n2. Decode\n3. Quit\n\nPlease enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {encoded}, and the original password is {password}.")
        elif option == 3:
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == '__main__':
    main()