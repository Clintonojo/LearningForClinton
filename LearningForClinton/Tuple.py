#tuple= collection which is ordered and unchangeable
# used to group together related data

student=("Bro",21,"male")

#Count method to see how many times this element appears
print(student.count("Bro"))

print(student.index("male"))

for x in student:
    print (x)

    if "Bro" in student:
        print("bro is here")