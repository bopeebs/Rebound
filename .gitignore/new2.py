import rebound
import numpy as np
from random import randint
from fractions import Fraction
import math
import random
import matplotlib.pyplot as plt

mu = (3.9860043543609598E+05/1.3271244004193938E+11) #planet 2 star mass ratio
expo = Fraction('1/3')
c = ((2/3)*(mu))**expo #constant in formula for mutual hill radius

#f1-f5 = true anomoly/phase angle
f1 = random.uniform(0, (2*math.pi))
f2 = random.uniform(0, (2*math.pi))
f3 = random.uniform(0, (2*math.pi))
f4 = random.uniform(0, (2*math.pi))
f5 = random.uniform(0, (2*math.pi))

d = 3 #delta value

#a1-a5 are the semi major axis
a1 = 0.99
a2 = (a1+((d*c*a1)/2))/(1-((d*c)/2))
a3 = (a2+((d*c*a2)/2))/(1-((d*c)/2))
a4 = (a3+((d*c*a3)/2))/(1-((d*c)/2))
a5 = (a4+((d*c*a4)/2))/(1-((d*c)/2))

#function calculating the distances between adjacent bodies
def P_dist(p1, p2):
    x = sim.particles[p1].x - sim.particles[p2].x
    y = sim.particles[p1].y - sim.particles[p2].y
    z = sim.particles[p1].z - sim.particles[p2].z
    dist = np.sqrt(x**2 + y**2 + z**2)
    return dist

#simulation setup
sim = rebound.Simulation()
sim.integrator = "whfast"
sim.units = ('AU', 'yr', 'Msun')
sim.add(m=1.3271244004193938E+11)
sim.add(m=3.9860043543609598E+05, a=a1, f=f1)
sim.add(m=3.9860043543609598E+05, a=a2, f=f2)
sim.add(m=3.9860043543609598E+05, a=a3, f=f3)
sim.add(m=3.9860043543609598E+05, a=a4, f=f4)
sim.add(m=3.9860043543609598E+05, a=a5, f=f5)
sim.dt = .050 #timestep, .05 yr


#array of initial periods before simulation
init_periods = [sim.particles[1].P,sim.particles[2].P,sim.particles[3].P,sim.particles[4].P,sim.particles[5].P]

#np.linspace allows me to use a beginning and ending time for simulation time
#This try and except will integrate from t = 0 UNTIL a close encounter happens or until 10 billion years is reached


sim.exit_min_distance = (a1*(mu/3)**expo)
times = np.linspace(0,10e+9*2.*np.pi)

try:
    for i,time in enumerate(times):
        sim.integrate(time)
except rebound.Encounter as error:
    print(error)

try:
    sim.integrate(10e+9*2.*np.pi)
except rebound.Encounter as error:
    print(error)
'''
#calculates the distances between adjacent planet pairs from the array init_periods
for i in range(len(sim.particles)-1):
    distance = P_dist(i, i+1)
    print(i,":",i+1, '=', distance)
    if distance <= sim.exit_min_distance: #returns the period ratio of the two planets that had the close enecounter and the inner orbital period between the two
        p_r = init_periods[i+1]/init_periods[i]
        inner_period = init_periods[i]
        with open('good.txt', 'a') as data: #opens a file writing the x & y values for the graph
            data.write(str(math.log10(sim.t/inner_period)))
            data.write('\n')
            data.write(str(p_r))
            data.write('\n')

print("Inner Period:", inner_period)
print("Stabibility Time:", sim.t)
print("Period Ratio:", p_r)
for i in range(len(init_periods)):
    print('Planet', i+1, '=', init_periods)
'''
