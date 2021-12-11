# [] are used to assign a list of values to a variable
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#This is the first For-loop going through the list the_count
for count in the_count:
    print(f'This is count {count}')

#Same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#We can also go through mixed lists
for i in change:
    print(f"I got {i}")

#We can also build lists, first start with an empty list
elements=[]

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Element was: {i}")
