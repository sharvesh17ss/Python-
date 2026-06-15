##Write a Python program to insert items into a list in sorted order.
##
##Write a Python program to sum all the items in a list.
##
##Write a Python program to get the largest number from a list.
##
##Write a Python program to remove duplicates from a list.
##
##Write a Python program to clone or copy a list.
##
##Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
##Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
##
##Write a Python program to print the numbers of a specified list after removing even numbers from it.
##
##Write a Python program to access the index of a list.
##
##Write a Python program to append a list to the second list.
##
##Write a Python program to get unique values from a list.
##
##Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.
##Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##
##Write a Python program to reverse strings in a given list of string values.
##Original list: ['Red', 'Green', 'Blue', 'White', 'Black']
##
##Write a Python program to remove words from a given list of strings containing a character or string.
##Original list: ['Red color', 'Orange#', 'Green', 'Orange @', 'White']


lst = [25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
print( lst)
lst.sort()
print(lst)


lst = [1, 2, 3, 4, 5]
print( sum(lst))



lst = [1, 2, 3, 4, 5]
print( max(lst))



lst = [1, 2, 2, 3, 4, 4, 5]
u = list(dict.fromkeys(lst))
print( u)


lst = [1, 2, 3]
cl = lst.copy()
print(cl)

##
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print( colors)

del colors[0]   
del colors[3]   
del colors[3]   

print( colors)

##
nums = [1, 2, 3, 4, 5, 6, 7]
f = [x for x in nums if x % 2 != 0]
print(f)



lst = ['a', 'b', 'c']
for i in range(len(lst)):
    print( i, lst[i])




list1 = [1, 2, 3]
list2 = [4, 5]
list1.extend(list2)
print( list1)


lst = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(lst))
print( unique)



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
diffs = [lst[i+1] - lst[i] for i in range(len(lst)-1)]
print( diffs)




lst = ['Red', 'Green', 'Blue', 'White', 'Black']
rev = [s[::-1] for s in lst]
print( rev)




list1 = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
f = [w for w in list1 if '#' not in w and '@' not in w]
print(f)




















