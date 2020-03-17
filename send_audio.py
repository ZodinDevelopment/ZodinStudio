import os
import pyaudio
import numpy as np
import sounddevice as sd
import wave
import socket
import time

HEADERSIZE = 16

class Recorder(object):
    def __init__(self, channels=1, rate=44100, chunk=1024):
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self._pa = pyaudio.PyAudio()
        self._stream = None
        self.frames = []
        self.raw = None

    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        self.close()

    def start_recording(self):
        self._stream = self._pa.open(format=pyaudio.paInt16,
                                     channels=self.channels,
                                     rate=self.rate,
                                     input=True,
                                     frames_per_buffer=self.chunk,
                                     stream_callback=self.get_callback())
        self._stream.start_stream()
        return self

    def stop_recording(self):
        self._stream.stop_stream()
        return self

    def get_callback(self):
        def callback(in_data, frame_count, time_info, status):
            self.frames.append(in_data)
            return in_data, pyaudio.paContinue
        return callback

    def close(self):
        self._stream.close()
        self._pa.terminate()

    def compile_raw(self):
        self.raw = b''.join(self.frames)


    def total_frames(self):
        return len(self.frames) * self.chunk

    def clear_buffer(self):
        self.frames = []
        self.raw = None


def record(rec):
    input('Press enter to start recording')
    rec.start_recording()
    os.system('clear')
    input('Now recording, press enter to stop.')
    rec.stop_recording()
    rec.compile_raw()

    return rec.compile_raw()

def main():
    rec = Recorder()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 1234))
    s.listen(5)

    while True:
        clientsocket, address = s.accept()
        print('Connection success')
        audio = record(rec)

        option = str(input('Enter a command (record_more[r] / clear current [c] / send data [s], exit [x]'))

        option = option.strip()

        if option.lower() == 'r':
            new_raw = record(rec)
            audio += new_raw
            print('Appended to current buffer')

        elif option.lower() == 'c':
            rec.clear_buffer()

        elif option.lower() == 'x':
            sys.exit()

        elif option.lower() == 's':
            print('Sending current audio to client')

            msg = f'{len(audio):<{HEADERSIZE}}'
            msg = bytes(msg, "utf-8")
            full_msg = msg+audio

            clientsocket.send(full_msg)
            audio = None
            rec.close()

            rec = Recorder()
        else:
            print('Invalid Option')
            continue


if __name__ == "__main__":
    main()
