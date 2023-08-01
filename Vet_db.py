import datetime
#import mysql.connector as db
#from DBHelper_class import DBHelper

class Customer:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.email = ""
        self.age = 0
        self.gender = ""
        self.address = ""
        self.createdon = ""
    def read_customer_data(self):
        self.name=input("Customer Name:").lower()
        self.phone=input("Customer Phone:")
        self.email=input("Customer Email:").lower()
        self.age = int(input("Customer Age:"))
        self.gender = input("Customer Gender(male/female):").lower()
        self.address = input("Customer Address:").lower()
        self.createdon = str(datetime.datetime.today())
        self.createdon = self.createdon[:self.createdon.rindex(".")]

    def get_insert_sql_query(self):
        sql = "insert into Customer values(null, '{name}', '{phone}', '{email}', " \
              "{age}, '{gender}', '{address}', '{createdon}')".format_map(vars(self))
        return sql
    def get_update_sql_query(self, cid):
        self.cid = cid
        sql = "UPDATE Customer SET name='{name}', phone='{phone}', email='{email}', " \
              "age={age}, gender='{gender}', address='{address}', createdon='{createdon}' " \
              "WHERE cid={cid}".format_map(vars(self))
        return sql

    def get_customers_sql_query(self, phone=""):
        if len(phone) == 0:
            sql = "select * from Customer"
        else:
            sql = "select * from Customer where phone = '{}'".format(phone)
        return sql

    def get_delete_sql_query(self):
        sql = "delete from Customer where cid = {}".format(self.cid)
        return sql

def main():
    # customer = Customer()
    # customer.read_customer_data()
    # print(vars(customer))
    #
    # connection = DBHelper()
    #
    # sql = customer.insert_sql()
    # connection.execute_sql(sql)


    # connection = db.connect(user='root', password='rootroot', host='127.0.0.1', database='groundwork')
    # cursor = connection.cursor()
    # sql = customer.insert_sql()
    # cursor.execute(sql)
    # connection.commit()

    print("Customer Inserted...")

if __name__ == "__main__":
    main()

    """
    create database database_name;
    create table Customer(cid int primary key auto_increment, name text, phone text, email text, age int, gender text, address text, createdon datetime);
    """