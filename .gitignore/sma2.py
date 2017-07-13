import rebound
import numpy as np
from random import randint
from fractions import Fraction
import math
import random
import matplotlib.pyplot as plt


##pbs script 16 times
#SEMI MAJOR AXIS CALCULATION/RANDOMIZATION
mu = (3.9860043543609598E+05/1.3271244004193938E+11)
expo = Fraction('1/3')
a1 = 0.99
d = 8.6
c = ((2/3)*(mu))**expo


f1 = random.uniform(0, (2*math.pi))
f2 = random.uniform(0, (2*math.pi))
f3 = random.uniform(0, (2*math.pi))
f4 = random.uniform(0, (2*math.pi))
f5 = random.uniform(0, (2*math.pi))


a2 = (a1+((d*c*a1)/2))/(1-((d*c)/2))
a3 = (a2+((d*c*a2)/2))/(1-((d*c)/2))
a4 = (a3+((d*c*a3)/2))/(1-((d*c)/2))
a5 = (a4+((d*c*a4)/2))/(1-((d*c)/2))

def P_dist(p1, p2):
    x = sim.particles[p1].x - sim.particles[p2].x
    y = sim.particles[p1].y - sim.particles[p2].y
    z = sim.particles[p1].z - sim.particles[p2].z
    dist = np.sqrt(x**2 + y**2 + z**2)
    return dist

sim = rebound.Simulation()
sim.integrator = "whfast"
sim.units = ('AU', 'yr', 'Msun')
sim.add(m=1.3271244004193938E+11)
sim.add(m=3.9860043543609598E+05, a=a1, f=f1)
sim.add(m=3.9860043543609598E+05, a=a2, f=f2)
sim.add(m=3.9860043543609598E+05, a=a3, f=f3)
sim.add(m=3.9860043543609598E+05, a=a4, f=f4)
sim.add(m=3.9860043543609598E+05, a=a5, f=f5)
sim.dt = .050

print(a1)
print(a2)
print(a3)
print(a4)
print(a5)

print('\n')
print(sim.particles[1].P)
print(sim.particles[2].P)
print(sim.particles[3].P)
print(sim.particles[4].P)
print(sim.particles[5].P)
print("-------------------------")

print('ORBITAL PERIOD RATIOS')

print(sim.particles[2].P/sim.particles[1].P)
print(sim.particles[3].P/sim.particles[2].P)
print(sim.particles[4].P/sim.particles[3].P)
print(sim.particles[5].P/sim.particles[4].P)
print("-------------------------")

fig = rebound.OrbitPlot(sim, trails=True, unitlabel="[AU]")
plt.show()
