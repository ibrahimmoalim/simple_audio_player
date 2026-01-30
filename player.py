import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

import os
import pygame
import sys

from pathlib import Path

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                             QGridLayout, QPushButton, QFileDialog)
from PyQt5.QtGui import QIcon
# Always use QTimer instead of importing 'time' module for GUI
# using 'time.sleep()' makes the GUI freeze, buttons stop responding, windows stop repainting, etc.
from PyQt5.QtCore import Qt, QTimer

# use all capital variable name for constant variables
# you cannot change them later
# "Path(__file__).resolve().parent" gets the absolute directory of this script
# (safe for loading assets like icons)
BASE_DIR = Path(__file__).resolve().parent


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('audioplayer')
        self.setGeometry(700, 300, 500, 300)
        self.setWindowIcon(QIcon(f'{BASE_DIR}/favicon.ico'))
        self.folder_path = ""
        self.choose = QPushButton("Choose folder", self)
        self.play = QPushButton("Play", self)
        self.pause = QPushButton("Pause", self)
        self.is_paused = False
        self.skip = QPushButton("Skip", self)
        self.stop = QPushButton("Stop", self)
        self.selected_folder = QLabel("")
        self.playing = QLabel("")
        self.error_text = QLabel("")
        # create a timer to periodically check if the current audio has finished,
        # so we can automatically play the next track without blocking the GUI
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_audio)
        self.initUI()

    def initUI(self):

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid = QGridLayout()
        central_widget.setLayout(grid)

        # grid.addWidget(self.textbox, 0, 0)
        grid.addWidget(self.choose, 0, 0)
        grid.addWidget(self.play, 0, 1)
        grid.addWidget(self.pause, 0, 2)
        grid.addWidget(self.skip, 0, 3)
        grid.addWidget(self.stop, 0, 4)
        grid.addWidget(self.selected_folder, 2, 1)
        grid.addWidget(self.playing, 4, 1)
        grid.addWidget(self.error_text, 6, 1)

        self.choose.setProperty('class', 'choose')
        self.play.setProperty('class', 'play')
        self.pause.setProperty('class', 'pause')
        self.skip.setProperty('class', 'skip')
        self.stop.setProperty('class', 'stop')

        grid.setAlignment(Qt.AlignTop)

        self.setStyleSheet('''
            QPushButton {
                font-weight: bold;
                font-size: 16px;
                font-family: Arial;
            }
                           
            QPushButton[class='choose'] {
                background-color: rgb(50, 180, 255);
            }
            
            QPushButton[class='play'] {
                background-color: lime;
            }
                           
            QPushButton[class='pause'] {
                background-color: rgb(155, 0, 255);
            }
            
            QPushButton[class='skip'] {
                background-color: rgb(250, 255, 0);
            }
                           
            QPushButton[class='stop'] {
                background-color: red;
            }
                           
            QLabel {
                font-weight: bold;
                font-size: 24px;
                font-family: Arial;
            }
        ''')

        self.choose.setCursor(Qt.PointingHandCursor)
        self.play.setCursor(Qt.PointingHandCursor)
        self.pause.setCursor(Qt.PointingHandCursor)
        self.skip.setCursor(Qt.PointingHandCursor)
        self.stop.setCursor(Qt.PointingHandCursor)

        self.play.clicked.connect(self.play_audio)
        self.pause.clicked.connect(self.pause_audio)
        self.skip.clicked.connect(self.skip_audio)
        self.stop.clicked.connect(self.stop_audio)
        self.choose.clicked.connect(self.choose_folder)


    def choose_folder(self):
        try:
            folder = QFileDialog.getExistingDirectory(self, 'Choose folder')
            self.folder_path = folder + '/'
            self.selected_folder.setText(f"Selected folder: {self.folder_path}")
        except TypeError:
            return
    
    def play_audio(self):
        try:

            pygame.mixer.init()
            self.folder = self.folder_path
            self.audio_files = os.listdir(self.folder)
            # set the index to '0' so we don't have to use a for loop
            # and when audio file (at index 0) finishes playing, we do 'self.index += 1'
            # to play next
            self.index = 0
            self.timer.start(500)
            self.play_next()
            self.error_text.clear()

        except FileNotFoundError:
            self.error_text.setText("Folder not found")
        # get any other error and display it as readable error text
        except Exception as e:
            self.error_text.setText(str(e))

    def pause_audio(self):
        if not pygame.mixer.get_init():
            self.error_text.setText("No audio playing!")
            return
        
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.pause.setText("Resume")
            self.pause.setStyleSheet("background-color: cyan;")
            self.is_paused = True
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.pause.setText("Pause")
            self.pause.setStyleSheet("background-color: rgb(155, 0, 255)")
            self.is_paused = False

    def play_next(self):
        try:
            # uncomment lines below to disable looping
            # if self.index >= len(self.audio_files):
            #     return
            
            file = self.audio_files[self.index]
            pygame.mixer.music.load(self.folder + file)
            pygame.mixer.music.play()
            self.playing.setText(f"Playing Now: {file}")
            print(f"Playing Now: {file}")
            
            self.index += 1

            if self.index >= len(self.audio_files):
                self.index = 0
            
        except pygame.error:
            self.error_text.setText("Please select a folder with only audio files!")
        except Exception as e:
            self.error_text.setText(str(e))


    def check_audio(self):
        # if audio is paused do not go to next file
        if self.is_paused:
            return
        
        if not pygame.mixer.music.get_busy():
            self.play_next()
            
    
    def skip_audio(self):
        if not pygame.mixer.get_init():
            self.error_text.setText("No audio playing!")
            return
        
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.play_next()
        else:
            self.error_text.setText("No audio playing!")

  
    def stop_audio(self):
        if not pygame.mixer.get_init():
            self.error_text.setText("No audio playing!")
            return
        
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.timer.stop()
            self.index = 0
            self.playing.clear()
            self.play.setText("Play")
            self.play.setStyleSheet("background-color: lime;")
        else:
            self.error_text.setText("No audio playing!")
    

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
