import random

def password_length():
    passlen = int(input("Enter your Desired Length for Your Password: "))
    return passlen
#I KNOW ITS USELESS BUT ITS FANCY
def password_type():
    print('Please Choose from below options:')
    print('1. Lowercase')
    print('2. Uppercase')
    print('3. Numbers')
    print('4. Special Characters')
    print('5. Multiple Types (Combine)')
    
    choices_str = input().split()
    choices = []
    
    for choice_str in choices_str:
        try:
            choice = int(choice_str)
            if choice not in [1, 2, 3, 4, 5]:
                print("Invalid Input!!!")
                return None
            choices.append(choice)
        except ValueError:
            print("Invalid Input!!!")
            return None
    
    return choices


def generating_password():
    length = password_length()
    type_choices = []
    print(f"Generating a {length}-character password with multiple types......")

    while True:
        print('Please Choose from below options:')
        print('1. Lowercase')
        print('2. Uppercase')
        print('3. Numbers')
        print('4. Special Characters')
        print('5. Done (Generate Password)')
        print('6. All in One')
        choice = int(input())
        
        if choice == 6:
            type_choices.extend([1, 2, 3, 4])
            break
        elif choice == 5:
            if not type_choices:
                print("No types selected. Please select at least one type.")
            else:
                break
        elif choice in [1, 2, 3, 4]:
            type_choices.append(choice)
        else:
            print("Invalid Input!!!")

    password = ''
    lowercase_chars = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number_chars = '0123456789'
    special_characters = '!@#$%^&*()-=_+~`[]{}<>?,./'
    
    for choice in type_choices:
        if choice == 1:
            password += random.choice(lowercase_chars)
        elif choice == 2:
            password += random.choice(uppercase_chars)
        elif choice == 3:
            password += random.choice(number_chars)
        elif choice == 4:
            password += random.choice(special_characters)
    
    remaining_length = length - len(password)
    
    if remaining_length > 0:
        available_choices = ''
        if 1 in type_choices:
            available_choices += lowercase_chars
        if 2 in type_choices:
            available_choices += uppercase_chars
        if 3 in type_choices:
            available_choices += number_chars
        if 4 in type_choices:
            available_choices += special_characters
        
        password += ''.join(random.choice(available_choices) for _ in range(remaining_length))
    
    password_list = list(password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)
    print("-----------------------------------------------------------------------")
    print()
    print("Generated Password:", final_password)
    print()
    print("-----------------------------------------------------------------------")




def main():
    while True:
        
        print("██╗░░░██╗███████╗░██████╗░░█████╗░░██████╗  ██████╗░░██╗░░░░░░░██╗░██████╗  ░██████╗░███████╗███╗░░██╗")
        print("██║░░░██║██╔════╝██╔════╝░██╔══██╗██╔════╝  ██╔══██╗░██║░░██╗░░██║██╔════╝  ██╔════╝░██╔════╝████╗░██║")
        print("╚██╗░██╔╝█████╗░░██║░░██╗░███████║╚█████╗░  ██████╔╝░╚██╗████╗██╔╝╚█████╗░  ██║░░██╗░█████╗░░██╔██╗██║")
        print("░╚████╔╝░██╔══╝░░██║░░╚██╗██╔══██║░╚═══██╗  ██╔═══╝░░░████╔═████║░░╚═══██╗  ██║░░╚██╗██╔══╝░░██║╚████║")
        print("░░╚██╔╝░░███████╗╚██████╔╝██║░░██║██████╔╝  ██║░░░░░░░╚██╔╝░╚██╔╝░██████╔╝  ╚██████╔╝███████╗██║░╚███║")
        print("░░░╚═╝░░░╚══════╝░╚═════╝░╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝")
        print("Choose From Below Options:\n")
        print("1. Create A New Password.")
        print("2. Exit Program.")
        print("Your Choice is : ")
        ch = int(input())
        try:
            if ch not in [1, 2]:
                raise ValueError
            elif ch == 1:
                generating_password()
            else:
                exit()
        except Exception as e:
            print(e, "\n", end="")

if __name__ == "__main__":
    main()
