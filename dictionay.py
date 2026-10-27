### membuat dictionary ###
# dictionary dengan key integer
Dict = {1: 'Apple', 2: 'For', 3: 'A'}
print(Dict)

# dictionary dengan key campuran
Dict = {'Name': 'Apple', 1: [1, 2, 3, 4]}
print(Dict)

# dictionary kosong
Dict = {}
print("Empty Dictionary:")
print(Dict)

# menggunakan dict()
Dict = dict({1: 'Apple', 2: 'For', 3: 'A'})
print(Dict)

# setiap item berupa pasangan
Dict = dict([(1, 'Apple'), (2, 'For')])
print(Dict)


### menambahkan elemen pada dictionary ###
Dict = {}
print("Empty Dictionary:")
print(Dict)

# menambahkan elemen satu per satu
Dict[0] = 'Apple'
Dict[2] = 'For'
Dict[3] = 1
print("Dictionary setelah menambahkan elemen:")
print(Dict)

# satu key memiliki tuple sebagai value
Dict['Value_set'] = 2, 3, 4
print("Dictionary setelah menambahkan Value_set:")
print(Dict)

# memperbarui value pada key yang sudah ada
Dict[2] = 'Welcome'
print("Key value yang di-update:")
print(Dict)

# menambahkan nested key
Dict[5] = {'Nested': {'1': 'Life', '2': 'Balance'}}
print("Menambahkan nested key:")
print(Dict)

### mengakses elemen pada dictioanry ###
Dict = {1: 'Apple', 'name': 'For', 3: 'Apple'}

print("Mengakses elemen dengan key:")
print(Dict['name'])
print(Dict[1])

# mengakses menggunakan get()
print("Mengakses elemen dengan get():")
print(Dict.get(3))


### mengakses elemen pada nested dictionary ###
Dict = {
    'Dict1': {1: 'Apple'},
    'Dict2': {'Name': 'For'}
}

print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])


### menghapus elemen pada dictionary ###
Dict = {1: 'Apple', 'name': 'For', 3: 'Apple'}

print("Dictionary =")
print(Dict)

del Dict[1]

print("Data setelah penghapusan Dictionary =")
print(Dict)


### metode pada dictionary ###
# demo beberapa metode dictionary
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# copy()
dict2 = dict1.copy()
print(dict2)

# clear()
dict1.clear()
print(dict1)

# get()
print(dict2.get(1))

# items() dan keys()
print(dict2.items())
print(dict2.keys())

# pop() menghapus key 4
dict2.pop(4)
print(dict2)

# popitem() menghapus pasangan terakhir
dict2.popitem()
print(dict2)

# update()
dict2.update({3: "Scala"})
print(dict2)

# values()
print(dict2.values())