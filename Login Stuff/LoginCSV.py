#Christian Krenzlin
import uuid
import hashlib
import getpass
import csv
import sys
UserDict = {}
status = ""

def hash_password(password):
	return hashlib.sha256(password.encode()).hexdigest()


def csvRead(UserDict):
	with open("data.csv") as csvData:
		fieldnames = ["username", "password"]
		csvReader = csv.DictReader(csvData,fieldnames = fieldnames)
		for row in csvReader:
			UserDict[row['username']] = row['password']



def csvWrite(username,password):
	with open("data.csv","a") as csvfile:
		fieldnames = ["username","password"]
		writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
		writer.writeheader()
		writer.writerow({"username":username, "password": password})



def register():
	csvRead(UserDict)
	newUser = input("Enter a username: ")
	if newUser in UserDict:
		print("This user already exists")
	else:
		createPass = getpass.getpass()
		hashed_pass = hash_password(createPass)
		csvWrite(newUser,hashed_pass)
		print("User has been created")


def login():
	csvRead(UserDict)
	username = input("Enter your username: ")
	passw = getpass.getpass()
	hashed_password = hash_password(passw)
	try:
		if hashed_password == UserDict[username]:
			print("Login succeeded")
	except Exception:	
		print("Login failed")


def display():
	status = input("Are you registered? [y/n] (press q to quit): ")
	if status == "y":
		login()
	elif status == "n":
		register()
	elif status == "q":
		sys.exit()
	return status

while status != "q":
	status = display()
