import math

#1. Write a shutting down program:
# First, def a function, shut_down, that takes one argument s. Then, if the shut_down function receives an s equal to "yes", it should return "Shutting down" Alternatively, elif s is equal to "no", then the function should return "Shutdown aborted". Finally, if shut_down gets anything other than those inputs, the function should return "Sorry".

# def shut_down(s):
#     while True:
#         if s=="yes":
#             print("Shutting down")
#             break
#
#         elif s=="no":
#             print("Shutting aborted!")
#             s = input("Would you like to shut down? (yes/no): ")
#
#         else:
#             print("Sorry Invalid input!")
#             s = input("Would you like to shut down? (yes/no): ")
#
#
# options = input("Would you like to shut down? (yes/no): ")
# shut_down(options)


#2. Import the math module in whatever way you prefer. Call its sqrt function on the number 13689 and print that value to the console.
# print(math.sqrt(13689))


#3. First, def a function called distance_from_zero, with one argument (choose any argument name you like). If the type of the argument is either int or float, the function should return the absolute value of the function input. Otherwise, the function should return "Nope". Check if it works calling the function with -5.6 and "what?".
# def distance_from_zero(n):
#     if isinstance(n, (int, float)):
#         print(abs(n))
#     else:
#         print("Nope")
#
# distance_from_zero(-5.6)
# distance_from_zero("what")


#4. Rewrite your pay computation program (previous chapter) with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
# def compute_pay(hour,rate):
#     if hour>40:
#         overtime = hour - 40
#         overtime_pay = overtime * (rate * 1.5)
#         regular_pay = 40*rate
#         total_pay = overtime_pay+regular_pay
#         print("Hours:",hour)
#         print("rate:",rate)
#         print("Pay:",total_pay)
#     else:
#         print("Hours:", hour)
#         print("rate:", rate)
#         print("Pay:", hour*rate)
#
# h = int(input("Enter Hours: "))
# r = int(input("Enter Rate: "))
# compute_pay(h,r)

#5.


# def hotel_cost(nights):
#     return 140*nights
#
# def plane_ride_cost(city):
#     plane_cost=0
#     if  c=="charlotte":
#         plane_cost = 183
#
#     elif c=="tampa":
#         plane_cost = 220
#
#     elif c=="pittsburgh":
#         plane_cost = 222
#
#     elif city=="los angeles":
#         plane_cost = 475
#
#     else:
#         "Invalid city!"
#
#     return plane_cost
#
# def rental_car_cost(days):
#     cost=0
#     if days>=7:
#         cost = (40*days)-50
#     elif 3<=days<7:
#         cost = (40*days)-20
#     else:
#         cost = 40*days
#
#     return cost
#
# def trip_cost(days,city):
#     print("Trip Cost: ",hotel_cost(days)+rental_car_cost(days)+plane_ride_cost(city))
#
#
# d = int(input("Enter number of hotel nights: "))
# c = input("Enter city to travel: ").lower()
# trip_cost(d, c)
