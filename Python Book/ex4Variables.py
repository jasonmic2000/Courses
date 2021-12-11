#Number of cars
cars = 100
#Space in each car
space_in_a_car = 4
#Number of drivers available
drivers = 30
#Total number of passengers to be transported
passengers = 90
#Number of empty cars
cars_not_driven = cars - drivers
#Number of cars that will be driven
cars_driven = drivers
#Total number of passengers that can be transported
carpool_capacity = cars_driven * space_in_a_car
#Number of passengers to be accomodated in each car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "passengers today.")
print("We have", passengers, "to transport today.")
print("We have to put about", average_passengers_per_car, "passengers in each car.")
