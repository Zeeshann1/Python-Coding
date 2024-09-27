#import numpy as np

#01 Pattern
for num in range(6, 0, -1):
    for i in range(num):
        print("*", end =" ")
    print(" ")


#02 reserve number
n = 123
n = str(n)
n= n[::-1]
n = int(n)
print(n, type(n))


#03 Convert decimal to binary
decimal_number = 42
binary_representation = bin(decimal_number)[2:]
print("Decimal as binary:", binary_representation)  # Output: '101010'


#04 count number of digits
n =  123
n = str(n)
print("num of digits = ", len(n))

#05 display -10 to -1  numbers

for i in range(10, 0, -1):
    print(-i)


#06 Print prime numbers in certain range
print("prime numbers")
count = 0

for i in range (20, 100):
   #if i > 1:
     for j in range(2, i):
         if (i % j) == 0:
             break
     else:
      if count < 10:
       print(i)
       count += 1

#07 Print Even number in the certain number range #arr = [1,2,3,4,5,6,7,8,9,10]
even = []
for i in range(1,30):
   if i%2 == 0:
      even.append(i)

print("list of Even numbers" , even)

#08 Fibonacci  [1,2,3,5]
n1, n2 = 1, 2
print("Fibonacci:", end = " ")
for i in range(1, 10):
   
   print(n1, end = " ")
   nth = n1 + n2
   n1 = n2
   n2 = nth

#09 Factorial 5! = 5x4x3x2x1
res = 1 
print()
for i in range(1,6):
   res = res * i
print("Factorial =", res)
   
   
#10 Cube
print("Cube = ", end = " ")
n = 5
for i in range(1, 6):
    cube = i*i*i
    print(cube, end = ' ')
print(" ")

#11 Print series sum 1+2+3+4
n = 4
res = 0
for i in range(1,n+1):
   res = res + i
print(res)


#12 print two table
print("Table of Two")
for i in range (1, 11, 1):
   print(i*2,  end = ' ')

print(" ")

#13 Display pattern
for i in range(0, 6):
    for j in range (0, i, 1):
     print(j, end = '')
    print("")

for i in range(0, 5):
    for j in range (4-i, 0, -1):
     print(j, end = '')
    print("")


#14 Print Pattern
print("Print Pattern")
for i in range(0, 6):
    for j in range (5-i, 0 , -1):
     print(j, end = ' ')
    print("")

#15 Draw a pattern

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

#16 Print number pattern
for i in range(1, 5, 1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print("")

#17 Print multiplication table from 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")

#18 #09 Check Palindrome Number
n = 181181


#19 Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

i = 0
for i in range(10):

    print("current number is", i) 
    if i == 0:
      pn = 0
    else:
        pn = i-1
    print("previous number is", pn)
    
    sum = (i) + pn
    print("sum is", sum)
    i+1

#20 Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def solution(num1, num2):
  product = num1*num2
  sum = num1+num2
  if product <= 1000:
      return product
  else:
      return sum
  
#num1 = int(input("Input Number 1: "))
#num2 = int(input("Input Number 2: "))
#print(solution(num1, num2))
print(solution(20,30))

#21 Display numbers divisible by 5 from a list

def division(numlist):
    for num in numlist:
        if num % 5 == 0:
            print(num)

print(division([10, 20, 30, 40, 11]))



#22 Check if the first and last number of a list is the same

def numbers(numbers_x):
    if numbers_x [0] == numbers_x [4]:
     return True
    else:
        return False

print(numbers([10, 20, 30, 40, 11]))


#23 Add two binaries
a = "1010"
b = "1011"

deci_a = int(a, 2)
print(deci_a)

deci_b = int(b, 2)
print(deci_b)

res = deci_a + deci_b
print(res)
print(bin(res)[2:]) 

