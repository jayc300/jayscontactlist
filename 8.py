import sqlite3
conn = sqlite3.connect('contactdatabase.db')

c = conn.cursor()

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
	
	c.execute('INSERT INTO contacts VALUES (?,?,?)', (FirstName, LastName, PhoneNumber))

conn.commit()