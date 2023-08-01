from Vet_db_pet import Pet
from Vet_db import Customer
from VetConsultationClass import Consultation
from DBHelper_class import DBHelper
from tabulate import tabulate

def consultation_menu():

    db = DBHelper()
    message = """
    << Consultation Menu >>
    1. Add Consultation
    2: Update Consultation
    3: View ALl Consultation
    4: View Customer by Date
    5: View Customer Pets Consultation
    0: Quit
    """
    print(message)
    choice = int(input("Enter Your Choice:"))
    customer = Customer()
    pet = Pet()
    consultation = Consultation()

    while True:
        if choice == 1:
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

            if len(rows) == 0:
                print("Please Add Pet First...")
                break
            if len(rows) == 1:
                pet.pid = rows[0][0]
            else:
                pet.pid = int(input("Enter Pet ID: "))

            consultation.cid = customer.cid
            consultation.pid = pet.pid

            consultation.read_consultation_data()

            sql = consultation.get_insert_sql_query()
            db.execute_sql(sql)

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

            sql = consultation.get_consultation_sql_query()
            rows = db.execute_select_sql(sql)

            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMPRATURE', 'MEDICINES', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))
            consultation_fetched = rows[0]

            #pet.pid = int(input("Enter Ped PID: "))


            if len(rows) == 0:
                print("Please Add Consultation First...")
                break
            if len(rows) == 1:
                consultation.cnid = rows[0][0]
            else:
                consultation.cnid = int(input("Enter Consulataion CNID: "))

            consultation.cid = customer.cid
            consultation.pid = pet.pid
            consultation.cnid = consultation.cnid


            consultation.problem = input("Enter Updated Problem Name: ")
            if len(consultation.problem) == 0:
                consultation.problem = consultation_fetched[3]

            consultation.heartrate = input("Enter Updated HeartRate: ")
            if len(consultation.heartrate) == 0:
                consultation.heartrate = consultation_fetched[4]
            else:
                consultation.heartrate = int(consultation.heartrate)

            consultation.temperature = input("Enter Updated Temp: ")
            if len(consultation.temperature) == 0:
                consultation.temperature = consultation_fetched[5]
            else:
                consultation.temperature = float(consultation.temperature)


            consultation.medicines = input("Enter Updated Pet Medicines: ")
            if len(consultation.medicines) == 0:
                consultation.medicines = consultation_fetched[6]


            sql = consultation.get_update_sql_query()
            print(sql)
            db.execute_sql(sql)
            print("Consultation Updated...")


        elif choice == 3:
            sql = consultation.get_consultation_sql_query()
            rows = db.execute_select_sql(sql)

            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMPRATURE', 'MEDICINES', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 4:
            pass
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
            columns = ['PID', 'NAME', 'AGE', 'WEIGHT', 'BREAD', 'GENDER', 'CID', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

            sql = consultation.get_consultation_sql_query(cid=int(customer.cid))
            rows = db.execute_select_sql(sql)

            columns = ['CNID', 'CID', 'PID', 'PROBLEM', 'HEARTRATE', 'TEMPRATURE', 'MEDICINES', 'CREATEDON']
            print(tabulate(rows, headers=columns, tablefmt="grid"))

        elif choice == 0:
            break
        else:
            print("Invalid Choice")

        print(message)
        choice = int(input("Enter Your Choice:"))