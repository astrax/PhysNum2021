from ProjectPi import PiLeibniz, PiEuler
from math import pi
n = 100
print("i", "ErrLeibniz", "ErrEuler", sep = "\t")
for i in range(n):
    ErrLeibniz = abs(pi-PiLeibniz(i))
    ErrEuler = abs(pi-PiEuler(i))
    print(i, ErrLeibniz, ErrEuler, sep = "\t")