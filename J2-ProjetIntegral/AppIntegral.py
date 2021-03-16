from integral import midpoint, trapeze
from math import exp
def vt(t):
    return 3*t**2 * exp(t**3)

def xt(t):
    return exp(t**3) - 1
numMidpoint = midpoint(vt, 0, 1, 100)
numTrapeze = trapeze(vt, 0, 1, 100)
exact = xt(1) - xt(0)
erreurMidpoint = abs(exact - numMidpoint)
erreurTrapeze = abs(exact - numTrapeze)
print("Sol Exacte : ", exact)
print("Point Milieu: ", numMidpoint)
print("Trapeze : ", numTrapeze)
print("Erreur Point Milieu : ", erreurMidpoint)
print("Erreur Trapeze : ", erreurTrapeze)