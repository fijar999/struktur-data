### akses elemen tuple - indexing dan negative indexing ###
# indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(letters[0])
print(letters[5])

# negative indexing
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(letters[-1])
print(letters[-3])


### akses elemen tuple - slicing ###
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

# elemen indeks 1 hingga sebelum indeks 4
print(my_tuple[1:4])

# elemen dari awal hingga sebelum indeks 2
print(my_tuple[:-7])

# elemen indeks 7 hingga akhir
print(my_tuple[7:])

# semua elemen
print(my_tuple[:])


### metode pada tuple ###
my_tuple = ('a', 'p', 'p', 'l', 'e')

print(my_tuple.count('p'))  # jumlah kemunculan 'p'
print(my_tuple.index('l'))  # indeks kemunculan pertama 'l'

# iterasi melalui tuple
languages = ('Python', 'Swift', 'C++')
for language in languages:
    print(language)

# memeriksa apakah item ada di tuple
print('C' in languages)       # False
print('Python' in languages)  # True