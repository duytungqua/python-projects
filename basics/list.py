#arraty 
empty_lis = []
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1]) #banana
fruits.append("date")

cordinates = [[0,10], [10, 20], [20, 30]]
print(cordinates[0][0])

#loop cordinates
for x, y in cordinates:
    print(f"x: {x}, y: {y}")

#access last element:
print(fruits[-1]) #date
print(coridnates[-1][-1]) #30

#remove elemment: use pop()
fruits.pop() #remove last element
print(fruits)
fruits.pop(0) #remove first element
print(fruits)

fruits.insert(0, "kiwi") #add kiwi to first position
fruits.remove(""banana") #remove banana by value