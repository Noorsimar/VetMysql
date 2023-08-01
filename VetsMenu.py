
from VetsPetsMenu import pets_menu
from VetsConsultMenu import consultation_menu
from VetsCustomerMenu import customer_menu
import datetime

def main_menu():
    message = """
    << Main Menu >>
    1. Manage Customer
    2: Manage Pets
    3: Manage Consultations
    0. Quit
    """
    print(message)
    choice = int(input("Enter Your Choice:"))

    while True:
        if choice == 1:
            customer_menu()
        elif choice == 2:
            pets_menu()
        elif choice == 3:
            consultation_menu()
        elif choice == 0:
            break
        else:
            print("Invalid Choice")

        print(message)
        choice = int(input("Enter Your Choice:"))


def main():
    date1 = datetime.datetime.today()

    welcome = """
    ~~~~~~~~~~~~~~~~~~~
    Welcome to Vets APP
    ~~~~~~~~~~~~~~~~~~~
    """
    print(welcome)

    main_menu()

    bye_message = """
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Thankyou for Using Vets APP
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~    
    """
    date2 = datetime.datetime.today()
    print("App Usage: ", date2-date1)

if __name__ == "__main__":
    main()