#1.	Write a  program to accept two integers and check whether they are equal or not.
# no1 = int(input("Enter number1: "))
# no2 = int(input("Enter number2: "))
# if no1==no2:
#     print("Numbers are equal")
# else:
#     print("Numbers are not equal")

#2. Write a  program to check whether a given number is even or odd.
# number = int(input("Enter number to check if it is odd or even: "))
# if number % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

#3. Write a  program to check whether a given number is positive or negative.
# number = int(input("Enter number: "))
# if number<0:
#     print("Number is negative")
# else:
#     print("Number is positive")

#4. Write a  program to find whether a given year is a leap year or not.
# year = int(input("Enter year to check if it is a leap year: "))
# if year % 4 == 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")

#6. Write a  program to read the value of an integer m and display the value of n is 1 when m is larger than 0, 0 when m is 0 and -1 when m is less than 0.
# m = int(input("Enter a number: "))
# if m > 0:
#     n=1
# elif m < 0:
#     n=-1
# else:
#     n=0
# print("The value of n is",n)

#8. Write a program to find the largest of three numbers.
# no1 = int(input("Enter no1: "))
# no2 = int(input("Enter no2: "))
# no3 = int(input("Enter no3: "))
# if no1 > no2 and no1 > no3:
#     print(no1,"is largest")
# elif no2 > no1 and no2 > no3:
#     print(no2,"is largest")
# else:
#     print(no3,"is largest")

#9. Write a  program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies.
# x = int(input("Enter value for X-axis: "))
# y = int(input("Enter value for Y-axis: "))
#
# if x > 0 and y > 0 :
#     print(f"The coordinate point ({x},{y}) lies in First Quadrant")
#
# elif x < 0 and y > 0 :
#     print(f"The coordinate point ({x},{y}) lies in Second Quadrant")
#
# elif x < 0 and y < 0 :
#     print(f"The coordinate point ({x},{y}) lies in Third Quadrant")
#
# else:
#     print(f"The coordinate point ({x},{y}) lies in Fourth Quadrant")


#10. Write a  program to find the eligibility of admission for a professional course based on the following criteria:
# maths = int(input("Enter a Maths marks: "))
# physics = int(input("Enter a Physics marks: "))
# chemistry = int(input("Enter a Chemistry marks: "))
# total = maths + physics + chemistry
#
#
# if (maths>=65 and physics>=55 and chemistry>=50) or (total>=180):
#     print("The candidate is eligible for admission.")
#
# else:
#     print("The candidate is not eligible for admission.")

#16. Write a  program to check whether a character is an alphabet, digit or special character.
# char = input("Enter a character: ")
#
# if char.isalpha():
#     print("The character an alphabet")
# elif char.isdigit():
#     print("The character is a digit")
# else:
#     print("The is a special character")

#23. Write a program in  to read any Month Number in integer and display Month name in the word.
month = int(input("Enter month in digit (1-12): "))
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
if 1 <= month <= 12:
    print("The month is", months[month-1])
else:
    print("Enter a valid digit")