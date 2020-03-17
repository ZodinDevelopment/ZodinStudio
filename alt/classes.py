import numpy as np
import sounddevice as sd
import time 
import matplotlib.pyplot as plt
import wavio 

#config

class Wave(object):
    def __init__(self, sample_rate=44100, duration=3.0, frequency=440.0, ):

        self.sample_rate = sample_rate
        self.duration = duration
        self.frequency = frequency 

        self._generate()

    def _line_arr(self):
        d = self.duration
        s = self.sample_rate 

        x = np.linspace(0, d*2*np.pi, int(d*s))
        return x

    def _generate(self, attenuation=0.3):
        
        
        wave_data = np.sin(self.frequency * self._line_arr())

        self.wave_data = wave_data * attenuation

        
    def play(self):
        sd.play(self.wave_data, self.sample_rate)
        time.sleep(self.duration)
        sd.stop()

    def plot(self, sample_size=500, title='Wave Data'):
        plot_data = self.wave_data[:sample_size]

        fig, ax = plt.subplots()
        ax.plot(plot_data, linewidth=3)
        plt.xlabel('Sample Number')
        plt.ylabel('Amplitude')
        plt.title(str(title))
        plt.show()


