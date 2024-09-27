#01
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(thistuple[1])
print(thistuple[-1])
print(thistuple[2:4])

thistuple = list(thistuple)
print(thistuple)


#02 Input 34,67,55,33,12,98
# Output ['34', '67', '55', '33', '12', '98'] # ('34', '67', '55', '33', '12', '98')

#n= input("Enter numbers ")
n = "34,67,55,33,12,98"
print("Type Input", type(n))
n = n.split(",")
print("Split Input List", n)
n = tuple(n)
print("Tuple Input,", n)

#03




