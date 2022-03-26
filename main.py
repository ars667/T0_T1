import math
import matplotlib.pyplot as plt
import numpy as np

name = input('название лазера - ')
number = int(input('количество точек = '))
T = np.zeros(number)
Ith = np.zeros(number)
Slope = np.zeros(number)
logith = np.zeros(number)
logslope = np.zeros(number)
for i in range(0, number):
    print('температура в точке', i, ' = ')
    T[i] = float(input())
for i in range(0, number):
    print('Ith в точке', i, ' = ')
    Ith[i] = float(input())
for i in range(0, number):
    print('Slope в точке', i, ' = ')
    Slope[i] = float(input())
for i in range(0, number):
    logith[i] = float((math.log(Ith[i]/Ith[0], math.e)))
    logslope[i] = float((math.log(Slope[i]/Slope[0], math.e)))
A = np.vstack([T, np.ones(len(T))]).T
m, c = np.linalg.lstsq(A, logith, rcond=None)[0]
print(m, c)
plt.xlabel('температура, C')
plt.ylabel('ln(Ith/Ith*)')
# plt.title('')
plt.plot(T, logith, 'o', label='эксперимент', markersize=5)
plt.plot(T, m*T + c, 'r', label='аппроксимация')
plt.legend()
# plt.show()
plt.savefig(name + 'T0.png')
B = np.vstack([T, np.ones(len(T))]).T
m2, c2 = np.linalg.lstsq(B, logslope, rcond=None)[0]
print(m2, c2)
plt.xlabel('температура, C')
plt.ylabel('ln(Slope/Slope*)')
plt.plot(T, logslope, 'o', label='эксперимент', markersize=5)
plt.plot(T, m2 * T + c2, 'r', label='аппроксимация')
plt.legend()
# plt.show()
plt.savefig(name + 'T1.png')
T00 = 1/m
T11 = -1 / m2
T00w = str(1/m)
T11w = str(-1 / m2)
print('T0 = ', T00w)
print('T1 = ', T11w)
f = open(name + '.txt', 'w')
f.write(name + '\n')
f.write('T0 = ' + T00w + '\n')
f.write('T1 = ' + T11w)
f.close()
