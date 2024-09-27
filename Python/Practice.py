num = [-1,2,-3,3]
new_num = []

for i in num:
    if i and -i in num:
        new_num.append(i)

print(new_num)
if new_num == []:    
  m = -1
else:
  m = max(new_num)

print(m, "is the max number")



# Input: nums = [-1,2,-3,3] Output: 3, Input: nums = [-1,10,6,7,-7,1] Output: 7



arr = [3,2,3,1]
arr = map(str, arr)
arr = "".join(arr)
m = 0

for i in range(len(arr)):
   new_arr = int(arr[:i] + arr[i+1:])
   m = max(new_arr, m)
   current_max = m
   
print(current_max)


arr = [3,2,4]
target = 6


for i in range(len(arr)):
   for j in range(i+1, len(arr)):
      print(i , j)
      if arr[i] + arr[j] == target:
         print([i,j])




map_dict = {
   'I'       :      '1',
   'V'      :      '5'

}
   
num = "V"
   
for i in num:
   if i in map_dict:
      print(map_dict[i])
   


num2 = "abc"
num3 = "def"


for i in num2:
   for j in num3:
      print(i,j, end = ", ")


arr = [1,0,-1,0,-2,2]

print("")
for i in range(len(arr)):
   for j in range(i):
      for k in range(j):
         for l in range(k):
            if (arr[i]+arr[j]+arr[k]+arr[l] == 0):
               print(arr[i], arr[j], arr[k],arr[l])



s = "   fly me   to   the moon  "
s = s.split()
l = len(s)

print(len(s[l-1]))




arr = [3,2,2,3]
val = 3
res = []
count = 0

for i in arr:
   if i != val:
      res.append(i)
      count +=1

print(res, count)
   

a = "1010"
b = "1011"

deci_a = int(a, 2)
print(deci_a)

deci_b = int(b, 2)
print(deci_b)

res = deci_a + deci_b
print(bin(res)[2:]) 


l1 = [2,4,3]
l2 = [5,6,4]

l1 = l1[::-1]
l2 = l2[::-1]

l1 = [str(i) for i in l1]
l1 = map(str, l1)
l1 = int("".join(l1))

l2 = [str(i) for i in l2]
l2 = map(str, l2)
l2 = int("".join(l2))

res = l1+l2
print([res])


import numpy as np
l1 = [2,4,3]
l2 = [5,6,4]

l1 = np.array(l1)
l2 = np.array(l2)
print(l1+l2)



arr = [1,2,3]
res = []
res.append([])


for i in range(len(arr)):
   res.append([arr[i]])
   for j in range(i):
      res.append([arr[i],arr[j]])
      for k in range(j):
         res.append([arr[i],arr[j],arr[k]])


print(res)

arr = [1,2,3]

arr1 = [3,1,2]
print("e", arr1[-2:] + arr1[:-2])
count = 0


for i in range(len(arr1)):
    arr1 = arr1[-i:] + arr1[:-i]
    count += 1
   

print(count)


arr = [1,2,3,4]
pair = int(len(arr)/2)
print(pair)

arr1 = arr[:pair]
print(arr1)

arr2 = arr[pair:]
print(arr1[::-1] + arr2[::-1])



str1 = "sadbutsad"
str2 = "sad"
print(str1.find(str2))



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
board = np.array(board)
board = board.flatten()
print(board)
word = "ABCB"
count = 0

for i in word:
   if i in board:
      count += 1
      #mask = board != board[i]
      #board = board[mask]

if count == len(word):
   print("true")
else:
   print("false")



import numpy as np
arr = np.array([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]])
word = "ABCB"    # "SEE", "ABCB" ABCCED
arr = arr.flatten()
res = []

for i in range(len(word)):
    if word[i] in arr:
        res.append(word[i])
        mask = arr != arr[i]
        arr = arr[mask]

print("Result length =", len(res))
print("Word length =", len(word))

if len(res) == len(word):
    print("True")
else:
    print("False")



nums = [2,2,3,2]

freq = {}

for i in nums:
   if i in freq:
      freq[i] += 1
   else:
      freq[i] = 1

print(freq)

for key, value in freq.items():
   if value == 1:
      print(key)




arr = [1,2,3,4,5]
k = 2
arr = arr[-k:] + arr[:-k]
# [3, 4, 5, 1, 2] output positive k
# [4, 5, 1, 2, 3] output negative k
#arr1 = np.array(arr)
#rotated_matrix = np.roll(arr1, 2, axis= 0)


print(arr)



#mask = arr != arr[i]
#arr = arr[mask]


arr = [1,2,3,4]
s = [1,4,4]


for i in arr:
   if i in s:
      print(i)



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
board = np.array(board)
board = board.flatten()
res = []
word = "SEE"

for i in range(len(word)):
   if word[i] in board:
      res.append(word[i])
      mask = board != board[i]
      board = board[mask]

print(res)
print(word)

if res == word:
   print("true")
else:
   print("false")

#"SEE", "ABCB" ABCCED




# Function to compare two numbers
def compare(a, b):
    if a + b > b + a:
        return True
    else:
        return False

# Function to generate the maximum number
def max_number(arr):
    # Convert all numbers to strings
    arr = list(map(str, arr))
    
    # Bubble sort with custom comparison
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if not compare(arr[j], arr[j+1]):
                # Swap if the current order is not optimal
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    # Join sorted list into a single string
    return ''.join(arr)

# Example usage
arr = [3,30,34,5,9]
result = max_number(arr)
print(result)  # Output will be '9534330'



num = 38
num = str(num)
s = 0
res = 0

for i in num:
   s += int(i)

print(s)

for j in str(s):
   res += int(j)  
   
print(res)  # Output: 11


pattern = "abba"
pattern_lst = []
s = "dog cat cat dog"
s = s.split()
print(s)

for i in pattern:
   pattern_lst.append(i)

print(pattern_lst)

for i , j in zip(pattern_lst, s):
   print(i, j)


str1 = "112358"
c = 0

for i in range(len(str1)-2):
    n1 = int (str1[i])
    n2 = int (str1[i+1])
    nth = n1 + n2
    if nth != int (str1[i+2]):
       c += 1

if c == 0:
   print("True")
else:
   print("False")
    

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
c = 0

for i in range(len(nums1)):
   for j in range(len(nums1)):
      for k in range(len(nums1)):
         for l in range(len(nums1)):
            #print(nums1[i], nums2[j], nums3[k], nums4[l])
            if (nums1[i] + nums2[j] + nums3[k] + nums4[l]) == 0:
               print((i, j, k, l))
               c += 1
print(c)





arr = [3,30,34,5,9]

arr = [1,2,3]
print(arr[:1] + arr[2:])


n = "214"
rev = n[::-1]

for i in n:
   rev = n[::-1]
   if n == rev:
      print(n)
      break
   else:
      n = int (n) - 1
      n = str(n)


n = "329"
n = int(n)
start = n-10
end = n+10

for i in range(start, end):
   if str(i) == (str(i)[::-1]):
      print(i)

