import numpy as np 
import sounddevice as sd
import time 
import matplotlib.pyplot as plt

sample_rate = 44100
duration = 60.0
frequency = 440.0

x = np.linspace(0, duration * 2 * np.pi, int(duration * sample_rate))
sinewave_data = np.sin(frequency * x)

sinewave_data = sinewave_data * 0.3

fig, ax = plt.subplots()
ax.plot(sinewave_data)
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.title('Sine')
plt.show()


