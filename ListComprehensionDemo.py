list1 = [x for x in range(10)]
list2 = [x for x in list1]
list3 = [x for x in list1 if x%2==0]
print(list3)


marks = [45,34,56,76,32,25,87,90,17]
pass_marks = [x for x in marks if x>=35]
fail_marks = [x for x in marks if x<35]
print(pass_marks)
print(fail_marks)