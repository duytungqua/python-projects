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
#sort dictionary
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_dict = dict(sorted(my_dict.items()))
print("Sorted Dictionary:", sorted_dict)
#sort dictionary by value

sorted_dict_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted Dictionary by Value:", sorted_dict_by_value)

#slice in list lst = [start: end:]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
slice_lst = lst[-3:]
retrieve = lst[::4]
lst.sort(reverse=True)
reverse_lst = lst[::-1]
print("Sliced List:", slice_lst)
print("Retrieve every second element:", retrieve)
print("Sorted List in Descending Order:", lst)
print("Reversed List:", reverse_lst)

#substiuting a part of list 
lst[2:5] = [10, 11, 12]
print("List after substitution:", lst)

#partial replacement and resize
new_lst = [1, 2, 3, 4, 5]
new_lst[1:4] = [20, 30]  # Replace elements at
print("List after partial replacement and resize:", new_lst)
new_lst[1:3] = [8, 9, 7, 6]  # Replace elements at index 1 and 2 with four new elements
print("List after expanding elements:", new_lst)

