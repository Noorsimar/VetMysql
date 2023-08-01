import datetime

"""
    create table Consultation(
        cnid int primary key auto_increment,
        cid int,
        pid int,
        problem text,
        heartrate int,
        temperature float,
        medicines text,
        createdon datetime,
        FOREIGN KEY (cid) REFERENCES Customer(cid),
        FOREIGN KEY (pid) REFERENCES Pet(pid)
        );

"""
class Consultation:
    def __init__(self):
        self.cnid = 0
        self.cid = 0
        self.pid = 0
        self.problem = ""
        self.heartrate = 0
        self.temperature = 98.4
        self.medicines = ""
        self.createdon = ""

    def read_consultation_data(self):
        self.problem = input("Enter Pet Problem: ")
        self.heartrate = int(input("Enter Heartrate: "))
        self.temperature = float(input("Enter Pet Temprature: "))
        self.medicines = input("Enter Pet Medicines: ")
        #self.gender = input("Enter Pet Gender (male/female): ").lower()

        # Get the date and time
        self.createdon = str(datetime.datetime.today())
        # Eliminate Milli Seconds
        self.createdon = self.createdon[: self.createdon.rindex(".")]

    def get_insert_sql_query(self):
        sql = "insert into Consultation values(null, {cid}, {pid}, '{problem}', " \
              "{heartrate}, {temperature}, '{medicines}', '{createdon}')".format_map(vars(self))
        return sql


    def get_consultation_sql_query(self, cid="", pid=""):
        sql = "select * from Consultation"

        if len(cid) != 0:
            sql = "select * from Consultation where cid = {}".format(cid)
        if len(pid) != 0:
            sql = "select * from Consultation where pid = {}".format(pid)

        return sql

    def get_delete_sql_query(self):
        sql = "delete from Customer where cid = {}".format(self.cid)
        return sql

    def get_update_sql_query(self):
        sql = "update Consultation set problem='{problem}', heartrate={heartrate}, temperature={temperature}, medicines='{medicines}' " \
              "where cnid = {cnid}".format_map(vars(self))
        return sql