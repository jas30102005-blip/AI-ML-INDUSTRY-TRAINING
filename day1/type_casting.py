# str -> int
# x = int("42") # x = 42


# int -> float
# y = float(10) # y = 10.0


# int -> str
# z = str(100) # z = "100"


# int() → Converts to integer
# float() → Converts to float
# str() → Converts to string
# bool() → Converts to boolean




# Convert String to Integer
num = "10"
x = int(num)

print(x)
print(type(x))



#Convert Integer to Float
a = 5
b = float(a)

print(b)
print(type(b))




#Convert Number to String
age = 21
text = str(age)

print(text)
print(type(text))


#Convert Integer to Boolean
x = 1
print(bool(x))

y = 0
print(bool(y))



#Implicit Type Casting (Automatic)
#Python converts the data type automatically when needed.
a = 5
b = 2.5

c = a + b
print(c)
print(type(c))


# Explicit Type Casting (Manual)
# The programmer converts the data type using functions like int(), float(), or str()
x = "25"
y = int(x)

print(y + 5)