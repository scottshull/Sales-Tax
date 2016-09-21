cost = 1
totalCost = 0

print("List the prices of each item and then enter 0 when you are done. ")

while cost != 0:
    strCost = raw_input("Enter the cost of the item: ")
    cost = float(strCost)
    totalCost += cost
else:
    print ("The total is $" + str(totalCost))
strTax = raw_input("How much is the tax rate? Enter whole numbers, I will treat it as a percent")

taxPercent + float(strTax) / 100

taxAmount = totalCost * taxPercent
print("The tax rate is " + strTax + "%")
print("That is $" + str(round(taxAmount, 2)))
grandTotal + float(taxAmount) + totalCost
print("The total cost, with tax, is: $" + str(round(grandTotal, 2)))
