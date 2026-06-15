##Write a Python program to create a tuple with different data types.
##
##Write a Python program to create a tuple of numbers and print one item.
##
##Write a Python program to unpack a tuple into several variables.
##
##Write a Python program to add an item to a tuple.
##
##Write a Python program to find the index of an item in a tuple.
##
##Write a Python program to find the length of a tuple.
##
##Write a Python program to reverse a tuple.
##
##Write a Python program to find repeated items in a tuple.
##
##Write a Python program to calculate the product, multiplying all the numbers in a given tuple. Original Tuple: (4, 3, 2, 2, -1, 18)
##
##Product - multiplying all the numbers of the said tuple: -864




t = ("Hello", 25, 3.14, True)
print(t)


numbers = (10, 20, 30, 40)
print(numbers[2])  


t = ("Python", 3.9, "Tuple")
a, b, c = t
print(a)
print(b)
print(c)


t = (1, 2, 3)
t = t + (4,)
print(t)


t = ("a", "b", "c", "d")
print(t.index("c"))


t = (10, 20, 30, 40, 50)
print(len(t))


t = (1, 2, 3, 4, 5)
print(t[::-1])

t = (1, 2, 3, 2, 4, 1, 5, 1)
for item in set(t):
    if t.count(item) > 1:
        print(item,  t.count(item))


t = (4, 3, 2, 2, -1, 18)
product = 1
for num in t:
    product *= num
print("Product:", product)


t = (4, 3, 2, 2, -1, 18)
p = 1
for num in t:
    p *= num
print( t)
print( p)  
