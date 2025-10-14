#array 
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
#find element in array
def city_finder(city_idx):
    result = print("Finding city:", city_idx)
    print("City found:", cities[city_idx])
    print("Index of city:", cities.index("Los Angeles"))

str = 'Iterables'
for char in str:
    print(char)

colors = ['red', 'green', 'blue']
colors_iter = iter(colors)

color = next(colors_iter)
print(color)