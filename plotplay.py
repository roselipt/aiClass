import numpy as np
import matplotlib.pyplot as plt

#evenly sampled time at 200ms intervals
t=np.arange(0., 5., 0.2)

#red dashes, blue squared and green triangle

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'b^')
plt.show()
