#Variable = a container for a value
first_name="Clinton"
last_name="Ojo"
Full_name=first_name+" "+last_name
print("Hello"+Full_name)

#Dont print variables with "" because that turns it into a string intstead
#print(type(name))
#shows what data class the variable is
#Int
age=19
age+=1
print("your age is:"+str(age))#If i want to print something with a string i gotta typecast it
print(type(age))

#Float
height=195.5
print("your height is :"+str(height)+"cm")
print(type(height))
#Boolean Aka true or flase
Human=False
print("Are you human:"+str(Human))
print(type(Human))

#mutple assigment = allows us to assign mutiple variables at the same time in one line of code
#This is one way
Spongebob=Patrick=Sandy=Squidward=30
#This is another
Clinton,Thomas,Joseph="Tall",1.65,True
print(Clinton,Thomas,Joseph)
print(Sandy,Patrick,Spongebob,Squidward)
print(type(Sandy))
print("Bob is :"+str(Sandy))