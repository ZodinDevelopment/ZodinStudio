import pyaudio
import wave
import numpy as np 
import sounddevice as sd
import wavio 


class Recorder(object):
    def __init__(self, channels=1, rate=44100, chunk=1024):
        self.channels = channels
        self.rate = rate 
        self.chunk = chunk
        self._pa = pyaudio.PyAudio()
        self._stream = None
        self.frames = []
        self.final_rec = None
    def __enter__(self):
        return self

    def __exit__(self, exception, value, traceback):
        self.close()

    def start_recording(self):
        self._stream = self._pa.open(format=pyaudio.paInt16, channels=self.channels, rate=self.rate, input=True, frames_per_buffer=self.chunk, stream_callback=self.get_callback())

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

    def render_audio(self):
        raw = b''.join(self.frames)
        self.final_rec = np.fromstring(raw, dtype=np.int16)

        
    

    def playback(self):
        data = self.final_rec
        sd.play(data, self.rate)


    def stop_playback(self):
        sd.stop()

    def duration(self):
        total_frames = len(self.frames) * self.chunk 

        seconds = total_frames / self.rate 

        return seconds 

    def save_file(self, fname):

        wavio.write(fname, self.final_rec, self.rate)


