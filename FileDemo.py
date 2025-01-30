# myFile = open("myFile.txt", "a")
# print("Welcome to my file",file=myFile)
# myFile.close()

myFile = open('myFile.txt', 'r')
# print(myFile.read())

for line in myFile:
    print(line, end='')

