#Using \n for newlines and \t for tabs
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\nnewlines and \t tabs')

#Using triple quote (""") for multi-line string
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \nthe needs of lovely
nor comprehend passion from intuition
and requies a explanation
\n\t\twhere there is none
"""

#Printing poem
print("--------------")
print(poem)
print("--------------")

#Using math operators
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

#Defining a function
def secret_formula(started):
    jelly_beans =  started * 500
    jars = jelly_beans / 1000
    crates = jars / 1000
    return jelly_beans, jars, crates

#Setting variable for using in the function and calling it with said value
start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
#It's just like with an f"" cooked_string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

#Changing value of the variable for use in the function
start_point = start_point / 10

#Calling on function again with new value
print("We can also do that this way")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("we'd have {} beans, {} jars, and {} crates.".format(*formula))
#Using format with function *formula returns values from function to the formatted string
