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