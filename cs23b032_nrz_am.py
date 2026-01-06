import numpy as np
import matplotlib.pyplot as plt

# Given data 
data = [1, 0, 1, 0, 1, 1, 0]
samples_per_bit = 200

# NRZ encoding (+1 for 1, -1 for 0)
nrz_signal = np.repeat([1 if bit == 1 else -1 for bit in data], samples_per_bit)
# time axis for the message 
t_message = np.linspace(0, len(data), len(nrz_signal))
