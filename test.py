import numpy as np
import matplotlib.pyplot as plt


with open('buffer_out.txt', 'r') as file:
    data = file.readlines()


complex_numbers = []
for line in data:
    x, y = map(float, line.strip().split(','))
    x = x / 2 ** 11
    y = y / 2 ** 11
    complex_numbers.append(complex(x, y))


real_parts = [z.real for z in complex_numbers]
imaginary_parts = [z.imag for z in complex_numbers]


oner = np.ones(10)
real_parts = np.convolve(real_parts, oner)
imaginary_parts = np.convolve(imaginary_parts, oner)

plt.figure(figsize=(10, 10))
plt.subplot(2,1,1)
plt.scatter(real_parts, imaginary_parts, marker='.')


plt.title('График комплексных чисел')
plt.xlabel('Действительная часть')
plt.ylabel('Мнимая часть')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
# plt.xlim(-1000, 1000)
# plt.ylim(-1000, 10000)
plt.subplot(2,1,2)
plt.plot(real_parts, label = "Реальная часть")
plt.plot(imaginary_parts, label = "Мнимая часть")
plt.legend()


plt.show()