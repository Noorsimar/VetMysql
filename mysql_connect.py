import mysql.connector as db

class Customer:
    def __init__(self):
        self.name=input("Customer Name:")
        self.phone=input("Customer Phone:")
        self.email=input("Customer Email:")

def main():
    customer1 = Customer()
    print(vars(customer1))
    connection = db.connect(user='root', password='rootroot', host='127.0.0.1', database='groundwork')
    cursor = connection.cursor()
    sql = "insert into Customer values(null, '{name}', '{phone}', '{email}');".format_map(vars(customer1))
    cursor.execute(sql)
    connection.commit()

    print("Customer Inserted...")


if __name__ == "__main__":
    main()