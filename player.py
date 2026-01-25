import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

import os
import pygame
import sys

from tkinter import filedialog

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                             QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon
# Always use QTimer instead of importing 'time' module for GUI
# using 'time.sleep()' makes the GUI freeze, buttons stop responding, windows stop repainting, etc.
from PyQt5.QtCore import Qt, QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('audioplayer')
        self.setGeometry(700, 300, 600, 500)
        self.setWindowIcon(QIcon('app_icon.png'))
        self.folder_path = ""
        self.play = QPushButton("Play", self)
        self.is_paused = False
        self.skip = QPushButton("Skip", self)
        self.choose = QPushButton("Choose folder", self)
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
        grid.addWidget(self.skip, 0, 2)
        grid.addWidget(self.selected_folder, 2, 1)
        grid.addWidget(self.playing, 4, 1)
        grid.addWidget(self.error_text, 6, 1)

        grid.setAlignment(Qt.AlignTop)

        # self.setStyleSheet('''
        #     QLineEdit {
        #     }
                           
        #     QPushButton {
        #     }
        # ''')

        self.play.setCursor(Qt.PointingHandCursor)
        self.skip.setCursor(Qt.PointingHandCursor)
        self.choose.setCursor(Qt.PointingHandCursor)

        self.play.clicked.connect(self.playaudio)
        self.skip.clicked.connect(self.skip_audio)
        self.choose.clicked.connect(self.choose_folder)

        # set the index to '0' so we don't have to use a for loop
        # and when audio file (at index 0) finishes playing, we do 'self.index += 1'
        # to play next
        # i have it 1 here, to skip the first audio file, and start from 2nd
        self.index = 1
        pygame.mixer.init()
    

    def choose_folder(self):
        folder = filedialog.askdirectory()
        self.folder_path = folder + '/'
        self.selected_folder.setText(f"Selected folder: {self.folder_path}")
    
    def playaudio(self):
        try:
            if pygame.mixer.music.get_busy():
                self.play.setText("Pause")

            if not pygame.mixer_music.get_busy() and not self.is_paused:
                # Start / Play
                self.folder = self.folder_path
                self.audio_files = os.listdir(self.folder)
                self.timer.start(500)
                self.play_next()
                self.error_text.clear()

            elif not self.is_paused:
                # Pause
                pygame.mixer.music.pause()
                self.is_paused = True
                self.play.setText("Play")

            else:
                # Resume
                pygame.mixer.music.unpause()
                self.is_paused = False
                self.play.setText("Pause")

        except FileNotFoundError:
            self.error_text.setText("Folder not found")
        # get any other error and display it as readable error text
        except pygame.error:
            self.error_text.setText("Please select a folder with only audio files!")
        except Exception as e:
            self.error_text.setText(str(e))


    def play_next(self):
        try:
            if self.index >= len(self.audio_files):
                return
            
            file = self.audio_files[self.index]
            pygame.mixer.music.load(self.folder + file)
            pygame.mixer.music.play()
            self.playing.setText(f"Playing Now: {file}")
            print(f"Playing Now: {file}")

            self.index += 1
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
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            self.play_next()
        else:
            self.error_text.setText("No audio playing!")
        
        if self.index == len(self.audio_files):
            self.skip.setDisabled(True)
    

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()