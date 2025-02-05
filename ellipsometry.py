
# Margaux's version

import math
import cmath

wavelength = 633 # nm
d = 100 # film thickness, in nm
N1 = 1 # refractive index of air
phi1 = math.radians(70) # radians
N2 = 1.46 # refractive index of SiO2
phi2 = math.asin(N1 * math.sin(phi1) / N2) # radians
N3 = 3.872 - 0.037j # refractive index of Si
phi3 = cmath.asin(N2 * math.sin(phi2) / N3) # radians

rp12 = (N2 * math.cos(phi1) - N1 * math.cos(phi2))/(N2 * math.cos(phi1) + N1 * math.cos(phi2))
rs12 = (N1 * math.cos(phi1) - N2 * math.cos(phi2))/(N1 * math.cos(phi1) + N2 * math.cos(phi2))
rp23 = (N3 * math.cos(phi2) - N2 * cmath.cos(phi3))/(N3 * math.cos(phi2) + N2 * cmath.cos(phi3))
rs23 = (N2 * math.cos(phi2) - N3 * cmath.cos(phi3))/(N2 * math.cos(phi2) + N3 * cmath.cos(phi3))

beta = (2 * math.pi * N2 * d * math.cos(phi2)) / wavelength

RP = (rp12 + rp23 * cmath.exp(-2j * beta))/(1 + rp12 * rp23 * cmath.exp(-2j * beta))
RS = (rs12 + rs23 * cmath.exp(-2j * beta))/(1 + rs12 * rs23 * cmath.exp(-2j * beta))

Psi = math.degrees(cmath.atan(abs(RP)/abs(RS)).real)
print(Psi)
Del = math.degrees((cmath.log((RP/RS)/cmath.tan(math.radians(Psi)))/(1j)).real)
print(Del)
