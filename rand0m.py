#!/usr/bin/env python3
import random 
import string

chars = string.ascii_letters + string.digits + '!@#$%^&()_+:"><,./}[{'

menu_options = {
    1: 'Random Password Generator',
    2: 'Random Number Generator',
    3: 'Exit',
}

def print_menu():
    banner = '''

  _   _ _______ ______ _____  __ ___  
 | \ | |__   __|  ____|  __ \/_ |__ \ 
 |  \| |  | |  | |__  | |__) || |  ) |
 | . ` |  | |  |  __| |  ___/ | | / / 
 | |\  |  | |  | |____| |     | |/ /_ 
 |_| \_|  |_|  |______|_|     |_|____|  
 
'''
    print(banner)
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

def random_pass():
    chars = string.ascii_letters + string.digits + '!@#$%^&()_+:"><,./}[{'
    length = int(input('What length do you want the password?: '))
    password = ''
    for i in range(length):
        password += random.choice(chars)
    print(password)

def random_number():
    times = int(input('How many times do you want to print random numbers?: '))

    for i in range(times):
        number = random.randint(0,9999999)
        print(number)


if __name__ == '__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
             print('Wrong input. Please enter a number.')
        if option == 1:
            random_pass()
        elif option == 2:
            random_number()
        elif option == 3:
            print('Thanks for using my program')
        exit()