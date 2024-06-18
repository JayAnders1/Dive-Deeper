# Question 1 Task 1

# number = float(input("Enter a number: "))

# if number > 0:
#     print("The number is positive.")
# elif number == 0:
#     print("The number is zero.")
# elif number < 0:
#     print("The number is negative.")


    # Question 2 Task 1

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
z = int(input("Enter a number: "))

if y <= x >= z:
    print(f"The largest number is: {x}")
elif z <= y >= x:
    print(f"The largest number is: {y}")
else:
    print(f"The largest number is: {z}")

    # Question 2 Task 2

if y >= x <= z:
    print(f"The smallest number is: {x}")
elif z >= y <= x:
    print(f"The smallest number is: {y}")
else:
    print(f"The smallest number is: {z}")

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

