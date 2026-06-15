##Count the number of characters in a string (without using len()).
##Count vowels and consonants in a string.
##Reverse a string without using slicing.
##Check whether a string is empty or not.
##Convert all lowercase letters to uppercase without using upper().
##Count how many times a given character appears in a string.
##Remove spaces from a string.
##Find the first and last character of a string
##Check whether a string is a palindrome.
##Count the number of words in a string.
##Find the longest word in a sentence.
##Replace all vowels with *.
##Check whether two strings are anagrams.
##Remove duplicate characters from a string.
##Find all duplicate characters in a string.
##Reverse each word in a sentence (not the full string).
##Check whether a string contains only digits.
##Find the index of a substring without using find().







s = "hello"
count = 0
for _ in s:
    count += 1
print( count)


s = "hello world"
vowels = "aeiouAEIOU"
v_count = c_count = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1
print( v_count, c_count)


s = "python"
rev = ""
for ch in s:
    rev = ch + rev
print( rev)


s = ""
if s == "":
    print("Empty string")
else:
    print("Not empty")


s = "hello"
result = ""
for ch in s:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch
print(result)


s = "banana"
char = "a"
count = 0
for ch in s:
    if ch == char:
        count += 1
print( count)


s = "hello world python"
ns = ""
for ch in s:
    if ch != " ":
        ns += ch
print(ns)


s = "python"
print( s[0],  s[-1])


s = "madam"
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not palindrome")


s = "hello world python"
words = s.split()
print( len(words))


s = "I love programming in python"
words = s.split()
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print( longest)


s = "hello world"
vowels = "aeiouAEIOU"
result = ""
for ch in s:
    if ch in vowels:
        result += "*"
    else:
        result += ch
print(result)


s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not anagram")


s = "programming"
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(result)


s = "programming"
seen = []
dup = []
for ch in s:
    if ch in seen and ch not in dup:
        dup.append(ch)
    else:
        seen.append(ch)
print( dup)


s = "hello world python"
words = s.split()
rw = []
for w in words:
    rev = ""
    for ch in w:
        rev = ch + rev
    rw.append(rev)
print(" ".join(rw))


s = "12345"
only_digits = True
for ch in s:
    if not ch.isdigit():
        only_digits = False
        break
print("Only digits:", only_digits)


s = "hello world"
sub = "world"
found = -1
for i in range(len(s) - len(sub) + 1):
    if s[i:i+len(sub)] == sub:
        found = i
        break
print( found)
