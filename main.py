import sys
import numpy as np
import sounddevice as sd
import time
import pyaudio
import wave
import wavio
from PyQt5 import QtWidgets 
import recUI
from rec import Recorder 

class RecApp(QtWidgets.QMainWindow, recUI.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.rec = Recorder()

        self.playButton.clicked.connect(self.playStart)
        self.recButton.clicked.connect(self.recStart)
        self.stopButton.clicked.connect(self.recStop)
        self.saveButton.clicked.connect(self.saveFile)

    def recStart(self):
        self.rec.start_recording()

    def recStop(self):
        self.rec.stop_recording()

    def playStart(self):
        self.recButton.setEnabled(False)
        self.rec.render_audio()
        duration = self.rec.duration()
        
        self.rec.playback()
        time.sleep(duration)
        self.rec.stop_playback()
        self.recButton.setEnabled(True)

    def saveFile(self):
        self.rec.render_audio()
        audio = self.rec.final_rec

        try:
            save_dialog = QtWidgets.QFileDialog()
            save_dialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
            file_path = save_dialog.getSaveFileName(self, 'Save as... File', './', filter='All Files(*.*);; Wave Files(*.wav)')

            if file_path[0]:
                self.file_path = file_path
                
                wavio.write(self.file_path[0], audio, self.rec.rate)

        except FileNotFoundError as why:
            self.error_box(why)
            pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = RecApp()
    ex.show()
    app.exec_()

if __name__ == "__main__":
    main()

