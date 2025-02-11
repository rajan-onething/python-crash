message="Hello World Python Reader"
print(message)

#String methods
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#Format Strings
first_name="ada"
last_name="lovalace"
full_name=f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#Strip functions
favorite_language=" python"
print(favorite_language.lstrip())
favorite_language="python  "
print(favorite_language.rstrip())
favorite_language=" python   "
print(favorite_language.strip())

num1=1_0_2222_3_4_0
print(num1)
print(10+10)
print(10-10)
print(10*10)
print(10/10)
print(2**3)

x,y,z=10,20,30
print(x,y,z)