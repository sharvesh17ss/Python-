

##RECURSION
##
##Recursive function to find sum of n numbers.
##
##Recursive function to find factorial.
##
##Recursive function to print numbers from 1 to n.
##
##Recursive function to print numbers from n to 1.
##
##Recursive function to find power (xⁿ).
##
##Recursive function to find GCD.
##
##Recursive function to find LCM.
##
##Recursive function to calculate sum of digits.
##
##Recursive function to reverse string.
##
##Recursive function to reverse number.
##
##Recursive function to check palindrome number.
##
##Recursive function to check palindrome string.
##
##Recursive function to find Fibonacci series.
##
##Recursive function to count digits in number.
##
##Recursive function to find maximum element in list.
##
##Recursive function to find minimum element in list.
##
##Recursive function to remove all spaces in string.
##
##Recursive function to count vowels in string.
##
##Recursive function to check prime number.
##
##Recursive function to calculate sum of list elements.






def sn(n):
    if n == 0:
        return 0
    return n + sn(n-1)
print(sn(10))

def f(n):
    if n <= 1:
        return 1
    return n * f(n-1)
print(f(5))

def nu(n):
    if n == 0:
        return
    nu(n-1)
    print(n)
nu(5)

def n1(n):
    if n == 0:
        return
    print(n)
    n1(n-1)
n1(5)

def p(x, n):
    if n == 0:
        return 1
    return x * p(x, n-1)
print(p(2, 5))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
print(gcd(48, 18))

def lcm(a, b):
    return a * b // gcd(a, b)
print(lcm(12, 15))

def sd(n):
    if n == 0:
        return 0
    return n % 10 + sd(n // 10)
print(sd(1234))

def rs(s):
    if len(s) == 0:
        return ""
    return rs(s[1:]) + s[0]

print(rs("hello"))



def rn(n, rev=0):
    if n == 0:
        return rev
    return rn(n // 10, rev*10 + n % 10)
print(rn(1234))



def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)
print([f(i) for i in range(10)])

def cd(n):
    if n == 0:
        return 0
    return 1 + cd(n // 10)
print(cd(12345))






def cv(s):
    if s == "":   
        return 0
    
    return (s[0].lower() in "aeiou") + cv(s[1:])

print(cv("hello world"))


def p(n, i=2):
    if n <= 1:
        return False
    if i*i > n:
        return True
    if n % i == 0:
        return False
    return p(n, i+1)
print(p(29))

def sl(lst):
   
    if len(lst) == 0:
        return 0
    else:
        return max(lst)
print(sl([1, 2, 3, 4, 5]))

