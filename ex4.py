cars = 100
spaceInACar = 4.0
drivers = 30
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCapacity = carsDriven * spaceInACar
averagePassengersPerCar = passengers / carsDriven


print("There are", cars,"cars available.")
print("There are only", drivers,"dirvers available")
print("there will be", carsNotDriven,"empty cars today")
print("we can transport", carpoolCapacity,"people today")
print("we have", passengers, "to carpool today.")
print("we need to put about", averagePassengersPerCar,"in each car")