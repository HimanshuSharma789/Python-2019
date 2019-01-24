import mysql.connector as my
conn = my.connect(user='root', password='', host='localhost')
sql = conn.cursor()

sql.execute("create database testing_db;")
sql.execute("use testing_db;")
sql.execute("create table test(name varchar(20), phone int);")
sql.execute("insert into test values('tester', 9945);")
sql.execute("insert into test values('debugger', 6645);")
sql.execute("select * from test;")

print(sql.fetchall())
