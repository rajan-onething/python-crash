#accessing list by index
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[1].title())
print(f"My first bike was {bicycles[0]}.")

#changing list item
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0]="ducati"
print(motorcycles)

#appending list item
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append("ducati")
print(motorcycles)

#inserting list item
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,"ducati")
print(motorcycles)

#deleting list item
del motorcycles[0]
print(motorcycles)

#inserting list item
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,"ducati")

#popping list
last_owned=motorcycles.pop()
print(f"The last motorcycle I owned was {last_owned.title()}")

#popping any item in list
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned=motorcycles.pop(0)
print(f"The first motorcycle I owned was {last_owned.title()}")

#removing list item by name
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove("ducati")
print(motorcycles)

#sorting list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
cars.sort()
print(cars)

#reversing list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
