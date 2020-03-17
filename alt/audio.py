import numpy as np
import sounddevice as sd
import wavio
import time 
import matplotlib.pyplot as plt

SAMPLE_RATE = 44100

def setup_array(duration, sample_rate=SAMPLE_RATE):

    return np.linspace(0, duration * 2 np.pi, int(duration * sample_rate))


def sine_wave(f, x):

    return np.sin(f * x)

def attenuate(wave, amount=0.3):

    return wave * amount


def play(wave_data, duration, sample_rate=SAMPLE_RATE):
    print("Playing")
    sd.play(wave_data, sample_rate)
    time.sleep(duration)
    sd.stop()
    print("Finished")

def plot_wave


