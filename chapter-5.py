cars=["audi","bmw","subaru","toyota"]

for car in cars:
    if car.lower()=="bmw":
        print(car.upper())
    else:
        print(car.title())

requested_toppings="mushrooms"

if requested_toppings != "anchovies":
    print("Hold the anchovies")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']

if "mushrooms" in requested_toppings:
    print("Available")

banned_users = ['andrew', 'carolina', 'david']
user ="marie"

if user not in banned_users:
    print(f"{user.title()}! You are allowed to post if you wish.")

age=16

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, You are not old enough to vote")

if age <4:
    print("You admission cost is $0")
elif age <18:
    print("You admission cost is $25")
else:
    print("You admission cost is $40")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping =="green peppers":
        print("Sorry, we are out of green peppers right now!")
    else:
        print(f"Adding {requested_topping}")


available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"{requested_topping} is not available")