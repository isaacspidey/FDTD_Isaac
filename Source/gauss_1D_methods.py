import numpy as np

def gauss(t0, time_step, spread):
    pulse = np.exp(-0.5 * ((t0 - time_step) / spread) ** 2)
    return pulse