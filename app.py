# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from pytube import Playlist
import os
from PyQt5.QtCore import *



class Ui_MainWindow(object):
    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(392, 317)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(110, 250, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.convertButton.setFont(font)
        self.convertButton.setObjectName("convertButton")
        self.mainLabel = QtWidgets.QLabel(self.centralwidget)
        self.mainLabel.setEnabled(True)
        self.mainLabel.setGeometry(QtCore.QRect(40, -10, 311, 121))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mainLabel.setFont(font)
        self.mainLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mainLabel.setStyleSheet("background-image: url(./assets/img/logo.png);")
        self.mainLabel.setText("")
        self.mainLabel.setTextFormat(QtCore.Qt.AutoText)
        self.mainLabel.setPixmap(QtGui.QPixmap("./assets/img/logo.png"))
        self.mainLabel.setScaledContents(True)
        self.mainLabel.setObjectName("mainLabel")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(20, 160, 341, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()
        self.urlPrompt = QtWidgets.QLabel(self.centralwidget)
        self.urlPrompt.setEnabled(True)
        self.urlPrompt.setGeometry(QtCore.QRect(90, 60, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.urlPrompt.setFont(font)
        self.urlPrompt.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.urlPrompt.setAutoFillBackground(False)
        self.urlPrompt.setTextFormat(QtCore.Qt.AutoText)
        self.urlPrompt.setScaledContents(False)
        self.urlPrompt.setAlignment(QtCore.Qt.AlignCenter)
        self.urlPrompt.setObjectName("urlPrompt")
        self.statusText = QtWidgets.QLabel(self.centralwidget)
        self.statusText.setEnabled(True)
        self.statusText.setGeometry(QtCore.QRect(20, 180, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.statusText.setFont(font)
        self.statusText.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.statusText.setAutoFillBackground(False)
        self.statusText.setText("")
        self.statusText.setTextFormat(QtCore.Qt.AutoText)
        self.statusText.setScaledContents(False)
        self.statusText.setAlignment(QtCore.Qt.AlignCenter)
        self.statusText.setObjectName("statusText")
        self.urlLabel = QtWidgets.QLineEdit(self.centralwidget)
        self.urlLabel.setGeometry(QtCore.QRect(20, 110, 341, 21))
        self.urlLabel.setObjectName("urlLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.convertButton.clicked.connect(self.buttonClicked)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Youtube Playlist Converter"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))
        self.urlPrompt.setText(_translate("MainWindow", "Enter the Youtube playlist URL below:"))
    
    
    def buttonClicked(self):
        
        
        if(len(self.urlLabel.text()) == 0):
            self.urlPrompt.setText("Invalid URL")
        
        else:
            if(self.convertButton.text() == "Cancel"):
                exit()
            elif(self.convertButton.text() == "Done"):
                exit()
            else:
                self.progressBar.show()
                self.urlLabel.hide()
                self.urlPrompt.hide()
                self.convertButton.setText("Cancel")
                self.statusText.setText("Clearing songs folder...")
                self.worker = WorkerThread(self.urlLabel.text())
                self.worker.start()
                self.worker.finished.connect(self.evt_worker_finished)
                self.worker.update_progress.connect(self.evt_update_progress)
                
    def evt_worker_finished(self):
        print("Done!")
        self.progressBar.setValue(100)
        self.statusText.setText("Download complete!\nYou can now exit this screen")
        self.convertButton.setText("Done")
        
    def evt_update_progress(self, val):
        self.progressBar.setValue(val["bar"])
        self.statusText.setText(val["song"])
        self.statusText.setWordWrap(True)
            
            
class WorkerThread(QThread):
    
    def __init__(self, url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = url
    
    update_progress = pyqtSignal(dict)
    
    def run(self):
        dir = './songs'
        progress = {"bar" : 0, "song" : ""}
        self.update_progress.emit(progress)
        numberOfFiles = 0
        numberDeleted = 0
        for path in os.listdir(dir):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir, path)):
                numberOfFiles += 1
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
            numberDeleted += 1
            progress["bar"] = (int((numberDeleted/numberOfFiles)*100))
            self.update_progress.emit(progress)

                    

                
        #Checking whether the URL entered exists
        try:
            p = Playlist(self.url)
        except KeyError:
            print("You the url you entered is invalid!")
            exit()
        except Exception:
            print("Error - Problem with the app!")
            exit()

                
                
        numberOfSongs = len(p.videos)
        songsDownloaded = 0

        #Download every video in the YouTube playlist

        for video in p.videos:
                    
            progress["bar"] = int((songsDownloaded/numberOfSongs)*100)
            progress["song"] = video.title
            self.update_progress.emit(progress)
            path = dir + './' + video.title+ '.mp3'
            if(os.path.exists(path)):
                print(f'{video.title} already exist!')
                songsDownloaded +=1
                continue
                    
                        
            stream = video.streams.filter(only_audio=True, mime_type='audio/mp4').order_by('abr').desc().first()
            try:
                out_file = stream.download(output_path='./songs')
            except:
                print(f'{video.title} download has failed...')
                songsDownloaded +=1
                continue

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            songsDownloaded += 1 
            print(songsDownloaded)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
