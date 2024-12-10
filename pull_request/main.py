from package import alejandro, deleon, mosenos, esparagoza

def main_menu():
    while True:
        print("---Main Menu---")
        print("1. Aleck Mcklaiyre Alejandro")
        print("2. Jasmine Robelle De leon")
        print("3. Mikka Kette Esparagoza")
        print("4. Ashley Hermoine Gomez")
        print("5. Loise Nicole Mosenos")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("-----------------------------------")  
            alejandro.aleck_info()

        elif choice == '2':
            print("---  ---")
            deleon.jasmine_info()
            
        elif choice == '3':
            print("-----------------------------------")
            esparagoza.esparagoza_menu()

        elif choice == '4':
            print("-----------------------------------")

        elif choice == '5':
            print("-----------------------------------")   
            mosenos.loise_info() 
            
        elif choice == '6':
            print("\nExiting program.\n")
            break

        else:
            print("\nInvalid option. Please try again.\n")

# Run the main menu
if __name__ == "__main__":
    main_menu()