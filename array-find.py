import array

arr_data = array.array('i', [1, 2, 3, 1, 2, 5])

print("Array asli:", end=" ")
for i in arr_data:
    print(i, end=" ")
print()

print("Index elemen dengan nilai 2:", arr_data.index(2))
print("Index elemen dengan nilai 1:", arr_data.index(1))