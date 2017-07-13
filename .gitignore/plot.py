import rebound
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
plt.axis([1.05, 1.30, 0, 10])
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


plt.show()
