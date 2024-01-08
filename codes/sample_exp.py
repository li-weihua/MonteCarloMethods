import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

n = 1000000

x1 = -np.log(1-np.random.rand(n))

# e^-x
x = np.linspace(0, 5, 10000)
y = np.exp(-x)

plt.hist(x1, bins=100, range=[0, 5], density=True)
plt.plot(x, y, 'r-')

plt.show()
plt.savefig('sample_exp.png')
