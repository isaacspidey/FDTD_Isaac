import numpy as np
from math import exp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ke = 200
ex = np.zeros(ke)
hy = np.zeros(ke)

t0 = 40
spread = 12

boundary_low = [0, 0]
boundary_high = [0, 0]

#__________solo para onda sinusoidal__________
ddx = 0.01 # Cell size
dt = ddx / 6e8 # Time step size
freq_in = 700e6
#_____________________________________________

# Create Dielectric Profile
cb = np.ones(ke)
cb = 0.5 * cb
cb_start = 100
epsilon = 4
cb[cb_start:] = 0.5 / epsilon
nsteps = 700

# Main FDTD Loop
frames = []

for time_step in range(1, nsteps + 1):
    # Calculate the Ex field
    for k in range(1, ke):
        ex[k] = ex[k] + cb[k] * (hy[k - 1] - hy[k])

    # Put a Gaussian pulse at the low end
    #pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
    #ex[5] = pulse + ex[5]

    #Put a sinusoidal soft source at the low end
    pulse = np.sin(2 *np.pi * freq_in * dt * time_step)
    ex[5] = pulse + ex[5]

    # Absorbing Boundary Conditions
    ex[0] = boundary_low.pop(0)
    boundary_low.append(ex[1])

    #ex[ke - 1] = boundary_high.pop(0)
    #boundary_high.append(ex[ke - 2])

    # Calculate the Hy field
    for k in range(ke - 1):
        hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    frames.append(np.copy(ex))

# Create animation
fig, ax = plt.subplots()
line, = ax.plot([], [], color='k', linewidth=1)
ax.set_ylabel('E$_x$', fontsize='14')
ax.set_xticks(np.arange(0, 199, step=20))
ax.set_xlim(0, 199)
ax.set_yticks(np.arange(-0.5, 1.2, step=0.5))
ax.set_ylim(-0.5, 1.2)
ax.plot((0.5 / cb - 1) / 3, 'k--', linewidth=0.75)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(range(ke), frames[i])
    ax.set_title('Simulation of a pulse hitting a dielectric medium')
    return line,

anim = FuncAnimation(fig, animate, init_func=init, frames=len(frames), interval=50, blit=True)
plt.xlabel('FDTD cells')
plt.show()
