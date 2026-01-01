def heisE():
    decide = int(input("Press '0' to calculate energy variation \nPress '1' to calculate time variation: "))
    if (decide == 0):
        t = float(input("Enter variation in time: "))
        power = int(input("Enter the power of 10 for t: "))
        E = (1/t*pow(10,power))*(h/4*pi)                                    #This Function uses the formula: (del)E.(del)t >= h/4*pi
        print(f"Variation in Energy is:{E} Joules")
    elif(decide == 1):
        E = float(input("Enter Variation in energy: "))
        power = int(input("Enter the power of 10 for E: "))
        t=(1/E*pow(10, power)) * (h / 4 * pi)
        print(f"Variation in Time is:{t} seconds")
        
def heisdis():
    decide = int(input("Press '0' to calculate displacement variation \nPress '1' to calculate momentum variation: "))
    if(decide == 0):
        p = float(input("Enter variation in momentum: "))
        power = int(input("Enter the power of 10 for momentum: "))
        x = (1/p*pow(10,power))*(h/4*pi)
        print(f"Variation in Displacement is {x} metres")
    elif (decide == 1):                                                     #This Function uses the formula: (del)p.(del)x >= h/4*pi
        x = float(input("Enter variation in displacement: "))
        power = int(input("Enter the power of 10 for displacement: "))
        p = (1 / x * pow(10, power)) * (h / 4 * pi)
        print(f"Variation in Momentum is {p} metres^2-seconds")

h = 6.626*pow(10,-34)
pi = 3.14159265358979323846   #Pi defined to 20 decimal places for higher accuracy
decide = 0
method= int(input("Enter '0' to calculate Variation in Energy/Time or Enter '1' to calculate Variation in Displacement/momentum: "))
if(method== 0):
    heisE()
elif(method==1):
    heisdis()
else:
    print("Invalid method/Undefined Method")

