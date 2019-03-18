import mysql.connector as my
conn = my.connect(user='root', password='', host='localhost')
sql = conn.cursor()

sql.execute("create database if not exists inventory;")
sql.execute("use inventory;")
# sql.execute("create table items(P_Id int not null, P_Name varchar(20) not null, P_Quantity int not null, P_Price int not null);")
sql.execute("insert into items values(1, 'Pencil', 5, 3);")
sql.execute("insert into items values(2, 'Eraser', 3, 5);")
sql.execute("insert into items values(3, 'Sharper', 1, 4);")
conn.commit()
# sql.execute("insert into items values('debugger', 6645);")
sql.execute("select * from items;")

print(sql.fetchall())
