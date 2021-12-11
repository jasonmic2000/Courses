#defining function to add two integers
def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

#defining function to subtract b from a
def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

#defining function to multiply a and b
def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

#Defining function to divide a by b
def divide(a,b):
    print(f"DIVIDING {a}/{b}")
    return a / b

print("Let's do some math with just functions")

age = add(12,7)
height = subtract(190, 18)
weight = multiply(41,2)
iq = divide(284,2)

print(f"Age = {age}\nHeight = {height}\nWeight = {weight}\nIQ = {iq}")

#A puzzle for extra credit
print("Here is a puzzle:")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "Can you do it by hand?")
