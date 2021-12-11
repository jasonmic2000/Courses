#Importing argument variable module
from sys import argv
script, filename = argv
#Asking user confirmation to erase contents of file
print(f"We're going to erase the file {filename}")
print("If you don't want that, hit CTRL-C (^C)") #CTRL-C causes traceback and ends current process in command prompt
print("If you do want that, hit RETURN (ENTER)")

input("?")
#Opening file
print("Opening the file...")
target = open(filename, 'w')
#Deleting all contents from the file
print("Truncating the file, Goodbye!")
target.truncate()
#Accepting 3 lines of input from the user
print("Now I'm going to ask you for three lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")
#Writing the three lines of input to the file
print("I'm going to write these lines to the file.")
target.write(line1)
target.write(line2)
target.write(line3)
target.write("\n")
#Closing the file
print("And finally, we close it.")
target.close()
