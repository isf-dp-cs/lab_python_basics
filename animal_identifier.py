legs = int(input("Enter the number of legs the animal has: "))
fur = input("Does the animal have fur? (yes/no) ")
fly = input("Can the animal fly? (yes/no) ")

type = None

if legs == 4:
    if fur == "yes":
        if fly == "yes":
            type = "a flying mammal"
        else:
            type = "a mammal"
    else:
        type = "a reptile"

print("The animal is:", type)