import rebound
import numpy as np
import math
import random
import matplotlib.pyplot as plt
from random import randint
from fractions import Fraction
mu = (3.9860043543609598E+05/1.3271244004193938E+11)
expo = Fraction('1/3')
c = ((2/3)*(mu))**expo
d = 3
a1 = 0.99
a2 = a1 * ((1+((d*c)/2))/(1-((d*c)/2)))
a3 = a2 * ((1+((d*c)/2))/(1-((d*c)/2)))
a4 = a3 * ((1+((d*c)/2))/(1-((d*c)/2)))
a5 = a4 * ((1+((d*c)/2))/(1-((d*c)/2)))

f1 = random.uniform(0, (2*math.pi))
f2 = random.uniform(0, (2*math.pi))
f3 = random.uniform(0, (2*math.pi))
f4 = random.uniform(0, (2*math.pi))
f5 = random.uniform(0, (2*math.pi))

sim = rebound.Simulation()
sim.integrator = "whfast"
sim.add(m=1.3271244004193938E+11)
sim.add(m=3.9860043543609598E+05, a=a1, f=f1)
sim.add(m=3.9860043543609598E+05, a=a2, f=f2)
sim.add(m=3.9860043543609598E+05, a=a3, f=f3)
sim.add(m=3.9860043543609598E+05, a=a4, f=f4)
sim.add(m=3.9860043543609598E+05, a=a5, f=f5)
sim.dt = .050
sim.exit_min_distance = .1#(a1*(mu/3)**expo)

try:
    sim.integrate(1000)
except rebound.Encounter as error:
    print(error)
    print(sim.t)
