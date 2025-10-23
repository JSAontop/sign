bags = int(input("Enter number of bags: "))
while bags < 1:
    bags = int(input("Invalid number of bags. Try again.\n "))
sweets = int(input("Enter number of sweets: "))
while sweets <= bags:
    sweets = int(input("The number of sweets must be greater than the number of bags. Try again.\n "))
for x in range  (1, int(bags), 2):
    if int(sweets) % x  == 0:
        print(x)
        