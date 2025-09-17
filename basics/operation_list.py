#sort list
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
lst.sort()

#reverse sort
lst.sort(reverse=True)
print("Sorted List:", lst)

#sort list number
numbers = [10, -1, 2, 3, 0, -5, 8]
numbers.sort()
print("Sorted Numbers:", numbers)

#sort with key
words = ["apple", "banana", "cherry", "date"]
words.sort(key=len)  # Sort by length of the word
print("Words sorted by length:", words)
#sort tuple list
tuple = [(1, 'banana'), (3, 'apple'), (2, 'cherry')]
tuple.sort()
print("Sorted Tuple List:", tuple)

#number tuple list
tuple_1 = (1, 6, 9, 4, 2)
sorted_tuple = sorted(tuple_1)
print("Sorted Tuple:", sorted_tuple)

#lambda with sort: lambda arguments: expression
company = [("Google", 200), ("Apple", 450), ("Microsoft", 300)]
company.sort(key = lambda company: company[0]) #sort by first element
print("Sorted Company List:", company)
company.sort(key = lambda company: company[1]) #sort by second element

print("Sorted Company List:", company)