cars=["audi","bmw","subaru","toyota"]

car="toyota"
print("Is car=='toyota' ? I predict True")
print(car=="toyota")
print("Is car=='bmw' ? I predict False")
print(car=="bmw")

car="Audi"
print("Is car=='audi' ? I predict False")
print(car=="audi")
print("Is car.lower()=='audi' ? I predict True")
print(car.lower()=="audi")


alien_color=["green","yellow","red"]
for color in alien_color:
    if color=="green":
        print("You have earned 5 points")
    elif color=="yellow":
        print("You have earned 10 points")
    elif color=="red":
        print("You have earned 15 points")

age=20

if age <2:
    print("The person is baby")
elif age >=2 and age <4:
    print("The person is toddler")
elif age >=4 and age <13:
    print("The person is kid")
elif age >=13 and age <20:
    print("The person is teenager")
elif age >=20 and age <65:
    print("The person is adult")
elif age >=65:
    print("The person is elder")


username =["scott","matt","eric","admin"]

for user in username:
    if user =="admin":
        print(f"Hello {user}, would you like to see the status report?")
    else:
        print(f"Hello {user}, thank you for logging back")

usernames=[]
if not usernames:
    print("We need to find some users")

current_users=["matt","simon","scott","chris"]
new_users=["scott","chris","luke","ben","david"]

for user in new_users:
    if user in current_users:
        print(f"{user}, you need to enter a new username")
    else:
        print(f"{user}, username is available")

