import string, random

def generate_password(min_length, numbers=True, special_characters=True):

    # Get all available  letters, digits. and special characters
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #Create password pool based on criteria
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    #Initialize empty password and criteria
    pwd = ""

    #Append random characters from the pool together to form password
    while True:
        pwd = ''.join(random.choice(characters) for _ in range(min_length))
        if (not numbers or any(char.isdigit() for char in pwd)) and \
           (not special_characters or any(char in string.punctuation for char in pwd)):
            return pwd

#Ask user to input minimum length, specify criteria
while True:
    try:
        minimum = int(input("What's the minimum length?: "))
        break
    except ValueError:
        print("Please enter a valid integer for the minimum length.")

while True:
    has_number_input = input("Do you want to have numbers (y/n)? ").lower()
    if has_number_input == "y" or has_number_input == "n":
        has_number = has_number_input == "y"
        break
    else:
        print("Please enter 'y' for yes or 'n' for no.")

while True:
    has_special_input = input("Do you want to have special characters (y/n)? ").lower()
    if has_special_input == "y" or has_special_input == "n":
        has_special = has_special_input == "y"
        break
    else:
        print("Please enter 'y' for yes or 'n' for no.")

#Generate password and save to this variable
new_password = generate_password(minimum, has_number, has_special)

#Display password on CLI
print("Generated Password: ", new_password)
