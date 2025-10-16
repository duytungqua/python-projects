bonuses = [100, 200, 300]
def apply_bonus(bonus):
    return bonus * 1.1
iterator = map(apply_bonus, bonuses)

# Convert the map object to a list to see the results
updated_bonuses = list(iterator)
for row in matrix:
    for value in row:
        print(value)
for updated_bonus in updated_bonuses:
    print("Updated Bonus:", updated_bonus)
    for value in row:
        print(value)
# Using map to transform a list
bonuses = [100, 200, 300]
def apply_bonus(bonus):
    return bonus * 1.1
iterator = map(apply_bonus, bonuses)    

#tuple
points = (1, 2, 3)
def double_point(point):
    return point * 2
points_iterator = map(double_point, points)
updated_points = list(points_iterator)
for updated_point in updated_points:
    print("Updated Point:", updated_point)
# Using map to transform a list