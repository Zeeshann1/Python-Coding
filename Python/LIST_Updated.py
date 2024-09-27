import numpy as np

#01  List (insert,remove, reverse,max, min, sorted )
arr = [2,1,3,4]
print("Original Aarray", arr)
arr.insert(1,5)
print("Array After Insert",arr)
arr.remove(5)
print("Array after element", arr)
arr.reverse()
print("Reversed Array: ",arr)
print("Length of Array:", len(arr))
print("MAX VALUE: ", max(arr))
print("MIN VALUE: ",min(arr))
print("Sorted Array ",sorted(arr))
print("Sorted Array ",arr.sort())


#02 Sum of elements of given List
list1 = [1, 4, 2, 9, 7, 8, 9, 3, 1]
sum = 0
for i in list1:
    sum += i
print("Sum of Given List =", sum)

#03 find duplicate elements in the array
arr = [1,2,3,4,4,3,3]
res = []
duplicate = []

for i in arr:
    if i not in res:
        res.append(i)
    else:
        duplicate.append(i)
print(duplicate)

#04 Finding the missing element in the array
arr = np.array([1,2,3,4,5,7])
sum_arr = np.sum(arr)
count = 0
for i in range(0, len(arr)+2):
    count += i

missing = count - sum_arr
print("missing value", missing)


#05 Find 2nd max value in the array
arr = [1, 2, 3, 4, 5, 6, 7, 3, 2, 8, 9, 9, 10]
m = max(arr)
arr.remove(m)
print(arr)

for i in arr[::-1]:
    if i < m:
        m2 = i
        break
print("2nd max element in array:", m2)


#06 print list using loop  (Tthree conditions)
numbers = [12, 75, 150, 180, 145, 525, 50]
print(" Numbers After Conditions ")
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i, end = ' ')

print(" ")


#07 Print list in reverse order using a loop
list1 =  [10, 20, 30, 40, 50]
l = len(list1) 
for i in range(1, l+1):
    print(list1[-i], end = " ")

#08 Use a loop to display elements from a given list present at odd index positions
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1, len(my_list), 2):
    print(my_list[i], end = ' ')        
        

#09 Sort Odd Even Array
print("Sort Odd Even Array")
arr = [1, 2, 3, 4, 5, 6, 7, 3, 2, 8, 9, 9, 10]
even = []
odd = []
for i in arr:
   if i%2 == 0:
     even.append(i)
   else:
      odd.append(i)

odd.reverse()
result = odd+even
print(result)

#10 Reverse List Array
arr = [1,2,3,4,5,6,7]
print(arr[::-1])
arr.reverse()
print(arr)
arr = [1,2,8,4,5,6,7]
for i in range(1, len(arr)+1):
    print(arr[-i], end = " ")


#11 Rotate list without any function
print(" ")
arr = [1,2,3,4,5]
n = 3  # rotate position
print(n)
print(arr[-1:])
print(arr[:-1])
rotate  = arr[-n:] + arr[:-n]
print(rotate)


#12 Slicing
print(" 1D Slicing arrays, [start:end], [start:end:step]")
arr = [1,2,3,4,5,6]
print("start, end :",arr[1::2])
print("start, end, step :",arr[1::2])  # print even or odd
print("Negative Slicing",arr[-3:-1])  #Negative Slicing

#13 Append, Clear Function in List
List1 = ['lemon', 'banana', 'cherry']
list3 = []
list3.append(List1)
print("List 3: ", list3)
List2 = ['apple', 'chikku', 'pineapple']
List1.append(List2)
List1.append("Orange")
print(List1)
list3.clear()
print(list3)
x = List1.copy()


#14 Extend, index, insert, pop, remove Function
fruits = ['apple', 'banana', 'cherry']
points = [1, 4, 5, '9']
fruits.extend(points)
print(fruits)
print(points.index(5))
fruits.insert(1, "orange")
print(fruits)
print("POP at index 1: ",fruits.pop(1))
print(fruits)
fruits.remove("banana")
print("Remove Banana:", fruits)

#15 Delete  Element at Given Index in Array

arr = [1, 2, 3, 4, 5]
#arr.pop(2)
#del arr[2]
arr = arr[:2] + arr[3:]
print(arr)


#16  delete specific value
arr = [1, 3, 5, 2, 6, 1,3]
n = 3
res = []
for i in arr:
    if i != 3:
        res.append(i)
print(res)
#OR
arr.remove(3)
print(arr)

#17 Find all Pairs Whose Sum is Equal to Given number
def find_pairs(arr, target_sum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 12
result = find_pairs(arr, target_sum)
print("All pairs Whose sum is equal to ",target_sum," is: \n",result)

#18 Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
res = []

for i in range(len(list1)):
    res.append((list1[i] + list2[i]))
print(res)

# Easy way
res = []
res = [i+j for i,j in zip(list1, list2)]
print(res)

#19 convert two lists into dictionary
z = zip(list1,list2)
print(dict(z))


#20 Turn every item of a list into its square and find max seperate loop

numbers = [1, 2, 3, 4, 5, 6, 7]

res = [i*i for i in numbers]
print(res)

maxi = max([i for i in res])
print(maxi)


#21 Concatenate two lists in the following order res = [00,01,10,11]

list1 = ["Hello ", "take"]
list2 = ["Dear", "Sir"]
#Nested Loop
res = [x + y for x in list1 for y in list2]
print(res)
# Other way: nested Loop
res = []
for i in list1:
    for j in list2:
        res.append(i + j)

print(res)


#22 Iterate both lists simultaneously, one list in reverse order

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1,list2[::-1]):
    print(x, y)

#23 Remove empty spaces from list
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
#1st method
res = []
for i in list1:
    if i != "":
        res.append(i)
print(res)
#2nd method
res = []
for i in list1:
    if i.strip():
        res.append(i)
     
# printing result 
print(res)

#24 Add new item to list after a specified item

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# understand indexing
# list1[0] = 10
# list1[1] = 20
# list1[2] = [300, 400, [5000, 6000], 500]
# list1[2][2] = [5000, 6000]
# list1[2][2][1] = 6000
list1[2][2].append(7000)
print(list1)

#25 differce in append and extend
arr = [1,2]
arr.extend([3])
print(arr)

arr = [1,2]
arr.append('3')
print(arr)


#26
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# understand indexing
# list1[2] = ['c', ['d', 'e', ['f', 'g'], 'k'], 'l']
# list1[2][1] = ['d', 'e', ['f', 'g'], 'k']
# list1[2][1][2] = ['f', 'g']

# sub list to add
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)


#27  Replace list’s item with new value if found (Only update the first occurrence of an item.)

list1 = [5, 10, 15, 20, 25, 50, 20]

for i in range(len(list1)):
    print(list1[i])
    if list1[i] == 20:
     list1[i] = 200
     break
print(list1)


#28 Remove all occurrences of a specific item from a list (remove 20)

list1 = [5, 20, 15, 20, 25, 50, 20]

for i in list1:
    if i == 20:
     list1.remove(i)
print(list1)


#29  Given an integer array nums, return the maximum possible sum of elements
#  of the array such that it is divisible by three
arr = [1,2,3,4,4]
arr = map(str, arr)
arr = "".join(arr)
res = []

for i in range(len(arr)):
 s = arr[:i] + arr[i+1:]
 res.append(int(s))   
print(res)

sums = []
result = 0

for i in res:
    digits = [int(digit) for digit in str(i)]
    digit_sum = sum(digits)
    if digit_sum % 3 == 0:
       large_num = digit_sum
       result = max(result, large_num)
    
print(result)

#extra of 29 question
res = [6518, 3518, 3618, 3658, 3651]
for i in res:
    digits = [int(digit) for digit in str(i)]
    print(digits)


#30 list to numpy array then add them

import numpy as np
l1 = [2,4,3]
l2 = [5,6,4]

l1 = np.array(l1)
l2 = np.array(l2)
print(l1+l2)




