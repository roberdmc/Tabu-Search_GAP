from tkinter import filedialog
from Clear_screen import clear_screen

def header():
    print("\n---------------------------------------------------------------------------")
    print("\n   ---------------------------------------------------------------------")
    print("   ---------------------------- Tabu Search ----------------------------")
    print("   ----------------- Generalized Assignment Problem --------------------")
    print("   ---------------------------------------------------------------------\n")
    print("---------------------------------------------------------------------------\n")

def type_menu():
    header()
    print("Default values:")
    print('\tMax iterations: 100')
    print('\tTabu size: \t10')
    print('\tP: \t\t1.3')
    print('\tVerbose: \tTrue')
    print('\tInput: \t\tFiles in folder "Input_files"')
    print()
    print("Use default values?")
    print('\t0 -> No')
    print('\t1 -> Yes')
    print()
    option = '2'
    while option not in ['0','1']:
        option = input("Type 0 or 1: ")
        print()
        if option=='1':
            default_values = True
        elif option == '0':
            default_values = False
        else:
            print("Invalid option.")
            print()
    return default_values

def menu():
    print("Select the input file:")
    file_name = filedialog.askopenfilename()

    print()
    print("Verbose outputs?")
    print('\t0 -> No')
    print('\t1 -> Yes')
    print()
    option = '2'
    while option not in ['0','1']:
        option = input("Type 0 or 1: ")
        print()
        if option=='1':
            verbose = True
        elif option=='0':
            verbose = False
        else:
            print("Invalid option.")
            print()

    option = '2'
    while option == '2':
        try:
            max_iter = int(input("Enter the max iterations: "))
            option = '1'
        except:
            print()
            print("Invalid input.")

    option = '2'
    while option == '2':
        try:
            print()
            tabu_size = int(input("Enter the tabu size: "))
            option = '1'
        except:
            print()
            print("Invalid input.")

    option = '2'
    while option == '2':
        try:
            print()
            P = float(input("Enter the P value: "))
            option = '1'
        except:
            print()
            print("Invalid input.")

    return file_name, max_iter, tabu_size, P, verbose

def menu_default():
    print("Select the input file:")
    print('\t1 -> PDG1.txt')
    print('\t2 -> PDG2.txt')
    print('\t3 -> PDG3.txt')
    print('\t4 -> PDG4.txt')

    option = '0'

    while(option not in ['1','2','3','4']):
        print()
        option = input("Type 1, 2, 3 or 4: ")
        if option=='1':
            file_name = "Input_files\\PDG1.txt"
        elif option=='2':
            file_name = "Input_files\\PDG2.txt"
        elif option=='3':
            file_name = "Input_files\\PDG3.txt"
        elif option=='4':
            file_name = "Input_files\\PDG4.txt"
        else:
            print()
            print("Invalid option.")

    return file_name

def rerun():
    print()
    print("Run the program again?")
    print('\t0 -> No')
    print('\t1 -> Yes')
    option = '2'
    while option not in ['0','1']:
        print()
        option = input("Type 0 or 1: ")
        print()
        if option=='1':
            run = True
            clear_screen()
        elif option=='0':
            run = False
        else:
            print("Invalid option.")
            print()

    return run