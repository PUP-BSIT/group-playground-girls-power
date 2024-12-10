import os

def info():
    print("Name: Loise Nicole")
    print("Year: 2nd Year")
    print("Program: Diploma in Information Technology")

def goals():
    print("Goal #1: To graduate")

def loise_info():
    while True:
        print("---Loise Menu---")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from Teamates")
        print("4. Comment from Teamates")
        print("5. Comment from Teamates")
        print("6. Comment from Teamates")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 7:
            break

        match choice:
            case 1:
                os.system('cls')
                print("----Basic Info----")

                info()

                input("\nPress Enter to continue...")

            case 2:
                os.system('cls')
                print("----Goals----")

                goals()

                input("\nPress Enter to continue...")

            case 3:
                os.system('cls')
                print("----Comment from teamate----")
                print(" ")

            case 4:
                os.system('cls')
                print("----Comment from teamate----")
                print(" ")

            case 5:
                os.system('cls')
                print("----Comment from teamate----")
                print(" ")

            case 6:
                os.system('cls')
                print("----Comment from teamate----")
                print(" ")

