import array

arr_data = array.array('i', [1, 2, 3, 1, 2, 5])

print("Array sebelum update:", end=" ")
for i in arr_data:
    print(i, end=" ")
print()

# update indeks 2 dengan nilai 6
arr_data[2] = 6
print("Array setelah update indeks 2:", end=" ")
for i in arr_data:
    print(i, end=" ")
print()

# update indeks 4 dengan nilai 8
arr_data[4] = 8
print("Array setelah update indeks 4:", end=" ")
for i in arr_data:
    print(i, end=" ")
print()