magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

#range
for value in range(1,6):
    print(value)

#range with step
print("Even numbers")
even_numbers=range(2,11,2)
for value in even_numbers:
    print(value)

squares=[]

#list append
for value in range(1,11):
    square=value ** 2
    squares.append(square)

print(squares)

#aggregate functions
print(min(squares))
print(max(squares))
print(sum(squares))

#list comprehension
squares=[ value ** 2 for value in range(1,11)]
print(squares)

#slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

#list copying
print("Here are the first three players of my team")
for player in players[:3]:
    print(player)

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food=my_foods[:]

print("My favorit foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

my_foods.append("cannoli")
friends_food.append("ice cream")

print("My favorit foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)


my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food=my_foods

print("My favorit foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

my_foods.append("cannoli")
friends_food.append("ice cream")

print("My favorit foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friends_food)

#tuple
dimensions= (200,50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


