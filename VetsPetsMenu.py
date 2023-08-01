from Vet_db_pet import Pet
from Vet_db import Customer
from DBHelper_class import DBHelper
from tabulate import tabulate
def pets_menu():
    db = DBHelper()
    message = """
    << Pets Menu >>
    1. Add Pet
    2: Update Pet
    3: Delete Pets
    4: View All Pets
    5: View Customer Pets
    0: Quit
    """
    print(message)
    choice = int(input("Enter Your Choice:"))

    pet = Pet()
    customer = Customer()

    while True:
        if choice == 1:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            pet.cid = customer.cid

            # pet.cid = rows[0][0]

            pet.read_pet_data()
            print(vars(pet))

            sql = pet.get_insert_sql_query()
            db.execute_sql(sql)
            print("Pet Added Successfully....")


        elif choice == 2:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pet_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREAD', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            pet_fetched = rows[0]
            pet.pid = int(input("Enter Ped PID: "))

            pet.name = input("Enter Pet Name: ")
            if len(pet.name) == 0:
                pet.name = pet_fetched[1]

            # pet.age = pet_fetched[2]
            # print("oldage: ", pet.age)
            pet.age = int(input("Enter Pet Age: "))
            if pet.age == 0:
                pet.age = pet_fetched[2]
            else:
                pet.age = int(pet.age)

            pet.weight = int(input("Enter Pet Weight: "))
            if pet.weight == 0:
                pet.weight = pet_fetched[3]

            pet.breed = input("Enter Pet Breed: ")
            if len(pet.breed) == 0:
                pet.breed = pet_fetched[4]

            pet.gender = input("Enter Pet Gender: ")
            if len(pet.gender) == 0:
                pet.gender = pet_fetched[5]

            sql = pet.get_update_sql_query()
            print(sql)
            db.execute_sql(sql)
            print("Pet Updated...")

        elif choice == 3:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            #sql = pet.get_pet_sql_query(cid)

            sql = pet.get_pet_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREAD', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            pet.pid = int(input("Enter Ped PID: "))
            delete_choice = input("Are Your Sure to Delete ? (yes/no): ")

            if delete_choice == "yes":
                sql = pet.get_delete_sql_query()
                db.execute_sql(sql)
                print("Pet Deleted...")

        elif choice == 4:
            sql = pet.get_pet_sql_query()
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'AGE', 'WEIGHT', 'BREED', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 5:
            phone = input("Enter Customer Phone: ")
            sql = customer.get_customers_sql_query(phone)
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'PHONE', 'EMAIL', 'AGE', 'GENDER', 'ADDRESS', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            customer_fetched = rows[0]
            customer.cid = customer_fetched[0]

            sql = pet.get_pet_sql_query(cid=str(customer.cid))
            rows = db.execute_select_sql(sql)
            columns = ['CID', 'NAME', 'AGE', 'WEIGHT', 'BREAD', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))


        elif choice == 0:
            break
        else:
            print("Invalid Choice")
        print(message)
        choice = int(input("Enter Your Choice:"))