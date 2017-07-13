import rebound
import numpy as np
from random import randint
from fractions import Fraction
import math
import random

##pbs script 16 times
with open('good.txt', 'a') as data:
    #SEMI MAJOR AXIS CALCULATION/RANDOMIZATION
    mu = (3.9860043543609598E+05/1.3271244004193938E+11)
    expo = Fraction('1/3')
    a1 = 0.99
    d = randint(11,13)
    c = ((2/3)*(mu))**expo
    R = (2*a1)/((2/c)-d)
    f1 = random.uniform(0, (2*math.pi))
    f2 = random.uniform(0, (2*math.pi))
    f3 = random.uniform(0, (2*math.pi))
    f4 = random.uniform(0, (2*math.pi))
    f5 = random.uniform(0, (2*math.pi))
    a2 = (a1 + (d*R))
    a3 = (a2 + (d*R))
    a4 = (a3 + (d*R))
    a5 = (a4 + (d*R))

    def setupSimulation():
        sim = rebound.Simulation()
        sim.integrator = "whfast"
        sim.add(m=1.3271244004193938E+11)
        sim.add(m=3.9860043543609598E+05, a=a1, f=f1)
        sim.add(m=3.9860043543609598E+05, a=a2, f=f2)
        sim.add(m=3.9860043543609598E+05, a=a3, f=f3)
        sim.add(m=3.9860043543609598E+05, a=a4, f=f4)
        sim.add(m=3.9860043543609598E+05, a=a5, f=f5)
        sim.dt = .050
        o1 = sim.particles[2].P/sim.particles[1].P
        o2 = sim.particles[3].P/sim.particles[2].P
        o3 = sim.particles[4].P/sim.particles[3].P
        o4 = sim.particles[5].P/sim.particles[4].P
        return sim

    sim = setupSimulation()
    sim.exit_min_distance = .010
    times = np.linspace(0,10e+9)
    ps = sim.particles
    counter = 0
    try:
        for time in times:
            sim.integrate(time)
            for p0, p1 in itertools.combinations(range(1, 6)):  # generates combinations of the particles numbered 1 thru 5
                dp = ps[p0] - ps[p1]
                distances[counter] = np.sqrt(dp.x*dp.x+dp.y*dp.y+dp.z*dp.z)
                counter += 1
    except rebound.Encounter as error:
        print(error)
