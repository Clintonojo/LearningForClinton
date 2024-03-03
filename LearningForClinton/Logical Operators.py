#Logical operators(and,or,not) = used to check if two or more conditional statements is true


temp =int(input("what is the tempertaure outside:"))
#and operator both of the condtions have to be met
if temp>=0 and temp<=30:
      print("the weather outside is great")
      print("go outside!")
      #OR operator only one condition has to be met so if one true the entire statement is true
elif temp<=0 or temp>31:
 print("The weather is not good!")
 print("Stay inside bro")

 #elif not(temp <= 0 or temp > 31):
#not opertor makes the conditon not true so this flips it so reverse.