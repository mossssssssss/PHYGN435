import math

# Gather user input
temperature = int(input("Enter the temperature in Celsius: "))
dry_input = input("Is the growth dry? Enter 'yes' or 'no': ").strip().lower()
dry = dry_input == "yes"
t0 = float(input("Enter the initial oxide thickness in micrometers: "))
time = float(input("Enter the growth time in hours: "))

# Table 4.1
table = [[800,0.370,0.0011,9,0,0],
 [920,0.235,0.0049,1.4,0.50,0.203],
  [1000,0.165,0.0117,0.37,0.226,0.287],
   [1100,0.090,0.027,0.076,0.11,0.510],
    [1200,0.040,0.045,0.027,0.05,0.720]]

# Figure out which line of the table this growth refers to based on temperature
row = None

for temp in range(5):
  if temperature == table[temp][0]:
    row = temp

if row == None:
  print("Temperature does not match presaved growth conditions. Accepted temperatures are 800, 920, 1000, 1100, and 1200.")
  exit()

# Differentiate if dry or wet growth
if dry:
  # Pick appropriate growth coefficients from the table
  A = table[row][1]
  B = table[row][2]
  if t0 == 0:
    # If there is no inital growth, find time taking rapid growth into account
    tau = table[row][3]
  else:
    # Use Deal-Grove for tau if there is inital growth
    tau = (t0**2 + A * t0)/B

else:
  # Pick appropriate growth coefficients from the table
  A = table[row][4]
  B = table[row][5]

  # Calculate tau for wet oxide, with or without intial growth, using Deal-Grove
  tau = (t0**2 + A * t0)/B

# Use Equation 4.11 to find thickness of oxide
tox = (-A + math.sqrt(A**2 + 4 * B * (time + tau)))/2
print("The oxide thickness for these parameters is", round(tox*1000), "nm.")