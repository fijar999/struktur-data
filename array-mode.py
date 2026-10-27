# menggunakan array khusus
import array as arr
import numpy as np

array_1 = arr.array("i", [3, 6, 9, 12])
print(array_1)
print(type(array_1))


array_data = np.array([3, 6, 9, 12])
division = array_data / 3
print(division)
print(type(division))

list_data = [3, 6, 9, 12]
# Baris berikut menghasilkan TypeError jika dijalankan:
# division = list_data / 3