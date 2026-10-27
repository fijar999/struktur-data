### membuat sebuah set ###
# set tipe integer
mahasiswa_id = {112, 114, 116, 118, 115}
print('Mahasiswa ID:', mahasiswa_id)

# set tipe string
huruf_vokal = {'a', 'e', 'i', 'o', 'u'}
print('Huruf Vokal:', huruf_vokal)

# set tipe data campuran
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Kumpulan tipe data campuran:', mixed_set)



### membuat set kosong ###
# membuat set kosong
empty_set = set()

# membuat dictionary kosong
empty_dictionary = {}

print('Jenis data dari empty_set:', type(empty_set))
print('Jenis data dari empty_dictionary:', type(empty_dictionary))



### duplikasi item dalam set ###
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)  # duplikasi dihilangkan otomatis


### menambahkan item pada set ###
numbers = {21, 34, 54, 12}
print('Initial Set:', numbers)

numbers.add(32)
print('Updated Set:', numbers)


### mengupdate item pada set ###
companies = {'UHB', 'UAD'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)
print(companies)


### remove item pada set ###
languages = {'Swift', 'Java', 'Python'}
print('Set Awal:', languages)

# discard() menghapus elemen jika ada tanpa error jika tidak ditemukan
removedValue = languages.discard('Java')
print('Set setelah menggunakan discard():', languages)



### fungsi bawaan set ###
fruits = {"Apple", "Peach", "Mango"}

# for loop untuk mengakses setiap elemen
for fruit in fruits:
    print(fruit)

even_numbers = {2, 4, 6, 8}
print('Set:', even_numbers)
print('Total Elements:', len(even_numbers))


### operasi pada set - onion ###
# first set
A = {2, 3, 5}
# second set
B = {1, 2, 6}

print('Union using |:', A | B)
print('Union using union():', A.union(B))


### operasi pada set - intersection ###
A = {1, 3, 5}
B = {1, 2, 3}

print('Intersection using &:', A & B)
print('Intersection using intersection():', A.intersection(B))


### operasi pada set - difference ###
A = {2, 3, 5}
B = {1, 2, 6}

print('Difference using -:', A - B)
print('Difference using difference():', A.difference(B))


### operasi pada set set - symmetric difference ###
A = {2, 3, 5}
B = {1, 2, 6}

print('Symmetric difference using ^:', A ^ B)
print('Symmetric difference using symmetric_difference():', A.symmetric_difference(B))


###periksa apakah dua set sama ###
A = {1, 3, 5}
B = {3, 5, 1}

if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')