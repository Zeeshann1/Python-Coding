#01 Remove character from string, 2) str to list, 3) list to str
str1 = 'Zeeshan Hyder'
str1 = list(str1)

str1.remove('e')
str1 = "".join(str1)
print("e has been remove = ",str1)
print("Data Type = ",type(str1))

str1 = str1.replace('n','N')
print("Replaced n with N = ",str1)

uppercase = str1.upper()
print("ALL UpperCase = ", uppercase)

lowercase = uppercase.lower()
print("All lowerCase = ",lowercase)

str1 = str1.replace(' ','')
print("Removed Space = ",str1)

print("Reserve the string ",str1[::-1])


#02 Python Program to count occurrence of a given characters in string.
str1 = 'Zeeshan'
print("Original String  = ",str1)
str = str1.count('n')
print(str)


#03 Python Program to check if two Strings are Anagram. (“listen” and “silent”)

str1  = 'listen' 
str2 = 'silent'

s1 = sorted(str1)
s2 = sorted(str2)
#l1 = len(str1)
#l2 = len(str2)
#print(l1,l2)

c1 = 0
c2 = 0
for i in str1:
    c1 = c1 + 1
print(c1)

for i in str2:
    c2 = c2 + 1
print(c2)

if (s1 == s2) and (c1 == c2):
    print("Anagram")
else:
    print("Not Anagram")


#04 Python program to check a String is palindrome or not.

str1 = 'Mad Am'
str1 = str1.replace(" ", '')
str1 = str1.lower()
rev = str1[::-1]

if rev == str1:
    print("Palindrome")
else:
    print("No palindrome")


#05 check if given charater is digit

ch = '1'
if ch >= '0' and ch <= '9':
    print("yes")
else:
      print("no")

#06 convert lowercase vowel to uppercase in string.
str1 = " Hello Word"
vowels = 'aeiouAEIOU'

for i in str1:
    if i in vowels:
        new_str = i.upper()
        str1 = str1.replace(i , new_str)
print(str1)


#07 delete vowels in a given string.
str1 =  'hello'
vowels = 'aeiouAEIOU'

for i in str1:
    if i in vowels:
        str1 = str1.replace(i , '')
print(str1)


#08 print vowels and Consonants in string and count

str1 = 'quescol'
vowels = 'aeiouAEIOU'
c1 = 0
c2 = 0
v = []
c = []

for i in str1:
    if i in vowels:
        v.append(i)
        c1 += 1
    else:
        c.append(i)
        c2 += 1

print("Total Vowels = ", c1, "Total Consonants = ", c2)

v = "".join(v)  # convert list into str
c = "".join(c)  # convert list into str
print("Vowels: ",v, " Consonants: ", c)


#09 Print highest frequency Character in String in Python

string = "pyython"
freq_dict = {}
# Count the frequency of each character
for char in string:
    if char in freq_dict:
        freq_dict[char] += 1
        print(freq_dict)
    else:
        freq_dict[char] = 1
        print("else", freq_dict)
max_freq = max(freq_dict.values())
# Print the characters with maximum frequency
for char in freq_dict:
    if freq_dict[char] == max_freq:
        print(char, end=' ')

print("")


# 10 Replace '_' at first vowel in string OR at all vowels in string
str1 = 'quescol'
vowels = 'aeiouAEIOU'

for i in str1:
    if i in vowels:
        v = i
        str1 = str1.replace( v , '_')
        #break        

print(str1)

#11 count and print specialchar, Alphabatics and digits in string

str1 = "Ques123!@we12"
digits = "123456789"
specialchar = "!@#$%^&*(_)"

c1 = 0
c2 = 0
c3 = 0
s= []

for i in str1:
    if i in specialchar:
        print(i)
        s.append(i)
        c1 += 1
    elif i in digits:
        print(i)
        c2 += 1
    elif i not in digits and specialchar:
        print(i)
        c3 += 1

print("specialchar: ",c1)
print("Numbers: ",c2)
print("Alphabatics: ",c3)
print("specialchar", " ".join(s))


#12 Separate Characters in a Given String

str1 = "hello"
for i in str1:
    print("\n",i)


#13 remove spaces from string
#Method 01
str1 = "Py thon"
print("Before: ",str1)
str1 = str1.replace(" ", "")
print("After: ",str1)

#Method 02
space = " "
str1 = "Py thon"
for i in str1:
    if i not in space:
        print(i)

#Method 03
str1 = "Py thon"
r = []
for i in str1:
    if i != ' ':
        r.append(i)
print("Result: ","".join(r))


#14 Join Two strings
str1 = 'python1'
str2 = "Python2"

print(str1+str2)
print("".join([str1,str2]))


#15 remove duplicate and find duplicate

str1 =  'hello quescol'
str2 = []
duplicate = []

for i in str1:
    if i not in str2:
        str2.append(i)
    else:
        duplicate.append(i)

print("After remove duplicate = ", "".join(str2))
print("Duplicate: ",duplicate)



#16 find sum of integers present in the string

str1 = "qwel123rty456"
digits = "123456789"
x = []
sum = 0

for i in str1:
    if i in digits:
        i = int(i)
        #print(type(i))
        sum = sum + i
        x.append(i)

print("digits: ",x)
print("Sum: ",sum)

#OR 
sum = 0
for i in x:
    sum+= i
print("Sum = ",sum)


#17 remove duplicates all (hello quescol = h qusc)

str1 = 'hello quescol'
str2 = []
str3 = []

for i in str1:
    if i not in str2:
        str2.append(i)
    else:
        str3.append(i)
        str1 = str1.replace(i, '')

print("After removal of duplicate: ", "".join(str2))
print("duplicates: ", "".join(str3))
print("After removal of all duplicates", str1)


#18 sort array in Assending and Desending order

str1 = "quescol"
s = sorted(str1)
print(s)
print("Assending Order sorting", "".join(s))
s = s[::-1]
print("Desending Order sorting", "".join(s))


#19 Reseven the string sentence
str1 = "I love HK"
str1 = str1.split()
str1.reverse()  #OR  str = str[::-1]
print(" ".join(str1))


#20 Given a String, perform split on vowels.
#Method 01
str1 = "GFGaBste4oCS"
vowels = "aeiouAEIOU"

for i in str1:
    if i in vowels:
        str1 = str1.replace(i, " ")

print(str1)
r = []
for i in str1:
    if i == ' ':
        r = str1.split()
print(r)


#Method 02
str1 = "GFGaBste4oCS"
vowels = "aeiouAEIOU"

for i in str1:
    if i in vowels:
        str1 = str1.replace(i, "*")

print(str1)
str1 = str1.split("*")
print(str1)


#21 remove multiple empty spaces from string List
#method 01
str1 = ['gfg',' ', ' ', 'is', '         ', 'best']
res = []

for i in str1:

    if (i =='gfg') or (i =='is') or (i =='best') :
        res.append(i)
        print(i)

print(res)

#Method 02
str1 = ['gfg',' ', ' ', 'is', '         ', 'best']
res = []

for i in str1:
    if (i != ' ') and (i != '         ') :
        res.append(i)
        print(i)

print(res)

#Method 03
str1 = ['gfg',' ', ' ', 'is', '         ', 'best']
res = []

for i in str1:
    if i.strip():
        res.append(i)
     
# printing result 
print(res)



#22 Remove punctuation from string

str1 = 'Gfg, is best: for ! Geeks ;'
punctuation = ',:!;'

for i in str1:
    if i in punctuation:
        str1 = str1.replace(i , "")

print(str1)


#23 Test if string is subset of another
str1 = "geeksforgeeks"
str2 = "gfks"
count = 0

for i in str2:
    if i not in str1:
        count += 1

if count  == 0:
    print("str2 is subset of str1")
else:
    print("str2 is not subset of str1")
    


#24 Remove suffix from string list

list_arr = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
res = []
for i in list_arr:
    if i[-1] != 'x':
      res.append(i)
print(res)


#25  Check if a given string is binary string
string = "101010000111"
count = 0

for i in string:
    if (i == 0) or (i == 1):
        count += 1

if count != 0:
    print("No")
else:
    print("Yes")


#26 Reverse Sort a String
str1 = 'geekforgeeks'
str1 = sorted(str1)
str1 = "".join(str1)
rev = str1[::-1]
print(rev)


#27 Check if two strings are Rotationally Equivalent

str1 = "geeks"
str2 = "ksegezn"
count = 0

for i in str1:
    if len(str1) == len(str2):
        if i not in str2:
            print("No")
        else:
            count += 1

if count != 0:
    print("Yes")
else:
    print("No")


#28 palindrom
#Q1
x =  'I am Zeeshan'
x = x.replace(" ", '')
x = x.lower()
print(x)
r = x[::-1]
print(r)

if x == r:
   print("YES")
else:
   print("NO")

#Q2
s = "I am IronnorI Ma i"
s = s.replace(" ", "").lower()
print(s)

rev = s[::-1]
if rev == s:
 print("true")
else:
   print("false")



#29 merge specific index
str1, str2 = "good", "bad"
i = 1
j = 2
merged = ""
merged += str1[i:] + str2[j:]
print(merged)


#30 Merge Alternatively
i = 0
j = 0
merge = ''
while i < len(str1) and i < len(str2):

   merge += str1[i] + str2[j]
   i += 1
   j += 1

print(merge)


#31 Remove Zero
n = '0133'
n_without_zero = n.replace('0', '')
print(n_without_zero)

result = ''
for i in range(1, len(n)):
   result += n[i]

print(result)


#32 Return the count of a given substring from a string

str1 = "Emma is good developer. Emma is a writer"
count = str1.count("Emma")
print("Total sub count = ",count)

#33  Count number of words in string sentence

str1 = "Emma is good developer. Emma is a writer"
str1 = str1.split()
print(str1)
print("Total number of words =", len(str1))


#34 For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’. (print even index)

str1 = "pynativebwr"
print(len(str1))
for i in range (0, len(str1), 2):
    print(str1[i])
    i + 1

#35 List to String
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
sentence = " ".join(words)
print(sentence)  # Output: "The quick brown fox jumps over the lazy dog"


#36 Remove first n characters from a string

def remove(name, n): 
 print(len(name))
 print(name[n:])

remove('zeeshan', 3)


#37  Search word in a string sentence

sentence = "The quick brown fox jumps over the lazy dog"
word = "fox"
words = sentence.split()
print(words[0])

if word in sentence:
    print("Found!")
else:
    print("Not found!")

#38 Check if two strings are equal
def arrayStringsAreEqual(word1, word2):

    if(word1 == word2):
        return True
    else:
        return False


word1 = "i am good"
word2 = "i am good"
print(arrayStringsAreEqual(word1, word2))

#39 Merging two strings using slicing
str1, str2 = "good", "bad"
i = 1
j = 2
merged = ""
merged += str1[i:] + str2[j:]
print(merged)

#40 Remove duplicate from string
str1 = "hello"
res = "".join(dict.fromkeys(str1))
print(res)

#41 Swaping #Swap a,b values
a = 2
b = 3
a,b = b , a
print("a =",  a)
print("b =",  b)



#42 word search
txt = "The best things in life are free!"

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


#43 Create a string made of the first, middle and last character

str1 = "James"
l = len(str1)
mid = str1[int(l/2)]
first = str1[0]
last = str1[-1]
res = first+mid+last
print(res)


#44 Create a string made of the middle three characters
str1 = "JhonDipPeta"
l = len(str1)
print(l)
mid = int(l/2)
print(mid)
res = str1[(mid-1):-(mid-1)]
print(res)

#45 Append new string in the middle of a given string
s1 = "zeeshan"
s2 = "hyder"
l = len(s1)
mid = int(l/2)
res = s1[:mid]+ s2 + s1[mid:]
print(res)

#46 
str1 = "America"
str2 = "Japan"

l1 = len(str1)
mid = str1[int(l/2)]
first = str1[0]
last = str1[-1]

l2 = len(str2)
mid2 = str2[int(l2/2)]
first2 = str2[0]
last2 = str2[-1]
res = first+first2+mid+mid2+last+last2
print(res)

#47 Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"
lowr = []
upp = []

for i in str1:
    if i.islower():
        lowr.append(i)
    else:
        upp.append(i)

print("lower = ",lowr)

res = lowr+upp
print("".join(res))

#48

str1 = "P@#yn26at^&i5ve"
#dig = "123456789"
#Symbol = "@#^&!*"

dig_count = 0
Symbol_count = 0
char_count = 0

for i in str1:
    if i.isdigit():
        dig_count = dig_count + 1
    elif i.isalpha():
        char_count = char_count + 1
    else:
        Symbol_count = Symbol_count + 1

print("number of Digits:", dig_count)
print("Number of Symbols:",Symbol_count)
print("Number of Chars:",char_count)

#49 mixed String s1 = "Abc" s2 = "Xyz" Expected Output: AzbycX

s1 = "Abc"
s2 = "Xyz"
res = ''

str1, str2 = "Abc", "Xyz"
i = 0
j = 1
merge = ''
while i < len(str1) and i < len(str2):

   merge += str1[i] + str2[-j]
   i += 1
   j += 1

print(merge)

#50 Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"

word = 'USA'
word1 = 'usa'
count = 0

if word in str1:
    count += 1
if word1 in str1:
    count += 1

print("Result:", count)

#51

str1 = "Apple"
dic = dict()

for i in str1:
    print(i)
    count = str1.count(i)
    dic[i] = count

print(dic)

#52 Split a string on hyphens
str1 = "Emma-is-a-data-scientist"
str1 = str1.split('-')
print(str1)
for i in str1:
    print(i)

#53 remove spaces and None
str1 = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res = []

for i in str1:
    if i:
        res.append(i)
print(res)

#54 Find words with both alphabets and numbers

str1 = "Emma25 is Data scientist50 and AI Expert 123"
str1 = str1.split()
res =[]
res1 =[]

for i in str1:
    if (i.isalpha()) or (i.isdigit()):
        res.append(i)
    else:
        res1.append(i)

print(" \n".join(res1))

#55

str1 = '/*Jon is @developer & musician!!'
Symbol = "@#^&!*/&"

for i in str1:
    if i in Symbol:
        str1 = str1.replace(i, "#")
print(str1)



#56 sorting the words

str1 = "without,hello,bag,world"
str1 = str1.split(",")
s = sorted(str1)
print(",".join(s))



#57 sort and remove duplicates
n = "hello world and practice makes perfect and hello world again"
n = n.split()
print(n)
res = " ".join(dict.fromkeys(n))
print(" ".join(sorted(res.split())))


#58 count alphabates and digits in string
str1 =" hello world! 123"
di = 0
n = 0
for i in str1:
    if i.isalpha():
        di += 1
    if i.isdigit():
        n += 1
print(di , n)


#59

str1 ="H1e2l3l4o5w6o7r8l9d"
s = "Helloworld"
res =[]

for i in str1:
    if i in s:
        res.append(i)

print("".join(res))


#60

str1 = "abcdefgabc"
res ={}

for i in str1:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1

print(res)

for key, value in res.items():
    #print(f"{key} , {value}")
    print(key , "," , value)


