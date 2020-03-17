import pyaudio
import numpy as np
import sounddevice as sd
import wavio
import socket
import time

HEADERSIZE = 16
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100


def play_audio(audio, duration):

    sd.play(audio, RATE)
    time.sleep(duration)
    sd.stop()
    print('Finished')

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))
    print('Connected to server')
    while True:
        full_msg = b''
        while True:
            msg = s.recv(16)
            if len(msg) <= 0:
                break
            full_msg += msg

        if len(full_msg) > 0:
            full_msg = full_msg[HEADERSIZE:]
            total_frames = len(full_msg)
            duration = total_frames / RATE
            audio = np.fromstring(full_msg, dtype=np.int16)

            print('Received Audio')
            play_audio(audio, duration)
            break
    main()


if __name__ == "__main__":
    main()

