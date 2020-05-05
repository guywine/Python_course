import matplotlib.pyplot as plt
import numpy as np

#### 
fig, ax = plt.subplots(1,2)
fig.set_size_inches(7,3)

x = np.arange(0.0, 2, 0.01)
y = np.sin(4*np.pi*x)
ax[0].plot(x, y, color='black')

ax[0].fill_between(x, -1, 1, where=y > 0.5, facecolor='green', alpha=0.5)
ax[0].fill_between(x, -1, 1, where=y < -0.5, facecolor='red', alpha=0.5)


x = np.arange(0.0, 2, 0.01)
y = np.sin(4 * np.pi * x)

std = 0.2  # computed value
y_top = y + std
y_bot = y - std
ax[1].plot(x, y, color='black')

ax[1].fill_between(x, y_bot, y_top, facecolor='gray', alpha=0.5)


####
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
def g(t):
    return np.sin(t) * np.cos(1/(t+0.1))

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
fig2 = plt.figure()
ax1 = fig2.add_subplot(111)
ax1.plot(t1, g(t1), 'ro', t2, f(t2), 'k')  # two plots in the same call
ax1.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)

# Assigning labels to each plot (can be done during plotting)
f_label = r'$e^{-t}\cos(2 \pi t)$'
g_label = r'$\sin(t) \cdot \cos(\frac{1}{t + 0.1})$'
ax1.legend([g_label, f_label])
