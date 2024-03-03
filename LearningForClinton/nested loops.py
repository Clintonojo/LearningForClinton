#nested loops = the "inner loop" will finsh allof it's iterations before
#               finshing one iteration of the "outer loop"
#               Bascially a loop inside a loop

rows=int(input("How many rows:"))
columns=int(input("How many columns:"))
symbol=input("Enter what symbol to use:")
#outerloop
for i in range(rows):
    #inner loop it will run first
    for j in range(columns):
        print(symbol, end="")
        #this last print has to line up with the inner loop
    print()
