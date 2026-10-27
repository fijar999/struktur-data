beli1 = 'Tomat'
beli2 = 'Kangkung'
beli3 = 'Bayam'
beli = ['Tomat', 'Kangkung', 'Bayam']
print(beli)

beli = ['Tomat', 'Kangkung', 'Bayam']
cetak = beli[0]
print(cetak)  # Tomat

beli = ['Tomat', 'Kangkung', 'Bayam']
for x in beli:
    print(x)

beli = ['Tomat', 'Kangkung', 'Bayam']
panjang = len(beli)
print(panjang)  # 3

ambil = []
ambil.append('Mangga')
ambil.append('Jeruk')
print(ambil)  # ['Mangga', 'Jeruk']

sayur = ['Kol', 'Wortel', 'Buncis', 'Toge']
sayur.pop(1)
print(sayur)  # ['Kol', 'Buncis', 'Toge']

sayur = ['Kol', 'Wortel', 'Buncis', 'Toge']
sayur.remove('Buncis')
print(sayur)  # ['Kol', 'Wortel', 'Toge']

bunga = ['Melati', 'Mawar', 'Anggrek']
bunga.clear()
print(bunga)  # []


motor = ['Yamaha', 'Honda', 'Suzuki']
motor2 = motor.copy()
print(motor2)


mahasiswa = ['Harry', 'John', 'Maya', 'Brisya', 'John']
jumlah = mahasiswa.count('John')
print(jumlah)  # 2


siswa = ['Juki', 'Ahmad', 'Roni']
siswabaru = ['Maya', 'Ari', 'Aji']
siswa.extend(siswabaru)
print(siswa)


kota = ['Jakarta', 'Bandung', 'Surabaya', 'Makasar']
x = kota.index('Bandung')
print(x)  # 1


fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
print(fruits)  # ['apple', 'orange', 'banana', 'cherry']


angka = [1, 2, 3, 4, 5]
angka.reverse()
print(angka)  # [5, 4, 3, 2, 1]


cars = ['Ford', 'BMW', 'Volvo']
angka = [1, 6, 7, 3, 2, 5]
cars.sort()
angka.sort()
print(cars)   # ['BMW', 'Ford', 'Volvo']
print(angka)  # [1, 2, 3, 5, 6, 7]