from ProjectPi import PiLeibniz, PiEuler
from math import pi
import matplotlib.pyplot as plt
n = 50
L1, L2, L3 = [], [], []
for i in range(n):
    ErrLeibniz = abs(pi-PiLeibniz(i))
    ErrEuler = abs(pi-PiEuler(i))
    L1.append(i)
    L2.append(ErrLeibniz)
    L3.append(ErrEuler)

plt.plot(L1, L2, label = "Erreur Leibniz")
plt.plot(L1, L3, label = "Erreur Euler")
plt.legend()