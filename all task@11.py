##Create a function to check whether a number is prime.
##
##Function to find maximum of 3 numbers.
##
##Function to swap two numbers (without temp).
##
##Function to count vowels in a string.
##
##Function to check palindrome string.
##
##Function to calculate simple interest.
##
##Function to find factorial of a number.
##
##Function to return sum of even numbers in a list.
##
##Function to convert Celsius to Fahrenheit.
##
##Function to check Armstrong number.
##
##Function to remove duplicate elements from list.
##
##Function to find second largest number in list.
##
##Function to check perfect number.
##
##Function to generate n Fibonacci numbers.
##
##Function to calculate power (xⁿ) without using **.
##
##Function to count words in a sentence.
##
##Function to validate email format.
##
##Function to find LCM of two numbers.
##
##Function to find GCD of two numbers.
##
##Function to simulate bank deposit & withdrawal.
##








##

def p(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(p(29))

##

def biggest(a, b, c):
    return max(a, b, c)

print(biggest(10, 20, 15)) 


##
def swap(a, b):
    a, b = b, a
    return a, b

print(swap(5, 7))  


##
s = input('enter a word')

def cv(s):
    v = "aeiou"
    c = 0
    for char in s.lower():  
        if char in v:
            c += 1
    return c

print(cv(s))

##

def P(s):
    return s == s[::-1]

print(P("madam"))


##

def st(p, r, t):
    return (p * r * t) / 100

print(st(1000, 5, 2))  


##

def f(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

print(f(5)) 

##

def seven(lst):
    t = 0                
    for x in lst:            
        if x % 2 == 0:       
            t = t + x  
    return t

print(seven([1,2,3,4,5,6]))

##

def cf(c):
    return (c * 9/5) + 32

print(cf(0))

##



def is_armstrong(n):
   
    s = str(n)

    
    length = 0
    for _ in s:
        length += 1

    
    total = 0
    for ch in s:
        digit = int(ch)

        
        pv = 1
        for _ in range(length):
            pv *= digit

        total += pv

    
    return total == n



num = 153
if is_armstrong(num):
    print(num)
else:
    print(num)




##

def rd(lst):
    return list(set(lst))

print(rd([1,2,2,3,4,4]))

##

def sl(lst):
    u = list(set(lst))
    u.sort()
    return u[-2] if len(u) > 1 else None

print(sl([10, 20, 4, 20]))


##

def per(n):
    t = 0
    for i in range(1, n):       
        if n % i == 0:           
            t = t + i   
    return t == n

print(per(28))  


##

def fibonacci(n):
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print(fibonacci(7))  



##

def pow(x, n):
    r = 1
    for _ in range(n):
        r *= x
    return r

print(pow(2, 5))   


##


def cw(sentence):
    return len(sentence.split())

print(cw("Hello world from Python"))   

##

def lcm(a, b):
    from math import gcd
    return abs(a*b) // gcd(a, b)

print(lcm(12, 15))   

##

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(12, 15)) 


