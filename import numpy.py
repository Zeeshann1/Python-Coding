import numpy as np

x = 3
n = 'name'
y = 'c'
print(x, n [2:], y)

listt = [2,6,89,67,51,75]
print(min(listt), max(listt), sum(listt))

set = (2,4,5,6,66,)
print(set)
print(set[1])

arr = np.array([1,2,4])
print(arr+2)

x = 2

if x == 4:
    print(x, 'is less than 4')
else:
    print('greater')
    
    
my_list = list(range(4, 10))
print(my_list)

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)


count = 0

while count < 5:
    print(count, 'is less than five')
    count += 1

for i in range(5):   
    print (i)       


# Number Swip
a = 7
b = 88
a,b = b, a
print('Number Swip: ',a,b)


# Reverse Charaters
namey = "ABCDE"
for char in reversed(namey):
  print(char)

z = namey[::-1] 
print("Reverse Charaters",z)

# Reverse List
name = ['HK', 'lOVE', 'I']
print ('Reverse List',' '.join(reversed(name)))


# Reserve Number
numbers = 1234
print(numbers)
numlist = list(str(numbers))
print (' '.join(reversed(numlist)))

# String Reverse Sentence
input = 'Hyder Zeeshan'
rev_abc = input.split(' ')
print(rev_abc)
print(' '.join(reversed(rev_abc)))








