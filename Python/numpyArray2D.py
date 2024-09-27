import numpy as np

# 01 Creating 3X3 array using numpy.arange
print("Creating 3X3 array using numpy.arange")
ar1 = np.arange(1, 10, 1)
ar1 = ar1.reshape(3,3)
print(ar1)


# 02 Display specific row or col
sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]]) 
print("Printing Input Array")
print(sampleArray)

print("\n Printing array column & rows")
R1 = sampleArray[2,...,1] # print row 1
R2 = sampleArray[1,...] # print row 2
R3 = sampleArray[2,...] # print row 3

C1 = sampleArray[...,0] # print Col 1
C2 = sampleArray[...,1] # print Col 2
C3 = sampleArray[...,2] # print Col 3

print(R1, R2, R3)
print(C1,C2,C3)


#03 Spiting Array into sub-array
print("\nDividing 8X3 array into 4 sub array\n")
subArrays = np.split(sampleArray, 3) 
print(subArrays)


#04 Array function (flatten,reshape, delete,insert, average )
ar1 = np.array([[1, 7, 3], [5, 2, 7], [8, 0, 10]])
print("Printing Original Array:\n", ar1)
ar1 = ar1.flatten()
print("Printing Flatten Array:\n",ar1)
ar1.sort()
ar1 = ar1.reshape((3, 3))
print("Printing Sorted Array:\n",ar1)
ar1 = np.delete(ar1 , 1, axis = 1)
print("Deletion on 2nd Colunm:\n",ar1)
arr = np.array([[10,10,10]])
ar1 = np.insert(ar1, 1, arr, axis = 1)
print("Array after insertion new col:\n",ar1)
ar2 = np.array([[3,3,3], [1,3,3]])
print("Printing Original Array:\n", ar2)
ar2 = np.average(ar2)
print(ar2)


####################   Printing Fuctions of Matrix #########################
#05 Array sum, Multiplication, Division, Transpose, Shape, Size, max, min
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 9]])
matrix2 = np.array([[10, 11, 12], [13, 14, 14], [16, 17, 18]])
   
print("Sum of two matrix: \n",matrix1 + matrix2)
print("Multiplication of two matrix: \n", matrix1@matrix2)
print("Multiplication of each element of two matrix: \n", matrix1*matrix2)
print("Division of each element of two matrix: \n", matrix1/matrix2)
print("Transpose of matrix: \n",matrix1.T)
print("Shape of matrix: \n", matrix1.shape)
print("Size of matrix: \n",matrix1.size)
print("Print row and col of matrix: \n", matrix1[0, :])
print("Print Max num of matrix: \n",np.max(matrix1))
print("Print Min num of matrix: \n",np.min(matrix1))



#06 Slicing  Ellipsis

ar1 = np.array([[1, 7, 3], 
                [5, 2, 7], 
                [8, 0, 10], 
                [3, 2, 99]])

print("Printing Original Array:\n", ar1)
newArray = ar1[3::, :1:]   # Multidimensional Slicing: array[start1:stop1:step1, start2:stop2:step2, ...]
newArray = ar1[:3, 1:]    # Basic Slicing

print("Result Array:\n" , newArray)
ar1 = np.array([0,1,3,3,4,5,6,7])
#ar1 = ar1[3:6:1]     #Basic Slicing: array[start:stop:step], by default step = 1
#ar1 = ar1[1,...]      #Ellipsis
#print(ar1)


#07 Rotate Array
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [6, 7, 9]])
#np.roll(arr, pos, axis) axis=0 means row and 1 mean col
rotated_matrix = np.roll(matrix1, 2, axis= 1)
print("ROTATED MATRIX Roll\n",rotated_matrix)
# k= 1 90 degree rotation, k=2, 180, k=3, 270
rotated_arr_90 = np.rot90(matrix1, k=1)
print("ROTATED MATRIX Ror90\n",rotated_arr_90)


#08 # Print 1st and 2nd maximun number of 2D array (unsorted)

arr = np.array([[9, 2, 3],
                [5, 9, 6],
                [7, 0, 5]])

arr = arr.flatten()
arr.sort()
print(arr)
m = max(arr)

for i in arr[::-1]:
    if i < m:
        m2 = i
        break
print("Result", m, i)

#09 Array Element replace and display specific elements, Slicing [row, col]

arr = np.array([[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15]])
print("Original Array \n", arr)
print("Result first\n", arr[1, 1:3])

print("2nd Result\n", arr[0:2, 2])

arr[0:2 , 2] = [25 , 25]
print(arr)

print(arr[1:3, 3:6])

#10 Create a 4X2 integer array and Prints its attributes
arr = np.empty([4,2], dtype = np.uint16) 
print("Printing Array")
print(arr)
print("Shape", arr.shape)
print("Array Dimension", arr.ndim)
print("The Length of each element of the array in bytes", arr.itemsize) # 
print("number of items", arr.size) 

#11 Create a 5X2 integer array from a range between 100 to 200 with dif each element is 10

arr = np.arange(100, 200, 10)
print(arr)
arr = arr.reshape(5,2)
print(arr)

#12 print third column from all rows
arr = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
print(arr[...,2])

#13 Printing array of odd rows and even columns

arr = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

res = arr[0::2 , 1::2]
print(res)

#14 two NumPy arrays add then square
arr1 = np.array([[5, 6, 9], [21 ,18, 27]])
arr2 = np.array([[15 ,33, 24], [4 ,7, 1]])
sum = arr1+arr2
sum =sum.flatten()
res = []

for i in sum:
    res.append(int(i*i))
print("res ",res)

res =np.array(res)
res = res.reshape(2,3)
print(res)

#15 Split the array into four equal-sized sub-arrays
arr = np.arange(10,34)
arr = arr.reshape(8,3)
arr = np.split(arr,4)
print(arr)

#16 Sort NumPy array specific row / col
arr = np.array([[34,43,73],[82,22,12],[53,94,66]])
res = np.sort(arr[1,...])
arr[1,...] = res
print(arr)

#17 max, min, sum of axis zero and exis one
arr = np.array([[34,43,73],[82,22,12],[53,94,66]])
minOfAxisOne = np.amin(arr, 1) 
print("minOfAxisOne =", minOfAxisOne)

minOfAxisZero = np.amax(arr, 0) 
print("minOfAxisZero =", minOfAxisZero)

SumOfAxisZero = np.sum(arr, 0) 
print("SumOfAxisZero =", SumOfAxisZero)


#18 print 1st and 3rd cols, hange 2nd col with new col
arr = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
newColumn = np.array([[10,10,10]])

# print 1st and 3rd cols
print(arr[::,::2])

# change 2nd col with new col
arr[...,1] = newColumn
print(arr)


#19 delete a col and then insert new one col
arr = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (arr)

arr = np.delete(arr , 1, axis = 1) 
print (arr)

new_col = np.array([[10,10,10]])

arr = np.insert(arr , 1, new_col, axis = 1) 
print (arr)


#20  Input = 3,5  output = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

input_str = "5,5"
dimensions=[int(x) for x in input_str.split(',')]
print("dimensions ",dimensions)
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
print ("multilist ", multilist)
print ("rowNum ", rowNum)
print ("colNum ", colNum)

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col

print ("multilist ",multilist)


