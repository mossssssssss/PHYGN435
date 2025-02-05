
import math
import cmath
import matplotlib.pyplot as plt

# System information, filled in with Snell's Law
wavelength = 633 # nm
d = 100 # nm
N1 = 1 # refractive index of air
phi1 = math.radians(70) # radians
N2 = 1.46 # refractive index of SiO2
phi2 = math.asin(N1 * math.sin(phi1) / N2) # radians
N3 = 3.872 - 0.037j # refractive index of Si
phi3 = cmath.asin(N2 * math.sin(phi2) / N3) # radians

# Fresnel equations
rp12 = (N2 * math.cos(phi1) - N1 * math.cos(phi2))/(N2 * math.cos(phi1) + N1 * math.cos(phi2))
rs12 = (N1 * math.cos(phi1) - N2 * math.cos(phi2))/(N1 * math.cos(phi1) + N2 * math.cos(phi2))
rp23 = (N3 * math.cos(phi2) - N2 * cmath.cos(phi3))/(N3 * math.cos(phi2) + N2 * cmath.cos(phi3))
rs23 = (N2 * math.cos(phi2) - N3 * cmath.cos(phi3))/(N2 * math.cos(phi2) + N3 * cmath.cos(phi3))

# Functions to calculate beta, RP, RS, Psi, and Del from equations 20, 19, 23, and 25
def beta_func(d):
    beta = 2 * math.pi * (d / wavelength) * N2 * math.cos(phi2)
    return beta

def RP_RS(beta):
    RP = (rp12 + rp23 * cmath.exp(-2j * beta))/(1 + rp12 * rp23 * cmath.exp(-2j * beta))
    RS = (rs12 + rs23 * cmath.exp(-2j * beta))/(1 + rs12 * rs23 * cmath.exp(-2j * beta))
    return RP, RS

def Psi_Del(RP, RS):
    Psi = math.degrees(cmath.atan(abs(RP)/abs(RS)).real)
    Del = math.degrees((cmath.log((RP/RS)/cmath.tan(math.radians(Psi)))/(1j)).real)
    if Del < 0:
        Del += 360
    return Psi, Del

# Call the functions for d = 100 nm
beta = beta_func(d)
RP, RS = RP_RS(beta)
Psi, Del = Psi_Del(RP, RS)
print("Psi: ", Psi, "\nDel: ", Del)

# This next part is just for funsies, to show that our code recreates Figure 3-6
# This is the whole reason I even bothered with defining functions above
del_points = []
psi_points = []
all_dels = []
all_psis = []
d = 0
for i in range(280):
    beta = beta_func(d)
    RP, RS = RP_RS(beta)
    Psi, Del = Psi_Del(RP, RS)
    all_psis.append(Psi)
    all_dels.append(Del)
    if d % 10 == 0:
        del_points.append(Del)
        psi_points.append(Psi)
    d += 1

plt.scatter(psi_points, del_points)
plt.plot(all_psis, all_dels)
plt.xlim(0, 90)
plt.ylim(0, 360)
plt.xlabel('Psi (degrees)')
plt.ylabel('Delta (degrees)')
plt.title('Psi vs Delta')
plt.show()