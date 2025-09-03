for i in range(5):
    print("Iteration:", i)  
i = 0
while i < 5:
    print("While Loop Iteration:", i)
    i += 1
#break and continue

for i in range(10): 
    if i == 5:
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # This will print only odd numbers less than 5

    