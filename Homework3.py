#1. Write a program in  to display the first 10 natural numbers.
# for i in range(1,11):
#     print(i,end=" ")

#2.  Write a  program to find the sum of first 10 natural numbers.
#total=0
# for i in range(1,11):
#     total=total+i
# print("The Sum is",total)

#3. Write a program in to display n terms of natural number and their sum.
# sum=0
# num = int(input("Enter a number: "))
# print(f"The first {num} natural numbers are: ")
# for i in range(1,num+1):
#     print(i,end=" ")
#     sum=sum+i
# print()
# print(f"The sum of natural numbers upto {num} terms is: {sum}")

#4. Write a program in to read 10 numbers from keyboard and find their sum and average.
# sum=0
# for i in range(10):
#     num = int(input("Enter a number: "))
#     sum = sum + num
# print("The sum is", sum)
# print("The average is", sum/10)

#5. Write a program in  to display the cube of the number upto given an integer.
# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     print(f"Number is: {i} and cube of the {i} is: {i**3}")

#7. Write a program in  to display the multiplication table vertically from 1 to n.
# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)
#
#     print()

#8. Write a program in to display the n terms of odd natural number and their sum
# sum = 0
# num = int(input("Enter a number: "))
# print("The odd numbers are:",end=" ")
# for i in range(num):
#     print(2*i+1, end=" ")
#     sum = sum + 2*i+1
# print()
# print(f"The Sum of odd Natural Number upto {num} terms : {sum} ")

#9. Write a program in  to display the pattern like right angle triangle using an asterisk.
# for i in range(5):
#     print(i*"*")

#10. Write a program in  to display the pattern like right angle triangle with a number.
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#14. Write a program in to make such a pattern like a pyramid with an asterisk.
for i in range(1,5):
    for j in range(1,i+1):
        print(" "*(5-i),end="")
        print("*",end="")
    print()