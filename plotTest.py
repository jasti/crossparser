import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1);
print type(x)
print x
y = np.sin(x)
print type(y)
plt.plot(x, y)
plt.show()