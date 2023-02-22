from os import system, name

def clear_screen():
    # for windows, mac or linux
    if name == 'nt':
        system('cls')
    else:
        system('clear')