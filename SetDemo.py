set1 = {1,2,3,4,5}
set2 = {4,5,6,7}

print("Intersection:",set1 & set2)
print("Intersection:",set1.intersection(set2))
# {4,5}

print("Difference:", set1-set2)
print("Difference:",set1.difference(set2))
# {1,2,3}

print("Union:", set1|set2)
print("Union:", set1.union(set2))
#{1,2,3,4,5,6,7}

print("Symmetric difference:", set1^set2)
print("Symmetric difference:", set1.symmetric_difference(set2))
#{1,2,3,6,7}

for x in set1:
    print(x, end=" ")
