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


#while loop with else
count = 0
while count < 3:
    print("Count:", count)
    count += 1
else:
    print("Loop ended normally.")   


#break with else
for i in range (5):
    if i == 3:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)
else:
    print("Loop completed without break.")  

#continue with else
for i in range(5):
    if i % 2 == 0:
        continue
    print("Odd i =", i)
else:
    print("Loop completed without break.")
# Review of Python Basics
print("Loop module loaded.")

#if not <=> !(java)
x = 10
if not x < 5:
    print("x is not less than 5")

# --- IGNORE ---   
"""
 --- IGNORE ---
 Loop Examples
"""