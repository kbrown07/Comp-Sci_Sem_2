items = int(input("how many items?"))

total = 0
for i in range (0, items):
    itemName = input("What is the name?")
    price = float(input("How much is it?"))
    print("Thanks for purchasing " + itemName)
    total = total + price
    
print("Your total is: " + str(total))
    


