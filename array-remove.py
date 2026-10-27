import array

# inisialisasi array integer
arr_data = array.array('i', [1, 2, 3, 1, 5])

print("Array pertama:", end=" ")
for i in range(0, len(arr_data)):
    print(arr_data[i], end=" ")
print()

# pop() menghapus elemen pada indeks ke-2
print("Element yang dihapus adalah:", arr_data.pop(2))
print("Array setelah di-pop():", end=" ")
for i in arr_data:
    print(i, end=" ")
print()

# remove() menghapus kemunculan pertama nilai 1
arr_data.remove(1)
print("Array setelah proses remove:", end=" ")
for i in arr_data:
    print(i, end=" ")
print()