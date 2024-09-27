


#01 Squares of Sorted List
class Solution(object):
    def numTeams(self, arr):
           
        res = []

        for i in arr:
            sq = i*i
            res.append(sq)
        
        res = sorted(res)
        print(res)
 
Solution().numTeams([-7,-3,2,3,11])

#02
arr = [1,3,4,2,2]
new = []
dup = []

for i in arr:
    if i not in new:
        new.append(i)
    else:
        dup.append(i)
print(dup)


#03
#Input: num = "1432219", k = 3   Output: "1219"
#Input: num = "10200", k = 1 Output: "200"
#Input: num = "10", k = 2 Output: "0"


num = "1432219"
nums = str(num)
k = 3
list_arr = []

for i in nums:
    list_arr.append(i)

print(list_arr)



#04 
# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.
# cases: Input: nums = [-1,2,-3,3] Output: 3, Input: nums = [-1,10,6,7,-7,1] Output: 7 and Input: nums = [-10,8,6,7,-2,-3]Output: -1

num = [-10,8,6,7,-2,-3]
new_num = []

for i in num:
    if i and -i in num:
        new_num.append(i)

if new_num == []:    
  m = -1
else:
  m = max(new_num)

print(m, "is the max number")


#05
# form a largest number from list after delete a element

#06 A phrase is a palindrome or not？
s = "A man, a plan, a ca nal: P a nam a"
s= s.lower()
s = s.replace(" ", '')
per = ",:"
for i in per:
    if i in per:
        s = s.replace(i, "")
rev = s[::-1]
print(s)
print(rev)
if s == rev:
    print("True")
else:
    print("False")


#07 Remove Single digit from list
arr = [2,2,1]
res = []

for i in arr:
    if i not in res:
        res.append(i)

for i in res:
    arr.remove(i)
    if i not in arr:
        result = i
        break

print(result)

#08 sort the people

names = ["Mary","John","Emma", "Ali"]
heights = [170,165,180, 900]

for i in range(len(heights)):
    for j in range(len(heights)-1):
        if heights[j] < heights[j+1]:
            heights[j], heights[j+1] = heights[j+1], heights[j]
            names[j], names[j+1] = names[j+1], names[j]
print(names)
        


#09 count frequency of letter in string and remove unequal frequency letters
#word = "abcc"  delete c , output = abc
#word = "aazz" dont remove any letter
#word = "aazzx" remove x and word become aazz



#10 two element sum from list to get targeted sum result

nums = [2,7,11,15]
target = 9
res = []

for i in range(len(nums)):
    for j in range(len(nums)):
     if i !=j:
        if nums[i] + nums [j] == target:
           res.append(i) and res.append(j)
print(res)


#11 Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string ""

def longestCommonPrefix(str):
    if not str:
        return ""
    
    min_length = min(len(s) for s in str)

    longest_common_prefix = ""
    for i in range(min_length):
        # Take the current character from the first string
        current_char = str[0][i]
        
        # Check if this character is the same in all other strings
        if all(s[i] == current_char for s in str):
            longest_common_prefix += current_char
        else:
            break
    
    return longest_common_prefix

# Example usage
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
#print(longestCommonPrefix(["dog", "racecar", "car"]))    # Output: ""


#12 Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

arr = [-1,0,1,2,-1,-4]

for i in range(len(arr)):
    for j in range(i):
        for k in range(j):
            if (i != j) and (i != k) and (j != k) and (arr[i] + arr[j] + arr[k] == 0):
                print(arr[i],arr[j],arr[k])
                

                
#13
arr = [123,456,678]
min_length = max(i for i in arr)
print(min_length)

#14 Write a function to find the maximum sum of a subarray of size k in an array

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
arr = sorted(arr)
arr.reverse()
print(arr)
max_sum = sum(arr[:3])
print(max_sum)


#15 rotate the list to the right by k places   example head = [0,1,2], k = 4 Output: [2,0,1]
#Input: head = [1,2,3,4,5], k = 2 , Output: [4,5,1,2,3]
arr = [1,2,3,4,5]
print(arr[-2:] + arr[:-2])

#16
#Given an array of integers, find the maximum number of consecutive elements that sum up to a given
#number. The function should return the maximum number of consecutive elements that sum up to the given number

arr = [1, 2, 3, 4, 5]
target = 9
arr = sorted(arr)
arr = arr[::-1]
print("Given Array:", arr)

for i in range(len(arr)):
    for j in range(i):
        if arr[i]+arr[j] == target:
            print(arr[i], arr[j])


        
#17 combination sum: create sub-array that was targeted sum
arr = [3,2,5]
target  = 8
result = []

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]+arr[j] == target:
                    print(arr[i],arr[j])
                    result.append([arr[i], arr[j]])
        for k in range(len(arr)):
            if arr[i]+arr[j]+arr[k] == target:
                    print(arr[i],arr[j],arr[k])
                    result.append([arr[i], arr[j], arr[k]])
            for l in range(len(arr)):
                if arr[i]+arr[j]+arr[k]+arr[l] == target:
                    print(arr[i],arr[j],arr[k],arr[l])
                    result.append([arr[i], arr[j], arr[k], arr[l]])

print(result)
   
#18 Sort Array without function and display number of rotations
arr = [1,1,4,2,1,3]
count = 0

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            count += 1

print(arr, count)

#19 how many ballon words can we generate from given text

text = "loonbalxballpoon"
target = "ballon"
res = []

for i in range(len(text)):
    if text[i] in target:
        text = text.replace(text[i], '*')
    
print(text)
c = text.count("*")
print(c)
if (c >= 6) and (c < 12):
    print("1")
elif (c >= 12) and (c < 18):
    print("2")
elif (c >= 18) and (c < 24):
    print("3")


#20 Input: arr = [1,0,2,3,0,4,5,0] Output: [1,0,0,2,3,0,0,4]

arr = [1,0,2,3,0,4,5,0]
indx = []

for i in range(len(arr)):
    if arr[i] == 0:
        indx.append(i)
print(arr)
print(indx)
new_arr = []

for i in range(len(arr)):
    new_arr.append(arr[i])
    if i in indx:
        print(i)
        new_arr.append(0)

print(new_arr[:len(arr)]) # print new array of same length of original array


#21  Input: words = ["bella","label","roller"] Output: ["e","l","l"]
#Input: words = ["cool","lock","cook"] Output: ["c","o"]

arr = ["bella","label","roller"]
arr1 = arr[0]
arr2 = arr[1]
arr3 = arr[2]
res = []

for i in arr1:
    if (i in arr2) and (i in arr3):
        #if i not in res:
         res.append(i)
print(res)

#22 All missing numbers : Input: nums = [4,3,2,7,8,2,3,1] Output: [5,6]
#Input: nums = [1,1] Output: [2]

arr = [4,3,2,7,8,2,3,1]
res = []
print("length=",len(arr))

for i in range(1,len(arr)+1):
    res.append(i)

print("All missing numbers:")
for i in res:
    if i not in arr:
        print(i) 


#23 Return the minimized largest sum of the splited array
#Input: nums = [7,2,5,10,8], k = 2 Output: 18

arr = [7,2,5,10,8]
k = 2
l = len(arr)
sum_of_sub_arr1 = sum(i for i in arr[:3])
print(arr)
print(sum_of_sub_arr1)
sum_of_sub_arr2 = sum(i for i in arr[3:])
print(sum_of_sub_arr2)

#24 Word SEARCH: The same letter cell may not be used more than once
import numpy as np
arr = np.array([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]])
word = "ABCCED"    # "SEE", "ABCB"
arr = arr.flatten()
res = []

for i in range(len(word)):
    if word[i] in arr:
        res.append(word[i])
        #mask = arr != arr[i]
        #arr = arr[mask]

print("Result length =", len(res))
print("Word length =", len(word))

if len(res) == len(word):
    print("True")
else:
    print("False")


#25 Plus one into input [1,2,3] output = [1,2,4] , 123 +1 = 124

arr = [4,3,2,1]
m = map(str, arr)
str1 = ''.join(m)
res = int(str1) + 1
print(res)
result = []
for i in str(res):
    print(i)
    result.append(int(i))
print(result)  


#26 
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
#Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"] Output: false

 
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(len(s)):
        if dp[i]:
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordSet:
                    dp[j] = True
    
    return dp[len(s)]

# Example usage
s = "applepenapple"
wordDict = ["apple","pen"]
print(wordBreak(s, wordDict))  # Output: False

#27 Input: nums = [1,2,3] Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# The solution set must not contain duplicate subsets. Return the solution in any order.
arr = [1,2,3]
res = []

for i in range(len(arr)+1):
    res.append([i])
    for j in range(i):
        res.append([i,j])
        for k in range(j):
            res.append([i,j,k])

print(res)

#28 4Sum
# Input: nums = [1,0,-1,0,-2,2], target = 0 Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


arr = [2,2,2,2,2]
target = 8
result = []
res = []
#sum = 0

for i in range(len(arr)):
    for j in range(i):
        for k in range(j):
            for l in range(k):
                if (arr [i] + arr[j] + arr[k] + arr[l]) == target:
                    result.append([arr[i],arr[j],arr[k],arr[l]])

print(result)

unique_tuples = {tuple(i) for i in result}
print(unique_tuples)
unique_lists = [list(j) for j in unique_tuples]
print(unique_lists)


#29  
#Input: s = "abbaca" Output: "ca"
#Input: s = "azxxzy" Output: "ay"

s = "azxxzy"
dup = []
res = []
final = []

for i in s:
    if i not in dup:
        dup.append(i)
    else:
        res.append(i)

print(dup)
print(res)

for i in dup:
    if i not in res:
        final.append(i)

print("".join(final))

#30 
# Max Sum Input: nums = [-2,1,-3,4,-1,2,1,-5,4] Output: 6
#Explanation: The subarray [4,-1,2,1] has the largest sum 6.

def max_subarray_sum(nums):
    if not nums:
        return 0

    max_current = max_global = nums[0]
    
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        print("max_current =",max_current)
        if max_current > max_global:
            max_global = max_current
    
    return max_global

# Example usage
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(nums))  # Output: 6




    
#31 form a largest number from list after delete an element

arr = [0,2,0,1] 

def list_to_number(lst):
        return int(''.join(map(str, lst)))

largest_num = 0

for i in range(len(arr)):
        #print(arr[:i] , arr[i+1:])
        new_list = arr[:i] + arr[i+1:]
        print(new_list)
        largest_num = max(largest_num, list_to_number(new_list))
    
print(largest_num)



