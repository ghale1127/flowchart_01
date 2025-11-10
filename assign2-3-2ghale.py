#assign2-3-2ghale 11/9/2025
#Remodeling Project

#constants
HOUR_RATE = 30
WHOLESALE_PERCENTAGE = 1.20
MESSAGE = "End of program"

totalHours = input("Enter the Total numbers of hours for the job: ")
totalHours = float(totalHours)

costMaterials = input("Enter wholesale cost of the materials: ")
costMaterials = float(costMaterials)

costLabour = totalHours * HOUR_RATE
totalMaterials = WHOLESALE_PERCENTAGE * costMaterials
totalCost = costLabour + totalMaterials

print(f"Total cost for {totalHours}hrs of work is ${costLabour}")
print(f"Total wholesale cost of ${costMaterials} is ${costMaterials}")
print(f"The total cost for the whole job is :${totalCost}")
print(f"{MESSAGE}")
