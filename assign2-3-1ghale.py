#assign2-3-1ghale.psy 11/9/2025
# Hazel Houa=secleaning servive calculator

# planning - Declaring constants
SERVICE_CHARGE = 40
MESSAGE = "Program Complete."
CHARGE_BATHROOM = 15
CHARGE_ROOM = 10



lastName = input("Enter your Last Name: ")
numBathroom = input("Enter number of Bathroom to be cleaned: ") 
numBathroom = int(numBathroom)
numRoom = input('Enter number of rooms to be cleaned: ')
numRoom = int(numRoom)
costBathroom = numBathroom * CHARGE_BATHROOM
costRoom = numRoom * CHARGE_ROOM
totalCost =SERVICE_CHARGE + costBathroom + costRoom

print(f"Customer Name: {lastName}")
print(f"The total cost to clean {numBathroom} bathroom is {costBathroom}.")
print(f"The total cost to clean {numRoom} oF room is {costRoom}.")
print(f"The total cost of the whole house is {totalCost}")
print(f"{MESSAGE}")
