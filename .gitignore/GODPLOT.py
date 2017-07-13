import rebound
import numpy as np
import matplotlib.pyplot as plt
import csv

#######################FORTMATTING##########################
############################################################
plt.figure(1)
plt.axis([0, 1, 0, 1])
plt.xlabel("P(i+1):Pi")

plt.ylabel("log(tc/to)")

plt.axvline(15/14, color = 'k')
plt.axvline(14/13, color = 'k')
plt.axvline(13/12, color = 'k')
plt.axvline(12/11, color = 'k')
plt.axvline(11/10, color = 'k')
plt.axvline(10/9, color = 'k')
plt.axvline(9/8, color = 'k')
plt.axvline(8/7, color = 'k')
plt.axvline(7/6, color = 'k')
plt.axvline(6/5, color = 'k')
plt.axvline(5/4, color = 'k')

plt.axvline(29/27, color = 'k', linestyle = '--')
plt.axvline(27/25, color = 'k', linestyle = '--')
plt.axvline(25/23, color = 'k', linestyle = '--')
plt.axvline(23/21, color = 'k', linestyle = '--')
plt.axvline(21/19, color = 'k', linestyle = '--')
plt.axvline(19/17, color = 'k', linestyle = '--')
plt.axvline(17/15, color = 'k', linestyle = '--')
plt.axvline(15/13, color = 'k', linestyle = '--')
plt.axvline(13/11, color = 'k', linestyle = '--')
plt.axvline(11/9, color = 'k', linestyle = '--')




######################I/O#########################
######################PLOT########################

x = []
y = []

with open('good.txt', 'r') as csvfile:
     plots = csv.reader(csvfile, delimiter=',')
     for row in plots:
         count = 0
         for line in csvfile:
            count+=1
            if count%2 == 0:
                x.append(float(line))
            elif count%2 != 0:
                y.append(float(line))


plt.plot([x], [y], 'ro')

plt.show()
