#File to read a file and display it
from sys import argv
script, filename = argv
#Opening file
txt = open(filename)
#Printing contents of the file
print(f"Here's your file '{filename}' \n")
print(txt.read())
#Asking for filename again using normal input
print("Type the filename again")
file_again = input("> ")
#Re-opening the file
txt_again = open(file_again)
#Priting the contents of file from input statement
print(txt_again.read())
