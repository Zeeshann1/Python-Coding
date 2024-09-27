#01 function that takes two arguments, name and age, and print their value

def zeeshan(name,age):
    print(name, age)
zeeshan("Zeeshan",27)

#02
print(list(range(4, 30, 2)))


#03 Assign a different name to function and call it through the new name
def display_student(name, age):
    print(name, age)

# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)



#04 function with default argument
def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")


#05
def myfunc(x, y):
    a = 2
    b = 4
    z = (x*a) + (y*b)
    return z

print(myfunc(1,1))

#06
def reverss():
    s = "Hello World"
    L = s.split()
    L.reverse()
    #L = L[::-1]
    return ' '.join(L)

print(reverss())



class Solution(object):
    def reverseWords(d, s):
        L = s.split()
        L.reverse()
        return " ".join(L)

result = Solution().reverseWords("the sky is blue")
print(result)



#07 create 2 functions in one class
class InputOutString(object):
    def getString(s, n):
        return n
    def redunct(d,r):
        return r.upper()

r = InputOutString().getString("w")   #input()
print(InputOutString().redunct(r))


#08 Use a formula on input series
#D is the variable  100,150,180
import math
C = 50
H = 30
D = "100,150,180" #input("Input Series: ")
D = D.split(",")
res = []

for i in D:
 Q =  (2 * C * int(i))/H
 sqr = math.sqrt(int(Q))
 res.append(int(sqr))

print(res)



#09   Classes
class MyClass:
  x = 5

print(MyClass.x)


class Person(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
     print("My name is " + self.name)


p1 = Person("John", 36)

print(p1.name, p1.age)
p1.myfunc()

