##If elif else
##
##1.	Find the largest number among three integers.
##2.	Find the smallest number among three integers.
##3.	Check if a given number is greater than 0, if yes then print 'Positive'. If the given number is lesser than 0, then print 'Negative'. If the given number is exactly equal to 0, then print 'Zero'.
##4.	A library charges fine for books returned late. To calculate the fine, define a class Library with the following .To input the number of days books were returned late. To calculate and print the fine based on the following condition:
##a.	First five days 40 paisa per day 
##b.	Six to ten days 65 paisa per day 
##c.	above 10 days 80 paisa per day
##5.	Write a Java program that functions as a basic calculator. The program will prompt the user to input two numbers and a mathematical operation (+, -, x, /). It will then perform the selected operation and display the result on the screen.
##6.	Check whether the given number is a multiple of 5, 3, and 7.
##7.	To input weight of the parcel and type of booking (`O' for ordinary and 'E' for express).To compute and display the charges based on the weight of the parcel as per the tariff given 
## 
##8.	Write a program to compute the discount according to the given conditions for the purchase of laptop. to take the price of the laptop.to calculate the charge according to the following condition.
## 
##Display the output as per the given format:
##Price of laptop : 
##Discount : 
##Total Price :








a, b, c = 10, 25, 15
if a >= b and a >= c:
    print( a)
elif b >= a and b >= c:
    print( b)
else:
    print( c)


if a <= b and a <= c:
    print( a)
elif b <= a and b <= c:
    print( b)
else:
    print( c)


n = 0
if n > 0:
    print("positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


class Library:
    def __init__(self, days):
        self.days = days

    def fine(self):
        if self.days <= 5:
            return self.days * 0.40
        elif self.days <= 10:
            return self.days * 0.65
        else:
            return self.days * 0.80

days_late = 7
lib = Library(days_late)
print("Fine:", lib.fine(), "Rs")


x, y, op = 10, 5, "+"
if op == "+":
    print( x + y)
elif op == "-":
    print( x - y)
elif op == "x":
    print( x * y)
elif op == "/":
    print( x / y)
else:
    print("Invalid operation")


n = 105
if n % 5 == 0 and n % 3 == 0 and n % 7 == 0:
    print(n, "is a multiple of 5, 3, and 7")
else:
    print(n, "is not a multiple of 5, 3, and 7")


weight, booking = 12, 'E'  
if booking == 'O':
    if weight <= 5:
        charge = weight * 10
    elif weight <= 10:
        charge = weight * 8
    else:
        charge = weight * 7
elif booking == 'E':
    if weight <= 5:
        charge = weight * 15
    elif weight <= 10:
        charge = weight * 12
    else:
        charge = weight * 10
else:
    charge = 0
print("Parcel charge:", charge, "Rs")


price = 60000
if price < 30000:
    discount = price * 0.05
elif price <= 50000:
    discount = price * 0.10
else:
    discount = price * 0.15

total = price - discount
print( price)
print( discount)
print( total)
