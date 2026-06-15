##If else
##1.	Write a program to find the smallest number among two given integers.
##2.	Write a program to find the largest number among two given integers.
##3.	Write a program to find the absolute value of a given integer.
##4.	Check if a given number is even number or odd number
##5.	Determine whether the given number is a multiple of 5 or not.
##6.	Determine whether the given number is a multiple of 10 or not.
##7.	Check whether the given number is a two-digit number or not.
##8.	Check whether the given number is a three-digit number or not.
##9.	Check if a given number ends with zero or not.
##10.	Write a program to accept a number and check if its square is above 50 or below 50.
##11.	Write a program to accept two numbers, subtract the two numbers and check if the difference (answer) is 0 or not
##12.	Write a program to read the Computer Science marks of a student and print if the student has passed or failed. The student has passed if marks is 50 or above otherwise failed).
##13.	Write a program to accept a number and check if the number is divisible by 10.
##14.	Write a program to take a two-digit number and print the biggest digit.
##15.	Write a program to accept the choice from the user. If the choice is 1 print “The exam will be easy”, otherwise print “The exam will be difficult”.
##16.	Write a program to accept a value from the user. If the value entered is 1 then print “You can go out and play” otherwise “You cannot go out and play”
##17.	Write a program to accept the length and breadth of a shape and print if they are the same. If they are the same, print it’s a square otherwise its rectangle.
##
##18.	Check if a given number is the ASCII value of an uppercase alphabet or not.
##19.	Check if a given number is the ASCII value of a lowercase alphabet.
##20.	Check if a given number is the ASCII value of a numeric character or not.
##21.	Check whether the given number is a multiple of both 5 and 3.
##22.	Check if a given number is a three-digit number and also a multiple of 10.
##23.	Check if a given number is a three-digit number and also a multiple of 2, 5, and 10.
##24.	Check the given two integer inputs. If both numbers are even, find their product. Otherwise, find their sum.
##25.	A number is said to be Buzz Number if it ends with 7 or is divisible by 7. Example: 1007 is a Buzz Number. Define a class Buzz number to read a number and check if it is a Buzz number or not.





a, b = 10, 20
if a < b:
    print( a)
else:
    print( b)


if a > b:
    print( a)
else:
    print( b)


n = -15
if n < 0:
    print( -n)
else:
    print( n)


n = 15
if n % 2 == 0:
    print("Even")
else:
    print("Odd")


if n % 5 == 0:
    print("Multiple of 5")
else:
    print("Not multiple of 5")


if n % 10 == 0:
    print("Multiple of 10")
else:
    print("Not multiple of 10")


if 10 <= n <= 99:
    print("Two-digit")
else:
    print("Not two-digit")


if 100 <= n <= 999:
    print("Three-digit")
else:
    print("Not three-digit")


if n % 10 == 0:
    print("Ends with zero")
else:
    print("Does not end with zero")


n = 8
if n**2 > 50:
    print("Square above 50")
else:
    print("Square below 50")


x, y = 15, 15
diff = x - y
if diff == 0:
    print("Difference is 0")
else:
    print("Difference is not 0")


marks = 45
if marks >= 50:
    print("Pass")
else:
    print("Fail")


if n % 10 == 0:
    print("Divisible by 10")
else:
    print("Not divisible by 10")


num = 47
d1, d2 = num // 10, num % 10
if d1 > d2:
    print( d1)
else:
    print( d2)


choice = 1
if choice == 1:
    print("The exam will be easy")
else:
    print("The exam will be difficult")


val = 1
if val == 1:
    print("You can go out and play")
else:
    print("You cannot go out and play")


length, breadth = 5, 5
if length == breadth:
    print("Square")
else:
    print("Rectangle")


ch = 65
if 65 <= ch <= 90:
    print("Uppercase ASCII")
else:
    print("Not uppercase")


if 97 <= ch <= 122:
    print("Lowercase ASCII")
else:
    print("Not lowercase")


if 48 <= ch <= 57:
    print("Numeric ASCII")
else:
    print("Not numeric")


n = 15
if n % 5 == 0 and n % 3 == 0:
    print("Multiple of 5 and 3")
else:
    print("Not multiple of both")


n = 120
if 100 <= n <= 999 and n % 10 == 0:
    print("Three-digit and multiple of 10")
else:
    print("Condition not met")


if 100 <= n <= 999 and n % 2 == 0 and n % 5 == 0 and n % 10 == 0:
    print("Three-digit and multiple of 2,5,10")
else:
    print("Condition not met")


a, b = 4, 7
if a % 2 == 0 and b % 2 == 0:
    print( a * b)
else:
    print( a + b)


class Buzz:
    def __init__(self, num):
        self.num = num

    def check(self):
        if self.num % 10 == 7 or self.num % 7 == 0:
            print(self.num, )
        else:
            print(self.num, )

obj = Buzz(1007)
obj.check()
