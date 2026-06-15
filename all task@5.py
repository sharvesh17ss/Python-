##1. WriteaprogramtoprintthefirstNnaturalnumbers.Input:10,Output:12345 678910
##2. WriteaprogramtoprintthefirstNevennaturalnumbers.Input:5,Output246 810
##3. WriteaprogramtoprintthefirstNoddnaturalnumbers.Input:5,Output:135 79
##4. WriteaprogramtoprintfirstNmultiplesof3.Input:7,Output:36912151821
##5. WriteaprogramtoprintfirstNmultiplesof5.Input:5,Output:510152025
##6. Writeaprogramtoprintallthemultiplesof2tillN.Input:15,Output:246810 1214
##7. Writeaprogramtoprintallthenumberswhicharemultiplesofeither2or3tillN. Input:15,Output:23468910121415
##8. Writeaprogramtoprintallthenumberswhicharemultiplesofeither2,5or7till N.Input:15,Output:24567810121415
##9. WriteaprogramtoprintthefirstNmultiplesofeither3,5or7.Input:10,Output: 356791012141518
##10.Findthesumofalldigitsinapositiveinteger.Input:123456789,Output:45
##11.Countthenumberofdigitsinapositiveinteger.Input:123456789,Output:9
##12.Writeaprogramtofindfactorsofagivennumber.Input:20,Output:124510 20
##13.Writeaprogramtocountfactorsofagivennumber.Input:20,Output:6
##14.Writeaprogramtofindwhetherthegivennumberisaprimenumberornot.Input :11,Output:Yes
##15.Printallprimenumbersfrom2uptoandincluding'n'.Input:15,Output:2357 1113
##16.Writeaprogramtofindthegreatestcommonfactorofgiven2integers.Input: 1020,Output:10
##17.Printthecommonfactorsoftwopositiveintegersnandm.Input:812,Output: 124
##18.WriteaprogramtogettheFibonacciseriesbetween0to50.
##19.Writeaprogramtofindthefactorialofagivennumbe
##20.Writeaprogramthatreadsasetofintegers,andthenprintsthesumoftheeven andoddintegers.
##21.Writeaprogramtocheckwhetherthegivennumberispalindromeornot. Palindromeisanumberwhenreverseditgivesthesamenumber.Example1:If thenumberis121Reverseis121Hence,121isaPalindromeExample2:Ifthe numberis438Reverseis834Hence,438isnotaPalindrome
##22.WriteaprogramtoprintifanumberisanArmstrongnumberornot.153isan Armstrongnumber.13+53+33=153.




N = 10
for i in range(1, N+1):
    print(i, end=" ")
print()


N = 5
for i in range(1, N+1):
    print(2*i, end=" ")
print()


N = 5
for i in range(1, N+1):
    print(2*i-1, end=" ")
print()


N = 7
for i in range(1, N+1):
    print(3*i, end=" ")
print()


N = 5
for i in range(1, N+1):
    print(5*i, end=" ")
print()


N = 15
for i in range(2, N+1, 2):
    print(i, end=" ")
print()


N = 15
for i in range(1, N+1):
    if i % 2 == 0 or i % 3 == 0:
        print(i, end=" ")
print()


N = 15
for i in range(1, N+1):
    if i % 2 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
print()


N = 10
count, num = 0, 1
while count < N:
    if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
        print(num, end=" ")
        count += 1
    num += 1
print()


num = 123456789
s = 0
for d in str(num):
    s += int(d)
print( s)


num = 123456789
print( len(str(num)))


num = 20
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=" ")
print()


num = 20
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1
print( count)


num = 11
is_prime = True
for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        is_prime = False
        break
print( "Yes" if is_prime else "No")


n = 15
for num in range(2, n+1):
    prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
print()


a, b = 10, 20
while b:
    a, b = b, a % b
print( a)


n, m = 8, 12
for i in range(1, min(n, m)+1):
    if n % i == 0 and m % i == 0:
        print(i, end=" ")
print()


a, b = 0, 1
while a <= 50:
    print(a, end=" ")
    a, b = b, a+b
print()


num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print( fact)


nums = [1,2,3,4,5,6,7,8,9,10]
es = sum(x for x in nums if x % 2 == 0)
os = sum(x for x in nums if x % 2 != 0)
print( es,  os)


num = 121
if str(num) == str(num)[::-1]:
    print(num)
else:
    print(num)


num = 153
s = sum(int(d)**3 for d in str(num))
if s == num:
    print(num)
else:
    print(num)

