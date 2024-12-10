import os

def jasmine_info():
    while True:
        print("\n---Main Menu ---")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from Alejandro")
        print("4. Comment from Esparagoza")
        print("5. Comment from Gomez")
        print("6. Comment from Mosenos")
        print("7. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            print (" Hi, I'm De Leon")               

        elif choice == '2':
            print ("---Goals--") 
            print ("Have a motorcycle")

        elif choice == '3':
           print (" ----") 

        elif choice == '4':
            print (" ----")   

        elif choice == '5':
           print (" ----") 

        elif choice == '6':
           print (" ----") 
           
        elif choice == '7':
            print("\nExiting program.\n")
            break
        else:
            print("\nInvalid option. Please try again.\n")

# Run the main menu
if __name__ == "__main__":
    jasmine_info()