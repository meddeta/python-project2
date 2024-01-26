

# Code for task 1 after this line
print("\n--- Task 1 ---: Compute Fare")
print("(1) One way or (2) round trip?")
x = int(input("Enter 1 or 2: "))
y = str
fare = float

while x > 2 or x <= 0:
    print("*Please enter valid number!")
    x = int(input("Enter 1 or 2: "))

else:
    if x == 1:
        y = "One way trip"
        fare = 1.80
    elif x == 2:
        y = "Round trip"
        fare = 3.50

    print("Your trip is: ",y ,"\n")
    print("Now please select Age Range:")
    print("(1) Under 12")
    print(("(2) 13-64"))
    print(("(3) 65 or older"))
    age = int(input("Enter 1, 2 or 3: "))
    fare_condition = str

    while age > 3 or age < 1:
        print("*Please enter valid number!")
        age = int(input("Enter 1, 2 or 3: "))
    else:
        if age == 1 or age == 3:
            fare = fare/2
            fare_condition = "reduced fare"
        elif age == 2:
            fare = fare
            fare_condition= "full fare"
        print("\nTotal amount due: $"+ str(fare) + ' ['+str(y),'('+str(fare_condition)+')'+']')

x = input("Input a string: ")
i = 0
while i < len(x):
    for boz in x:
        print("str["+str(i)+"] =", boz.replace(" ", "SPACE"))
        i += 1
gaav = x[::-1]
print("reverse no spaces: ", gaav.replace(" ", ""))




# Code for task 3 after this line
print("\n--- Task 3 ---: The maximum *even* number")
print("The maximum *even* number")
print("Keep entering positive integer. To quit, input a negative integer")
x = 0
largest_number = 0
if x < 0:
    print("No numbers were provided; Try again!")
    x = int(input("Enter number: "))
while x >= 0:
    x = int(input("Enter number: "))
    if x%2 == 0:
        if x > largest_number:
            largest_number = x

    if x < 0:
        print("Largest even number:", largest_number)
        break


# Code for task 4 after this line
print("\n--- Task 4 ---: Better triangle draw")
x = int(input("Enter size between 5 and 20: "))
while x<5 or x>20:
    x = int(input("Enter size between 5 and 20: "))
else:
    for i in range(0, x):
        print(("-"* i)+ "\\")

    print(("-" * x) + "|")

    for i in range(x-1, -1, -1):
        print(("-" * i) + "/")


input("Press enter to quit.")
