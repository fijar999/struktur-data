import array as arr

# membuat sebuah list lalu mengubahnya menjadi array
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = arr.array('i', l)

print("Initial Array:")
for i in a:
    print(i, end=" ")
print()

# cetak elemen dalam rentang tertentu
sliced_array = a[3:8]
print("\nAmbil elemen pada indeks 3 sampai sebelum 8:")
print(sliced_array)

# elemen mulai indeks 5 hingga akhir
sliced_array = a[5:]
print("\nElemen mulai indeks 5 hingga terakhir:")
print(sliced_array)

# semua elemen
sliced_array = a[:]
print("\nCetak semua elemen dengan operasi slice:")
print(sliced_array)

# seluruh array dalam urutan terbalik
print("\nArray terbalik:", a[::-1])