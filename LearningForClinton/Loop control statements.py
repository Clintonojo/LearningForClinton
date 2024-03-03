#Loop Control statements = changes a loops exceution from its normal sequence

#break= used to terminate the loop entireley
#continue= skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

while True:
    name=input("Enter you name:")
    if name !="":
        break

phone_number="123-456-7890"
#iteration so its what every number
for i in phone_number:
    #if index is a string
    if i=="-":
        #continue and ingnore the dashes
        continue
        #end makes the string be all on the same line
    print(i,end="")


for i in range(1,21):

    if i==13:
        pass
    else:
        print(i)


