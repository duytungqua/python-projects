#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#tuple with one item
thistuple = ("apple",)
print(thistuple)

#access tuple items
print(thistuple[0]) #banana

#loop through tuple
for x in thistuple:
    print(x)
#assign tuple to multiple variables
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green) #apple
print(yellow) #banana
print(red) #cherry  

#Can you assign a new tuple to a variable that references a tuple?
# Use tuple to prevent change a list
thistuple = ("kiwi", "orange")
emptytuple = ()
emptytuple = thistuple
print(emptytuple) #('kiwi', 'orange')
