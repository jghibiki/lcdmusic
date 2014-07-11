from subprocess import call
from time import sleep

file = open("outputDevice.txt", "r")
outputLocation = file.read()

blank = "'                                        '"
command = "echo"
line1 = ""
line2 = ""

isRunning = True

while isRunning:
    message = "test"
    call(command + " " + message + " > " + outputLocation, shell=True)
    isRunning = False



