# Setting up SQL/Python relationship--creating table for contacts (don't repeat creation?)
import sqlite3
conn = sqlite3.connect('contactdatabase.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS contacts 
				(UniqueID integer primary key autoincrement, firstName, lastName, phoneNumber)''')


c.execute("SELECT COUNT(UniqueID) FROM contacts")
result=c.fetchone()

number_of_rows=result[0]

conn.commit()

print "Welcome to Jay's Contact list. You currently have %d contacts.\nPress 'help' to view all contacts." %number_of_rows

input = raw_input(">")

if input == "help":
	print '''
	Create - Create new contact
	View - View contacts
	Update - Update contact
	Delete - Delete contact
	Exit - Exit Program
	'''
elif input == "create":
	import re
	
	FirstName = raw_input("> First Name: ")
	if not re.match("^[a-z]*$", FirstName):
		print "ERROR: Only letters a-z allowed!"
		
	elif len(FirstName) > 40:
		print "ERROR: Only 40 characters allowed!"
		
	
	LastName = raw_input("> Last Name: ")
	if not re.match("^[a-z]*$", LastName):
		print "ERROR: Only letters a-z allowed!"
		
	elif len(LastName) > 40:
		print "ERROR: Only 40 characters allowed!"
		
	
	PhoneNumber = raw_input("> Phone Number: ")
	if not re.match("^[0-9]*$", PhoneNumber):
		print "ERROR: Only numbers 0-9 can be used to complete this field!"
	elif len(PhoneNumber) > 10:
		print "ERROR: Only 10 characters allowed!"

	contact = ('FirstName', 'LastName', 'PhoneNumber')
	
	c.execute("INSERT INTO contacts (firstName, lastName, phoneNumber) VALUES (?, ?, ?)", contact)
	conn.commit()

if input == "view":
	ID = raw_input("Which contact would you like to view? (Search by Unique ID)")
	query = "SELECT * FROM contacts WHERE UniqueID=?"
	c.execute(query, ID)
	results = c.fetchone()
	print "First Name:" + results[1] + "\nLast Name:" + results[2] + "\nPhone Number:" + results[3]


elif input == "update":
	import re

	update = raw_input("Which contact would you like to update? (Updaye by Unique ID)")
	
	FirstName = raw_input("> Updated First Name: ")
	if not re.match("^[a-z]*$", FirstName):
		print "ERROR: Only letters a-z allowed!"
		
	elif len(FirstName) > 40:
		print "ERROR: Only 40 characters allowed!"
	updated = (FirstName, update)
	c.execute("UPDATE contacts SET firstName=? WHERE UniqueID=?", updated) 
	conn.commit()

	LastName = raw_input("> Updated Last Name: ")
	if not re.match("^[a-z]*$", LastName):
		print "ERROR: Only letters a-z allowed!"
		
	elif len(LastName) > 40:
		print "ERROR: Only 40 characters allowed!"
	updated = (LastName, update)
	c.execute("UPDATE contacts SET lastName=? WHERE UniqueID=?", updated) 
	conn.commit()

	PhoneNumber = raw_input("> Updated Phone Number: ")
	if not re.match("^[0-9]*$", PhoneNumber):
		print "ERROR: Only numbers 0-9 can be used to complete this field!"
	
	elif len(PhoneNumber) > 10:
		print "ERROR: Only 10 characters allowed!"
	updated = (PhoneNumber, update)
	c.execute("UPDATE contacts SET phoneNumber=? WHERE UniqueID=?", updated) 
	conn.commit()

elif input == "delete":
	Answer = raw_input("Are you sure you wish to delete contact? ")

	if Answer == "yes":
		delete = raw_input("Which contact would you like to delete? (Delete by Unique ID)")
		query = "DELETE FROM contacts WHERE UniqueID=?"
		c.execute(query, delete)
		conn.commit()
