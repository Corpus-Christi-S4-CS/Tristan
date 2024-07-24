import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,4*np.pi, 100)
y = np.sin(x)
print(x)
print(y)

plt.plot(x,y,"x-")
plt.show()