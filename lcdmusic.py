from subprocess import call
from time import sleep

file = open("outputDevice.txt", "r")
outputLocation = file.read()

blank = "'                                        '"
command = "echo"
line1 = ""
line2 = ""

switch = True

slide1a = "'(O.O)  (*.*)  ($.$) '"
slide2a = "'(-.-)  (0.O)  (O.O) '"

slide1b = "'*-*-*-*-*-*-*-*-*-*-'"
slide2b = "'-*-*-*-*-*-*-*-*-*-*'"

while True:
	
	message = blank
	call(command + " " + message + " > " + outputLocation, shell=True)

	if switch:
		message = slide1a
		message += slide1b
		switch = False
	else:
		message = slide2a
		message += slide2b
		switch = True

	call(command + " " + message + " > " + outputLocation, shell=True)

	sleep(0.01)



