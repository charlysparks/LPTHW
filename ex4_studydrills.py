
#This is a short script to figure out how many people we can carpool today.
#I made changes to this file from the original in order to see the difference output.

#Available cars
cars = 100

#Available seats in a single car
space_in_a_car = 4

#Number of drivers available
drivers = 30

#Number of passengers needing a ride.
passengers = 90

#Number of available cars in order to be given a ride.
cars_not_driven = cars - drivers

#Number of cars that are currently being driven.
cars_driven = drivers

#Available spaces for carpooling
carpool_capacity = cars_driven * space_in_a_car

#Average number of people in each car
average_passengers_per_car = passengers / cars_driven

print("There are", cars ,"cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven , "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers , "passengers to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
