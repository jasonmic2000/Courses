#Importing argument variable from system
from sys import argv
from os.path import exists #Module to check if file exists
#argv variables
script, from_file, to_file = argv
#Statement displaying file names from where data is being copied and to which file
print(f"Copying from {from_file} to {to_file}")
#Opening input file and reading data from it as indata
in_file = open(from_file);indata = in_file.read()
#Finding total number of bytes stored in indata i.e. total bytes in input file
print(f"The input file is {len(indata)} bytes long")
#Checking whether output file exists
print(f"Does the output file exist? {exists(to_file)}")
#Asking for user input to continue operation or abort
print("Ready, \nHit ENTER to continue\nCTRL-C to abort.")
input()
#Opening output file and writing data from input file to it
out_file = open(to_file, 'w')
out_file.write(indata)
#Confirmation statement printed and displayed to user
print("Alright, all done")
#Closing input and output files
out_file.close()
in_file.close()
