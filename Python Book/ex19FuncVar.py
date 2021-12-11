#Functions and Variables
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

#Directly giving numbers to functions
print("We can just give the function numbers directly: ")
cheese_and_crackers(20,30)

#Using variables as inputs for the functions
print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#Using math operators for values used in function
print("We can even do math inside: ")
cheese_and_crackers(10+20,5+6)

#Using variables and math operators for values in function
print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
