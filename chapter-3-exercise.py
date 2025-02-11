invite_list=["Eric","Scott","Mike"]
print( f"Hey {invite_list[0]}, I would like to invite you for the dinner")
print( f"Hey {invite_list[1]}, I would like to invite you for the dinner")
print( f"Hey {invite_list[2]}, I would like to invite you for the dinner")
print( f"Seems like  {invite_list[2]}can't make to the dinner")
invite_list[2]="Chris"
print("Updated invite list")
print( f"Hey {invite_list[0]}, I would like to invite you for the dinner")
print( f"Hey {invite_list[1]}, I would like to invite you for the dinner")
print( f"Hey {invite_list[2]}, I would like to invite you for the dinner")
invite_list.insert(0,"Matt")
invite_list.insert(1,"Luke")
invite_list.append("Mark")
print("Updated invite list")
print( f"Hey {invite_list[0]}, I would like to invite you for the dinner")
print( f"Hey {invite_list[1]}, I would like to invite you for the dinner")
print( f"Hey {invite_list[2]}, I would like to invite you for the dinner")
print( f"Hey {invite_list[3]}, I would like to invite you for the dinner")
print( f"Hey {invite_list[4]}, I would like to invite you for the dinner")
print( f"Hey {invite_list[5]}, I would like to invite you for the dinner")
print("Updated invite list")
print( f"Sorry {invite_list.pop()}, unfortunately the dinner plan has been changed")
print( f"Sorry {invite_list.pop()}, unfortunately the dinner plan has been changed")
print( f"Sorry {invite_list.pop()}, unfortunately the dinner plan has been changed")
print( f"Sorry {invite_list.pop()}, unfortunately the dinner plan has been changed")
del invite_list[0]
del invite_list[0]
print(invite_list)

places=["Japan","Russia","China","Switzerland","Germany"]
print(places)
print(sorted(places))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

print(len(places))

