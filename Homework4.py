import random
from math import floor

#1.Write a program that asks the user to enter a list of integers. Do the following:
# li = [23,45,5,54,5,67,4,32,2,3]
# while True:
#     num = int(input("Enter a number: "))
#     li.append(num)
#     option = input("Would you like to add another number? (y/n): ")
#     if option.lower() == "n":
#         break

#a. Print the total number of items in the list.
# print("Total numbers of items in the list:",len(li))
# #b. Print the last item in the list.
# print("The last item in the list:",li[-1])
# #c. Print the list in reverse order.
# print("List in reverse order:",li.reverse())
# #d. Print Yes if the list contains a 5 and No otherwise.
# if li.count(5)==0:
#     print("List does not contain 5")
# else:
#     print("List contains 5")
# #e. Print the number of fives in the list.
# print("number of fives in the list:",li.count(5))
# #f. Remove the first and last items from the list, sort the remaining items, and print the result
# li.pop(0)
# li.pop()
# li.sort()
# print(li)
#g. Print how many integers in the list are less than 5.
# li.sort()
# print("Number of integers less than 5:",len(li[:li.index(5)]))


#2. Write a program that generates a list of 20 random numbers between 1 and 100.
# li = []
# for i in range(20):
#     num = random.randint(1, 100)
#     li.append(num)
# #(a) Print the list.
# print(li)
# #(b) Print the average of the elements in the list.
# print("The average of the elements in the list:", sum(li)/len(li))
# #(c) Print the largest and smallest values in the list
# li.sort()
# print("The smallest element in the list:", li[0])
# print("The largest element in the list:", li[-1])
# #(d) Print the second largest and second smallest entries in the list
# li.sort()
# print("The second smallest element in the list:", li[1])
# print("The second largest element in the list:", li[-2])
# #(e) Print how many even numbers are in the list
# count=0
# for items in li:
#     if items % 2 == 0:
#         count += 1
# print("The number of even numbers in the list:",count)


#3. Start with the list [8,9,10]. Do the following:
# li = [8,9,10]
# # (a) Set the second entry (index 1) to 17
# li[1]=17
# # (b) Add 4, 5, and 6 to the end of the list
# li.append(4)
# li.append(5)
# li.append(6)
# # (c) Remove the first entry from the list
# li.pop(0)
# # (d) Sort the list
# li.sort()
# # (e) Double the list
# li.extend(li)
# # (f) Insert 25 at index 3
# li.insert(3,25)
# print(li)


#4. Ask the user to enter a list containing numbers between 1 and 12. Then replace all the entries in the list that are greater than 10 with 10.
# li = [4,6,9,10,12,7,8,12,11,5,11]
# for i in range(0,len(li)):
#     if li[i]>10:
#         li[i]=10
# print(li)

#5. Ask the user to enter a list of strings. Create a new list that consists of those strings with their first characters removed.
# li = ["Rohan","Nisarg","Sagar","Dhrumil"]
# li1=[]
# for item in li:
#     li1.append(item[1:])
# print(li1)


# 6. Create the following lists using a for loop.
#li = []
# (a) A list consisting of the integers 0 through 49
# for i in range(0,50):
#     li.append(i)
# print(li)
# (b) A list containing the squares of the integers 1 through 50.
# for i in range(1,51):
#     li.append(i**2)
# print(li)
# (c) The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.
# li1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# for i in range(0,len(li1)):
#     li.append(li1[i]*(i+1))
# print(li)


#7. Write a program that takes any two lists L and M of the same size and adds their elements
# together to form a new list N whose elements are sums of the corresponding elements in L
# and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13].

# L = [3,1,4]
# M = [1,5,9]
# N = []
#
# for i in range(0,len(L)):
#     N.append(L[i] + M[i])
# print(N)

# 9. When playing games where you have to roll two dice, it is nice to know the odds of each
# roll. For instance, the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about
# 17%. You can compute these mathematically, but if you don't know the math, you can write
# a program to do it. To do this, your program should simulate rolling two dice about 10,000
# times and compute and print out the percentage of rolls that come out to be 2, 3, 4, . . . , 12.

# dice1 = random.randint(1, 6)
# dice2 = random.randint(1, 6)
# li=[]
# for i in range(1000):
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     li.append(dice1+dice2)
# for i in range(2,13):
#     print(f"number {i}: {round((li.count(i)/1000)*100)}%")

#10. Write a program that accepts a list from user. Your program should reverse the content of list and display it. Do not use reverse() method.
# li = [9,8,7,6,5,4,3,2,1]
# for i in range(0,len(li)):
#     li.insert(i,li[len(li)-1-i])
#
# for i in range(len(li),floor(len(li)/2),-1):
#     li.pop()
#
# print(li)

#11. Write a program with a function that accepts a string from keyboard and create a new string after converting character of each word capitalized. For instance, if the sentence is "stop and smell the roses." the output should be "Stop And Smell The Roses"

sentence = input("Enter a sentence: ")
li = []
li.extend(sentence.split(" "))

for word in li:
    word = word.capitalize()
    print(word, end=" ")