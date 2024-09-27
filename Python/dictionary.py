import numpy as np


# 01 replace in string 
str1 = "geeksforgeeks is best"

print("The original string is : ", str1)

map_dict = {'e': '1', 'b': '6', 'i': '4'}

for i in str1:
    if i in map_dict.keys():
        str1 = str1.replace(i , map_dict[i])

print(str1)


#02 numeric words to their corresponding digits
word_to_digit = {
	'zero': '0',
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9'
}

# Initializing string
str1 = 'zero four zero one ten'

# Split the input string into words
str1 = str1.split()

digits = []
for i in str1:
    if i in word_to_digit:
        digits.append(word_to_digit[i])

result = ''.join(digits)

# Print the original string and the result
print('The original string is:', str)
print('The string after performing replace:', result)


#03 Remove duplicate from string
str1 = "hello"
res = "".join(dict.fromkeys(str1))
print(res)


#04
arr = [1, 2, 3, 4, 5, 6, 5, 4, 5, 1, 2, 3, 4, 5, 6, 5, 4, 5]
freq_dict = {}
for i in arr:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1
        
print(freq_dict)
highest_freq_element = max(freq_dict, key=freq_dict.get)
print("Highest frequency element:", highest_freq_element)




#06
###############
#word = "abcc"  delete c , output = abc
#word = "aazz" dont remove any letter
#word = "aazzx" remove x and word become aazz

word = "abcc"
freq = {}
res = []
for i in word:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
highest_freq_element = max(freq, key=freq.get)
print("Highest frequency element:", highest_freq_element)

#for keys in freq.keys():
#for values in freq.values():
#for key, value in freq.items():



#07
word = "aabbccc"
freq = {}

for i in word:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)
print(freq.items())
print(max(freq.values()))
print(max(freq.keys()))



dic = {'a': 1, 'b' : 2}
s = 'ab'

#08 convert dictionary interger values into string
for key, value in dic.items():
    dic[key] = str(value) 
print(dic)

for i in s:
    if i in dic.keys():
     s = s.replace(i, dic[i])

print(s)


#09 Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
value = [10, 20, 30]
dic = dict(zip(keys, value))
print(dic)

#10 Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 ={**dict1, **dict2}
print(dict3)

#11 Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}
# solution
print(sampleDict['class']['student']['marks']['history'])

#12 Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])


#13
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary", "city"]

res = {}
for k in keys:
    # add current key with its va;ue from sample_dict
    res.update({k: sample_dict[k]})
print(res)


#14 Create a dictionary by extracting the keys from a given dictionary

#15 Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for k in keys:
    #sample_dict.pop(k)
    del sample_dict[k]
print(sample_dict)

#16 Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 'a' in sample_dict.keys():
    print("given element found in the dictionary")
else:
    print("given element not found in the dictionary")


#17 Rename Key, Add another Key, and Remove any key
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
#Rename Key
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

# Add another Key
sample_dict['designation'] = "engineer"
print(sample_dict)

# Remove any key
sample_dict.pop('name')
print(sample_dict)

#18  Get the key of a minimum value from dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict, key=sample_dict.get))  # one line solution

# loop method
mini = 100 # suppose current minimun value is 100
for key , value in sample_dict.items():
    res = value
    mini = min(mini, res)

print(mini)
    
for key , value in sample_dict.items():
    if value == mini:
        print(key)


#19 Change value of a key in a nested dictionary

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict['emp3']['salary'] = 8500
print(sample_dict)


#20 generate a dictionary input = 8, output = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = 8
res = dict()
for i in range(1, n + 1):
    res[i] = i ** 2
print(res)


n= "34,67,55,33,12,98"        #input("Enter numbers ")
# Input 34,67,55,33,12,98
# Output ['34', '67', '55', '33', '12', '98'] # ('34', '67', '55', '33', '12', '98')

print("Type Input", type(n))
n = n.split(",")
print("Split Input List", n)
n = tuple(n)
print("Tuple Input,", n)



#21 print max repeated letter in the word

str1 = "hello"
freq = {}

for i in str1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print(freq)

print("Max repeated letter:", max(freq, key=freq.get))
print("Number of repeatation:", max(freq.values()))



#18  get minmum key and value
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

res = min(sample_dict, key=sample_dict.get)
print(res, sample_dict[res])





#19 map_dict = {'e': '1', 'b': '6', 'i': '4'}
print(map_dict)
print(map_dict["e"])


for i in map_dict.values():
    print(i)

for i in map_dict.keys():
    print(map_dict[i])

for i in map_dict.keys():
    print(i)


#20 construct a dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

str1 = "zeeshan"
map_dict = { "e": "1", "n": "2"}

for i in str1:
    if i in map_dict.keys():
        str1 = str1.replace(i ,map_dict[i])
print(str1)

#21 
arr = [1, 2, 3, 4, 5, 6, 5, 4, 5, 1, 2, 3, 4, 5, 6, 5, 4, 5]
freq_dict = {}

for i in arr:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        print(freq_dict)
        freq_dict[i] = 1

print(freq_dict)
highest_freq_element = max(freq_dict , key=freq_dict.get)
print("Highest frequency element:", highest_freq_element)

#22
n = 8
res = dict()
for i in range(1,8):
    res[i] = i*i
print(res)



#23 Single Number II  input  = [2,2,3,2] ,  output = 3
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


