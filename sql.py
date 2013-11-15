# Setting up SQL/Python relationship--creating table for contacts (don't repeat creation?)
import sqlite3
conn = sqlite3.connect('contactdatabase.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS contacts 
				(UniqueID integer primary key autoincrement, firstName, lastName, phoneNumber)''')

c.execute("SELECT COUNT(UniqueID) FROM contacts")
result=c.fetchone()

num_of_rows=result[0]

conn.commit()

print "Welcome to Jay's Contact list. You currently have %d contacts.\nPress 'help' to view all contacts." %num_of_rows

input = raw_input(">")


if input == "view":
	ID = raw_input("Which contact would you like to view? (Search by Unique ID)")
	query = "SELECT * FROM contacts WHERE UniqueID=?"
	c.execute(query, ID)
	results = c.fetchone()
	print "First Name:" + results[1] + "\nLast Name:" + results[2] + "\nPhone Number:" + results[3]