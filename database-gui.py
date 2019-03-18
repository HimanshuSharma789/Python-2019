from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

import mysql.connector as my


class Application(QWidget):
	def __init__(self):
		super().__init__()

		self.conn = my.connect(user='root', password='', host='localhost')
		self.sql = self.conn.cursor()

		self.sql.execute("create database if not exists inventory;")
		self.sql.execute("use inventory;")
		self.sql.execute("create table if not exists items(P_Id int not null, P_Name varchar(20) not null, P_Quantity int not null, P_Price int not null);")

		self.setGeometry(200,200,500,500)
		self.setWindowTitle("Database GUI")
		self.gui()

	def gui(self):
		mainlayout = QVBoxLayout()
		mainlayout.addStretch(0)
		mainlabel = QLabel()
		mainlabel.setText("Database")

		self.table = QTableWidget()
		# self.table.setRowCount(4)
		self.table.setColumnCount(4)
		self.col = ['Id', 'name', 'quantity', 'price']
		self.table.setHorizontalHeaderLabels(self.col)
		self.display()

		# insert table1
		id_label = QLabel()
		id_label.setText("Product Id: ")
		self.id_textbox = QLineEdit()
		name_label = QLabel()
		name_label.setText("Product Name: ")
		self.name_textbox = QLineEdit()
		quantity_label = QLabel()
		quantity_label.setText("Product Quantity: ")
		self.quantity_textbox = QLineEdit()
		price_label = QLabel()
		price_label.setText("Product Price: ")
		self.price_textbox = QLineEdit()
		self.insert_button = QPushButton("Insert")
		self.insert_button.clicked.connect(self.insert)
			

		mainlayout.addWidget(id_label)
		mainlayout.addWidget(self.id_textbox)
		mainlayout.addWidget(name_label)
		mainlayout.addWidget(self.name_textbox)
		mainlayout.addWidget(quantity_label)
		mainlayout.addWidget(self.quantity_textbox)
		mainlayout.addWidget(price_label)
		mainlayout.addWidget(self.price_textbox)
		mainlayout.addWidget(self.insert_button)

		
		# update table 2
		id_label1 = QLabel()
		id_label1.setText("ID: ")
		self.id_textbox1 = QLineEdit()
		choose_label = QLabel()
		choose_label.setText("Choose: ")
		self.col_combobox = QComboBox()
		self.col_combobox.addItems(['P_Name', 'P_Quantity', 'P_Price'])
		self.col_textbox = QLineEdit()
		update_button = QPushButton()
		update_button.clicked.connect(self.update)

		mainlayout.addWidget(id_label1)
		mainlayout.addWidget(self.id_textbox1)
		mainlayout.addWidget(choose_label)
		mainlayout.addWidget(self.col_combobox)
		mainlayout.addWidget(self.col_textbox)
		mainlayout.addWidget(update_button)



		mainlayout.addWidget(mainlabel)
		mainlayout.addWidget(self.table)
		
		button = QPushButton()
		mainlayout.addWidget(button)
		self.setLayout(mainlayout)

	
	# display table 0
	def display(self):
		self.sql.execute("select * from items;")
		fetch = self.sql.fetchall()
		print(fetch)
		self.table.setRowCount(0)
		for i,row in enumerate(fetch,0):
			self.table.insertRow(i)
			for j,column in enumerate(row,0):
				self.table.setItem(i,j, QTableWidgetItem(str(column)))

	
	def insert(self):
		# self.sql.execute("insert into items values("+self.id_textbox.text()+","+self.name_textbox.text()+","+self.quantity_textbox.text()+","+self.price_textbox.text()+");")
		self.sql.execute("insert into items values(%s,%s,%s,%s);",(self.id_textbox.text(),self.name_textbox.text(),self.quantity_textbox.text(),self.price_textbox.text()))
		self.conn.commit()
		self.display()
		print("successful")

	
	def update(self):
		s="""update items set %s = %s where p_id = %s;""" %(self.col_combobox.currentText(),self.col_textbox.text(),self.id_textbox1.text())
		self.sql.execute(s)
		self.conn.commit()
		print("successful")
		# print("""update items set %s = %s where p_id = %s;""",(self.col_combobox.currentText(),self.col_textbox.text(),self.id_textbox1.text()))
		# self.sql.execute("insert into items values("+self.id_textbox.text()+","+self.name_textbox.text()+","+self.quantity_textbox.text()+","+self.price_textbox.text()+");")
		# self.sql.execute("""update items set %s = %s where p_id = %s;""",(str(self.col_combobox.currentText()),self.col_textbox.text(),self.id_textbox1.text()))



if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Application()
	window.show()
	sys.exit(app.exec_())

