##pattern



def square_hollow(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
square_hollow(5)

def number_triangular(n):
    for i in range(2, n + 2):
        for j in range(i - 1):
            print(i, end=" ")
        print()
    print()
number_triangular(4)

def number_increasing_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    print()
number_increasing_pyramid(4)

def number_increasing_reverse_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    print()
number_increasing_reverse_pyramid(4)

def number_changing_pyramid(n):
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()
    print()
number_changing_pyramid(4)

def zero_one_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print((i + j) % 2, end=" ")
        print()
    print()
zero_one_triangle(4)

def palindrome_triangular(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(i, 0, -1):
            print(j, end=" ")
        for j in range(2, i + 1):
            print(j, end=" ")
        print()
    print()
palindrome_triangular(4)

def rhombus(n):
    for i in range(n):
        print(" " * (n - i) + "* " * n)
    print()
rhombus(5)

def diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)
    print()
diamond(3)

def butterfly(n):
    for i in range(1, n + 1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)
    for i in range(n, 0, -1):
        print("*" * i + " " * (2 * (n - i)) + "*" * i)
    print()
butterfly(5)

def square_fill(n):
    for i in range(n):
        print("* " * n)
    print()
square_fill(5)

def right_half(n):
    for i in range(1, n + 1):
        print("* " * i)
    print()
right_half(5)

def reverse_right_half(n):
    for i in range(n, 0, -1):
        print("* " * i)
    print()
reverse_right_half(5)

def left_half(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print()
left_half(5)

def reverse_left_half(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)
    print()
reverse_left_half(5)

def k_pattern(n):
    for i in range(n):
        for j in range(n):
            if j == 0 or i == j or i + j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
k_pattern(5)

def triangle_star(n):
    for i in range(1, n + 1):
        print("* " * i)
    print()
triangle_star(5)

def reverse_number_triangle(n):
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print()
    print()
reverse_number_triangle(4)

def mirror_image_triangle(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    print()
mirror_image_triangle(4)

def hollow_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
hollow_triangle(5)

def hollow_reverse_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            if j == 1 or j == i or i == n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()
hollow_reverse_triangle(5)

def hollow_diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print()
hollow_diamond(3)

def hollow_hourglass(n):
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i in range(2, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, 2 * i):
            if j == 1 or j == 2 * i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print()
hollow_hourglass(4)

def pascal(n):
    for i in range(n):
        print(" " * (n - i), end="")
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()
    print()
pascal(5)

def right_pascal(n):
    for i in range(1, n + 1):
        print("* " * i)
    for i in range(n - 1, 0, -1):
        print("* " * i)
    print()
right_pascal(5)


