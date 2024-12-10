def main_menu():
    while True:
        print("\n---Main Menu ---")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from De Leon")
        print("4. Comment from Esparagoza")
        print("5. Comment from Gomez")
        print("6. Comment from Mosenos")
        print("7. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            print (" Hi, I'm Aleck")               

        elif choice == '2':
            print (" ----") 

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
    main_menu()