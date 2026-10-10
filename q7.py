import numpy as np
def create_once_array():
    shape = tuple(map(int,input("Enter dimension separated by space(e.g. 2 3 for 2x3) : ").split()))
    arr = np.ones(shape)
    print ("\nArray filled with once :\n",arr)
def find_max_min():
    arr = np.array(list(map(int,input("Enter array elements separated by space : ").split())))
    print("Array:",arr)
    print("maximum value",np.max(arr))
    print("minimum value",np.min(arr))
def dot_product():
    arr1 = np.array(list(map(int,input("Enter element of first array: ").split())))
    arr2 = np.array(list(map(int,input("Enter element of second array: ").split())))
    if arr1.size != arr2.size:
        print ("Array must be of the same size for dot.")
    else:
        print ("dot product :",np.dot(arr1,arr2))
def reshape_array():
    arr = np.array(list(map(int, input("Enter elements of 1-D array: ").split())))
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    if rows * cols != arr.size:
        print("Cannot reshape array: total elements do not match.")
    else:
        reshaped = arr.reshape((rows, cols))
        print("Reshaped 2-D array:\n", reshaped)
while True:
    print("\nMenu:\n")
    print("a. Create an array filled with 1's \nb. Find maximum and minimum values from an array\nc. Dot product of 2 arrays\nd. Reshape a 1-D array to 2-D array\ne. Exit")
    choice = input("Enter your choice (a/b/c/d/e): ").lower()
    if choice == 'a':
        create_once_array()
    elif choice == 'b':
        find_max_min()
    elif choice == 'c':
        dot_product()
    elif choice == 'd':
        reshape_array()
    elif choice == 'e':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")