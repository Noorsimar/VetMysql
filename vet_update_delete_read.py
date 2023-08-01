import mysql.connector as db



def main():
    sql1 = "update Customer set name = 'John Watson', age = 26 where cid = 1"
    sql2 = "delete from Customer where cid = 2"
    sql3 = "select * from Customer"

    connection = db.connect(user='root',
                            password='rootroot',
                            host='127.0.0.1',
                            database='groundwork')

    cursor = connection.cursor()

    cursor.execute(sql3)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()