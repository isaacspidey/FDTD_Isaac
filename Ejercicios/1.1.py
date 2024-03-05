""" fd3d_1_1.py: 1D FDTD
Simulation in free space
"""

'''1.Get the program fd1d_1_1.py running. What happens when the pulse hits
the end of the array? Why?

Cuando el pulso llega al final del array rebota y vuelve invertido.

2. Modify the program so it has two sources, one at kc - 20 and one at kc +
20. (Notice that kc is the center of the problem space.) What happens when
the pulses meet? Explain this from basic electromagnetic (EM) theory.

Se suman los paquetes del pulso que van en direcciones contrarias en aproximadamente T=70

3. Instead of Ex as the source, use Hy at k = kc as the source. What difference
does it make? Try a two-point magnetic source at kc - 1 and kc such that
hy[kc - 1] = - hy[kc]. What does this look like? To what does it correspond physically?

Si pones la fuente como Hy se intercambian los comportamientos de los campos.
'''

import numpy as np
from math import exp
from matplotlib import pyplot as plt

ke = 200
ex = np.zeros(ke)
hy = np.zeros(ke)

# Pulse parameters
kc = int(ke / 2)
t0 = 40
spread = 12
nsteps = 41



# Main FDTD Loop
for time_step in range(1, nsteps + 1):

    # Calculate the Ex field
    for k in range(1, ke):
        ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

# Put a Gaussian pulse in the middle (Source ex)
    #pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
    #ex[kc] = pulse

#______________________Apartado 1_________________________
        
# Put a Gaussian pulse at kc-20 (Source ex)
    #pulse_minus = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
    #ex[kc-20] = pulse_minus

# Put a Gaussian pulse at kc+20 (Source ex)
    #pulse_plus = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
    #ex[kc+20] = pulse_plus
        
#______________________Apartado 2_________________________
        
# Put a Gaussian pulse in kc (Source hy)
    #pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
    #hy[kc] = pulse
        
#______________________Apartado 3_________________________        

# Put a Gaussian pulse at kc-1 (Source ex)
    pulse_minus = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
    hy[kc-1] = pulse_minus

# Put a Gaussian pulse at kc
    pulse_plus = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
    hy[kc] = -pulse_plus


# Calculate the Hy field
    for k in range(ke - 1):
        hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])




# Plot the outputs as shown in Fig. 1.2
plt.rcParams['font.size'] = 12
plt.figure(figsize=(8, 3.5))

plt.subplot(211)
plt.plot(ex, color='k', linewidth=1)
plt.ylabel('E$_x$', fontsize='14')
plt.xticks(np.arange(0, 201, step=20))
plt.xlim(0, 200)
plt.yticks(np.arange(-1, 1.2, step=1))
plt.ylim(-1.2, 1.2)
plt.text(100, 0.5, 'T = {}'.format(time_step),
horizontalalignment='center')

plt.subplot(212)
plt.plot(hy, color='k', linewidth=1)
plt.ylabel('H$_y$', fontsize='14')
plt.xlabel('FDTD cells')
plt.xticks(np.arange(0, 201, step=20))
plt.xlim(0, 200)
plt.yticks(np.arange(-1, 1.2, step=1))
plt.ylim(-1.2, 1.2)
plt.subplots_adjust(bottom=0.2, hspace=0.45)
plt.show()
