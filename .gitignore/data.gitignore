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

def setupSimulation():
    sim = rebound.Simulation()
    sim.integrator = 'whfast'
    sim.add(m=1.3271244004193938E+11)
    sim.add(m=3.9860043543609598E+05, a=a1, f=f1)
    sim.add(m=3.9860043543609598E+05, a=a2, f=f2)
    sim.add(m=3.9860043543609598E+05, a=a3, f=f3)
    sim.add(m=3.9860043543609598E+05, a=a4, f=f4)
    sim.add(m=3.9860043543609598E+05, a=a5, f=f5)
    sim.move_to_com()
    sim.dt = .05
    return sim

sim = setupSimulation()
sim.exit_min_distance = 0.01
Noutputs = 10000
times = np.linspace(0,50000.*2.*np.pi,Noutputs)
distances = np.zeros(Noutputs)
ps = sim.particles # ps is now an array of pointers. It will update as the simulation runs.
try:
    for i,time in enumerate(times):
        sim.integrate(time)
        dp = ps[1] - ps[2]   # Calculates the coponentwise difference between particles
        distances[i] = np.sqrt(dp.x*dp.x+dp.y*dp.y+dp.z*dp.z)
except rebound.Encounter as error:
    print(error)


fig = plt.figure(figsize=(10,5)) #size of actual plot
ax = plt.subplot(111)
ax.set_title('1-2')
ax.set_xlabel("time [orbits]")
ax.set_xlim([0,sim.t/(2.*np.pi)])
ax.set_ylabel("distance")
plt.plot(times/(2.*np.pi), distances);
plt.plot([0.0,12],[0.01,0.01]);
fig.savefig('12')

sim = setupSimulation()
sim.exit_min_distance = 0.01
Noutputs = 10000
times = np.linspace(0,50000.*2.*np.pi,Noutputs)
distances = np.zeros(Noutputs)
ps = sim.particles # ps is now an array of pointers. It will update as the simulation runs.
try:
    for i,time in enumerate(times):
        sim.integrate(time)
        dp = ps[2] - ps[3]   # Calculates the coponentwise difference between particles
        distances[i] = np.sqrt(dp.x*dp.x+dp.y*dp.y+dp.z*dp.z)
except rebound.Encounter as error:
    print(error)


fig = plt.figure(figsize=(10,5)) #size of actual plot
ax = plt.subplot(111)
ax.set_title('2-3')
ax.set_xlabel("time [orbits]")
ax.set_xlim([0,sim.t/(2.*np.pi)])
ax.set_ylabel("distance")
plt.plot(times/(2.*np.pi), distances);
plt.plot([0.0,12],[0.01,0.01]);
fig.savefig('23')

sim = setupSimulation()
sim.exit_min_distance = 0.01
Noutputs = 10000
times = np.linspace(0,50000.*2.*np.pi,Noutputs)
distances = np.zeros(Noutputs)
ps = sim.particles # ps is now an array of pointers. It will update as the simulation runs.
try:
    for i,time in enumerate(times):
        sim.integrate(time)
        dp = ps[3] - ps[4]   # Calculates the coponentwise difference between particles
        distances[i] = np.sqrt(dp.x*dp.x+dp.y*dp.y+dp.z*dp.z)
except rebound.Encounter as error:
    print(error)


fig = plt.figure(figsize=(10,5)) #size of actual plot
ax = plt.subplot(111)
ax.set_title('3-4')
ax.set_xlabel("time [orbits]")
ax.set_xlim([0,sim.t/(2.*np.pi)])
ax.set_ylabel("distance")
plt.plot(times/(2.*np.pi), distances);
plt.plot([0.0,12],[0.01,0.01]);
fig.savefig('34')

sim = setupSimulation()
sim.exit_min_distance = 0.01
Noutputs = 10000
times = np.linspace(0,50000.*2.*np.pi,Noutputs)
distances = np.zeros(Noutputs)
ps = sim.particles # ps is now an array of pointers. It will update as the simulation runs.
try:
    for i,time in enumerate(times):
        sim.integrate(time)
        dp = ps[4] - ps[5]   # Calculates the coponentwise difference between particles
        distances[i] = np.sqrt(dp.x*dp.x+dp.y*dp.y+dp.z*dp.z)
except rebound.Encounter as error:
    print(error)

fig = plt.figure(figsize=(10,5)) #size of actual plot
ax = plt.subplot(111)
ax.set_title('4-5')
ax.set_xlabel("time [orbits]")
ax.set_xlim([0,sim.t/(2.*np.pi)])
ax.set_ylabel("distance")
plt.plot(times/(2.*np.pi), distances);
plt.plot([0.0,12],[0.01,0.01]);
fig.savefig('45')
