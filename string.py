### str - menggabungkan teks ###
x = "Sepeda"
y = "Motor"
z = x + y
print(z)  # output: SepedaMotor


### str - mengulang teks ###
x = "Sepeda"
a = x * 2
print(a)  # output: SepedaSepeda


### str - slicing dan index ###
x = "Sepeda"
b = x[:2]       # dua karakter pertama
c = x[2:]       # mulai indeks 2 hingga akhir
d = x[0] + x[5]

print(b)  # Se
print(c)  # peda
print(d)  # Sa


### str - alfanumerik ###
f = '4'
g = '5'
h = f + g
print(h)  # output: 45


### fungsi bawaan str ###
i = 'donat'
j = str.capitalize(i)
print(j)  # Donat



### fungsi bawaan str - len ###
r = "Suka Makan"
s = "Hobbi"
print(len(r))  # 10
print(len(s))  # 5


### fungsi bawaan str - isdigit ###
digit = '404'
nondigit = 'Empat Kosong Empat'
print(digit.isdigit())     # True
print(nondigit.isdigit())  # False


### fungsi bawaan str - replace ###
nama = 'Joko Susanto'
ganti = nama.replace('Joko', 'Aldi')
print(ganti)  # Aldi Susanto


### fungsi bawaan str - find ###
menu = "Nasi Padang"
caristring = "Padang"
print(menu.find(caristring))  # 5


