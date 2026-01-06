iimport numpy as np
import matplotlib.pyplot as plt


data = [1, 0, 1, 0, 1, 1, 0]
samples_per_bit = 200


nrz_signal = np.repeat([1 if bit == 1 else -1 for bit in data], samples_per_bit)

t_message = np.linspace(0, len(data), len(nrz_signal))

fc = 20 
carrier_wave = np.sin(2 * np.pi * fc * t_message)  

amplitude_signal = nrz_signal * carrier 

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t_message, nrz_signal)
plt.title("NRZ Message Signal")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t_message, carrier)
plt.title("Carrier Signal (20 Hz)")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t_message, am_signal)
plt.title("AM Modulated Signal")
plt.grid(True)

plt.tight_layout()
plt.savefig("amplots.pdf")
plt.show()

