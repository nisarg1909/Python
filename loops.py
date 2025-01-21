# while loop
#1.
# rollno = int(input("Enter Rollno: "))
# name = input("Enter name: ")
# maths = int(input("Enter maths marks: "))
# while maths<=0 or maths>=100:
#     print("Enter a valid maths mark")
#     maths = int(input("Enter maths mark: "))
# science = int(input("Enter science marks: "))
# while science<=0 or science>=100:
#     print("Enter a valid science mark")
#     science = int(input("Enter science mark: "))
# english = int(input("Enter english marks: "))
# while english<=0 or english>=100:
#     print("Enter a valid english mark")
#     english = int(input("Enter english mark: "))

#2.
# while True:
#     rollno = int(input("Enter Rollno: "))
#     name = input("Enter name: ")
#     maths = int(input("Enter maths marks: "))
#     while maths<=0 or maths>=100:
#         print("Enter a valid maths mark")
#         maths = int(input("Enter maths mark: "))
#     science = int(input("Enter science marks: "))
#     while science<=0 or science>=100:
#         print("Enter a valid science mark")
#         science = int(input("Enter science mark: "))
#     english = int(input("Enter english marks: "))
#     while english<=0 or english>=100:
#         print("Enter a valid english mark")
#         english = int(input("Enter english mark: "))
#     option = input("Do you wish to continue? [Y/N] : ")
#     if option.lower() == "n":
#         break

#3.
# start=1
# while start<=10:
#     print(start)
#     start+=1

#4.
# start=int(input("Enter the start number: "))
# end=int(input("Enter the end number: "))
# while start<=end:
#     print(start)
#     start=start+1

#5.
# start=1
# total=0
# while start<=5:
#     no=int(input("Enter number for addition:"))
#     total=total+no
#     start=start+1
# print("The sum of all the numbers is",total)

#6.
# no = int(input("Enter number for multiplication table: "))
# start=1
# while start <= 10:
#     print(no,"x",start,"=",no*start)
#     start+=1

#7.
# no = int(input("Enter a number to find its divisors: "))
# start=1
# print("divisors:")
# while start <= no:
#     if no%start==0:
#         print(start)
#     start=start+1

#8.
# no = int(input("Enter a number to check if it is a prime number or not: "))
# start=2
# isPrime=True
# while start < no:
#     if no%start==0:
#         isPrime=False
#         break
#     start=start+1
#
# if isPrime:
#     print("The number is prime number")
# else:
#     print("The number is not prime number")

#9.
# startno = int(input("Enter start number : "))
# endno = int(input("Enter end number : "))

# while startno <= endno:
#     start = 2
#     isPrime = True
#     while start<startno:
#         if startno%start==0:
#             isPrime=False
#             break
#         start=start+1
#     if isPrime:
#         print(startno)
#
#     startno+=1


# for loop

#1.
# for i in range(1,51,10):
#     print(i)

#2.
# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))
# for i in range(start,end+1):
#     print(i)

#3.
# for i in range(10,0,-1):
#     print(i)

#4.
# total = 0
# for i in range(5):
#     num = int(input("Enter a number: "))
#     total = total+num
# print("Sum of numbers is:", total)

#5.
# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)

#6.
# num = int(input("Enter a number to find divisors: "))
# print("Divisors:")
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i)

#7.
isPrime = True
num = int(input("Enter a number: "))
for i in range(2, num):
    if num % i == 0:
        isPrime = False
        break
if isPrime:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
