pizzas=["chesse-pizza","veg-pizza","chicken-pizza"]
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"I like {pizza}")
print("I like all these pizzas")

animals=["dog","cat","rabbit"]
for animal in animals:
    print(f"{animal} is a great pet")
print("Any of these would make a great pet")

for value in range(1,21):
    print(value)

#list from range
numbers =list(range(1,1000001))
for value in numbers:
    print(value)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers=list(range(1,20,2))
for value in odd_numbers:
    print(value)

multiple_three=list(range(3,30,3))
for value in multiple_three:
    print(value)

#list comprehension
cubes=[ value**3 for value in range(1,11)]

for value in cubes:
    print(value)

print(f"The first three odd numbers are {odd_numbers[:3]}")
print(f"The middle three odd numbers are {odd_numbers[2:5]}")
print(f"The las three odd numbers are {odd_numbers[7:]}")

#tuple
buffet=("pizza","burger","chips","ice cream","chicken wings")
for food in buffet:
    print(food)