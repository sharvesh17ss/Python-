##Write a Python script to add a key to a dictionary.
##
##Write a Python script to concatenate the following dictionaries to create a new one.
##Sample Dictionary : Dic1={1:10, 2:20} Dic2={3:30, 4:40} Dic3={5:50,6:60}
##
##Write a Python program to iterate over dictionaries using for loops.
##
##Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
##Sample Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
##
##Write a Python script to merge two Python dictionaries.
##
##Write a Python program to sum all the values in a dictionary.
##
##Write a Python program to map two lists into a dictionary.
##
##Write a Python program to remove duplicates from the dictionary.
##
##Write a Python program to get the key, value and item in a dictionary.





d = {1: 10, 2: 20}
d[3] = 30
print(d)


Dic1 = {1: 10, 2: 20}
Dic2 = {3: 30, 4: 40}
Dic3 = {5: 50, 6: 60}
nd = {}
for d in (Dic1, Dic2, Dic3):
    nd.update(d)
print(nd)


d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print(key, d[key])


squares = {}
for i in range(1, 16):
    squares[i] = i * i
print(squares)


d1 = {"x": 1, "y": 2}
d2 = {"z": 3}
d1.update(d2)
print(d1)


d = {"a": 10, "b": 20, "c": 30}
print(sum(d.values()))


keys = ["a", "b", "c"]
values = [1, 2, 3]
mapped = dict(zip(keys, values))
print(mapped)


d = {"a": 1, "b": 2, "c": 1}
unique = {}
for k, v in d.items():
    if v not in unique.values():
        unique[k] = v
print(unique)


d = {"name": "M", "age": 21}
print( d.keys())
print( d.values())
print( d.items())
