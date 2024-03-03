#slicing = create a substring by extracting elements from another string
#          indexing[] or slice[]
#          [start:stop:step]

#Indexing getting certain part in a string
#name="Bro Code"
#index starts at 0 is B  is 0
#this says first three characters
#first_name=name[0:3]#strart and stop

#last_name=name[4:8]#start and stop
#funky_name=name[0:8:3]#Prints every third charcater
#reversed_name=name[::-1]#revereses the name
#print(reversed_name)
#print(first_name)
#print(last_name)
#print(funky_name)

#trick= input("Enter your name please")

#reversed_input=trick[::-1]

#print(reversed_input)

#Slcing how to get certain part in a string
website2="Http://wikipedia.com"
website="http://google.com" #Using negative index starts with -1 so m is neg 1 and o is negative 2
slice = slice(7,-4)
print(website[slice])
print(website2[slice])