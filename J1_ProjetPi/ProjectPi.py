from math import sqrt, pi
def PiLeibniz(n):
    s = 0
    for i in range(n+1):
        s += 1/((4*i + 1)*(4*i + 3))
    s = s * 8 
    return s

def PiEuler(n):
    s = 0
    for i in range(1, n+1): 
        s += 1/(i*i)
    s = sqrt(6*s)
    return s

