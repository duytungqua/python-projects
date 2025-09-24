#unpack list
colors = ['red', 'blue', 'green']
print(colors[0]) #red
print(colors[1]) #blue
print(colors[2]) #green
#unpack list to variables
red, blue, green = colors
print(red) #red
print(blue) #blue
print(green) #green
red1, blue1 = colors[0:2]
print(red1) #red

#unpacking and packing
lst = [1, 2, 3, 4, 5]
a, b, *new_lst = lst
print(a)        # 1
print(b)        # 2
print(new_lst)  # [3, 4, 5]
*a, b, c = lst
print(a)        # [1, 2, 3]
print(b)        # 4
print(c)        # 5
# finish unpack list
