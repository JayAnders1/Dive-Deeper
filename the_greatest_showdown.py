x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

#question 2 task 1

if y <= x >= z:
    print(f"The largest number is: {x}")
elif z <= y >= x:
    print(f"The largest number is: {y}")
else:
    print(f"The largest number is: {z}")

#question 2 task 2

if y >= x <= z:
    print(f"The smallest number is: {x}")
elif z >= y <= x:
    print(f"The smallest number is: {y}")
else:
    print(f"The smallest number is: {z}")

#question 2 task 3

if y == x == z:
    print("All three numbers are equal!")
elif y == x > z:
    print("Two numbers are equal and the largest!")
elif y == z > x:
    print("Two numbers are equal and the largest!")
elif x == z > y:
    print("Two numbers are equal and the largest!")
elif y == x < z:
    print("Two numbers are equal and the smallest!")
elif y == z < x:
    print ("Two numbers are equal and the smallest!")
else:
    print ("Two numbers are equal and the smallest!")

