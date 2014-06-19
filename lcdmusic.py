from subprocess import call

outputLocation = "testFile.txt"

message = "'Hello'"

command = "echo"

call(command + " " + message + " > " + outputLocation, shell=True)

