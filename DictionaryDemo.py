# person = {
#     "firstName": "Vimal",
#     "LastName": "Patel",
#     "phno":"957639283"
# }
# print(person["firstName"])
# print(person.keys())
# person["Age"]=30
# print(person)
# print(person.values())
# print(person.items())

# for k in person.keys():
#     print(k)

# for v in person.values():
#     print(v)

# for k,v in person.items():
#     print(k,":",v)


# words = input("Enter a sentence: ").lower()
# wordsList = words.split()
# wordsDict = {}
#
# print(wordsList)
# for word in wordsList:
#     if word in wordsDict:
#         wordsDict[word] += 1
#     else:
#         wordsDict[word] = 1
# print(wordsDict)

# dict1 = dict(zip("abc",[1,2,3]))
# print(dict1)


class Bag:
    def __init__(self):
        self.itemsList = []

    def add_item(self, item):
        self.itemsList.append(item)

    def add_items(self, items):
        for item in items:
            self.add_item(item)

    def get_item(self,item):
        for item in self.itemsList:
            if item == item:
                self.itemsList.remove(item)
                return item



bag = Bag()
bag.add_item('Purse')
bag.add_items(["Pen","Mirror","Bread"])
print(bag.itemsList)
current_item = bag.get_item('Purse')
print(current_item)
print(bag.itemsList)

