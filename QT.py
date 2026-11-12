import math

V0 = float(input("Barrier Voltage: "))  
E = float(input("Energy of incident particle: "))
a = float(input("Define width: "))
Ediff = V0 - E
m = 9.10938*pow(10,-31)
hbar = 1.05457*pow(10,-34)    #Defining hbar 
k = math.sqrt(2*m*Ediff)/hbar                    #
hypsin = (math.sinh(k*a))**2
Denom = 1 + ((V0**2)*hypsin)/(4*E*Ediff)
T = 1/ Denom
print(T)
