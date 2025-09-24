cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
for city in cities:
    print(city)

#using range() function
for i in range(5):
    print("Iteration:", i)

#using while loop
i = 0
while i < 5:
    print("While Loop Iteration:", i)
    i += 1

#use enumerate() to get index and value
for index, city in enumerate(cities):
    print(f"Index: {index}, City: {city}")

