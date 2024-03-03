#if statement = a block of code that execute if it's condition is true

age=int(input("What old are you:"))
#if statement only ran when true
if age==100:
    print("You are an century")
elif age>=18:#== is equal to so its comparison
    print("you are 18 years old")
    #another if statement
elif age<1:
    print("you havent been born yet")

    #else stament only ran when all condition havent been meet
else:
    print("you are a child! ")
