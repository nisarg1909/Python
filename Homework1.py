#1. Write a program that asks the user for his name and then welcomes him. The output should look like this:
# name = input("Enter your name: ")
# print("Welcome " + name)
import math

#2. Write a program that prompts the user to enter two integers and display the total on the screen.
# n01 = int(input("Enter n01: "))
# n02 = int(input("Enter n02: "))
# total = n01 + n02
# print("Total: ",total)

#3. Write a program that prompts the user to input a Celsius temperature and outputs the equivalent temperature in Fahrenheit. The formula to convert the temperature is: F = 9/5 C + 32 where F is the Fahrenheit temperature and C is the Celsius temperature.
# celsius = int(input("Enter temperature in celsius: "))
# fahrenheit = 9/5 * celsius + 32
# print("Fahrenheit: ", fahrenheit)

#5. Write a program that accepts seconds from keyboard as integer. Your program should convert seconds in hours, minutes and seconds.
# total_seconds = int(input("Enter the total number of seconds: "))
# hours = total_seconds // 3600
# remaining_seconds = total_seconds % 3600
# minutes = remaining_seconds // 60
# seconds = remaining_seconds % 60
# print("The total number of hours is: ", hours)
# print("The total number of minutes is: ", minutes)
# print("The total number of seconds is: ", seconds)

#6. Write a program that prompts the user to enter number in two variables and swap the contents of the variables.
# no1 = int(input("Enter the number of no1: "))
# no2 = int(input("Enter the number of no2: "))
# print(f"Before swapping: num1:{no1}, num2:{no2}")
# no1, no2 = no2, no1
# print(f"After swapping: num1:{no1}, num2:{no2}")

#8. Write a program that prompts the user to input the radius of a circle and outputs the area and circumference of the circle
# radius = int(input("Enter the radius of the circle to find it's area and circumference: "))
# area = 3.14 * radius * radius
# circumference = 2 * 3.14 * radius
# print("The area of the circle is: ", area)
# print("The circumference of the circle is: ", circumference)

#9. Write a program that prompts the user to input the length and the width of a rectangle and outputs the area and circumference of the rectangle
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
circumference = 2  * length * width
print("The area of the rectangle is ", area)
print("The circumference of the rectangle is ", circumference)