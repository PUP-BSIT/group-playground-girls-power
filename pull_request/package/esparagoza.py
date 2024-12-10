import os
             
def information():
    print('Name: Mikka Kette P. Esparagoza')
    print('Birthday: November 12, 2004')
    print('Age: 20')
    print()

def goals():
    print('Goal #1: To finish studies')
    print('Goal #2: To be financially stable')
    print('Goal #3: To visit Japan')
    print()

def esparagoza_menu():
    while True:
        os.system('cls')
        print('---Good Day, Mikka Kette P. Esparagoza!---')
        print('[1] Basic Informations')
        print('[2] Goals')
        print('[3] Comment from Alejandro')
        print('[4] Comment from De Leon')
        print('[5] Comment from Gomez')
        print('[6] Comment from Mosenos')
        print('[0] Exit Program')
        choice = int(input("Enter your choice: "))
        print()

        if choice == 0:
            break

        match choice:

            case 1:
                os.system('cls')
                print('Basic Information')

                information()

                input('Press Enter to Continue')
                print()

            case 2:
                os.system('cls')
                print('Goals')
                goals()

                input('Press Enter to Continue')
                print()
            
            case 3:
                os.system('cls')
                print('Comment from Alejandro:')
                print()

                input('Press Enter to Continue')
                print()

            case 4:
                os.system('cls')
                print('Comment from De Leon:')
                print()

                input('Press Enter to Continue')
                print()

            case 5:
                os.system('cls')
                print('Comments from Gomez:')
                print()

                input('Press Enter to Continue')
                print()
            
            case 6:
                os.system('cls')
                print('Comments from Mosenos:')
                print()

                input('Press Enter to Continue')
                print()

            case _:           
                print('Invalid Input Plese Try Again!')



