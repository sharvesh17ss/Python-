##Write a Python program to remove item(s) from a given set.
##
##Write a Python program to remove an item from a set if it is present in the set.
##
##Write a Python program to create set difference.
##
##Write a Python program to remove all elements from a given set.
##
##Write a Python program to find the maximum and minimum values in a set.



s = {1, 2, 3, 4, 5}
s.remove(3)   
print(s)


s = {10, 20, 30, 40}
s.discard(20)   
print(s)


set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1 - set2)   


s = {100, 200, 300}
s.clear()
print(s)




s = {5, 10, 25, 3, 18}
print(max(s))
print( min(s))
