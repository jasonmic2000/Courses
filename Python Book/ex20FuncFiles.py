#Importing argv from system
from sys import argv
script, input_file = argv

#defining function to print all contents of file
def print_all(f):
    print(f.read())

#defining function to seek back to the start of the file
def rewind(f):
    f.seek(0)

#defining functions to print a line from the file with the line number
def print_a_line(line_count, f):
    print(line_count, f.readline())

#opening the current file
current_file = open(input_file)

#printing the entire file
print("First let's print the whole file: \n")
print_all(current_file)

#seeking back to the start of the file
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

#printing first three individual lines of the file
print("Let's print 3 lines: ")

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line,current_file)
