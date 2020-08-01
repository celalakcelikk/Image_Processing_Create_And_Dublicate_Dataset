# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:10:50 2020

@author: celal
"""
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from FileSystemView import FileSystemView

class MainWindow(QtWidgets.QWidget):
  def __init__(self):
    self.folderPath=""
    self.dataClassesFilePath=""
    super().__init__()
    self.mainwindowui()
  def mainwindowui(self):

    self.pageBuilded()

    self.pageTitle()
    
    self.selectFolderUi()

    self.selectDataClassesFileUi()

  # select Data Classes File Ui
  def selectDataClassesFileUi(self):
    # Select File Button
    self.select_data_classes_file_button = QtWidgets.QPushButton(self)
    self.select_data_classes_file_button.setText(" Select Data Classes File")
    self.select_data_classes_file_button.setFont(QtGui.QFont("MS Shell Dlg 2",8))
    self.select_data_classes_file_button.setStyleSheet("background:#00AAFF; color:#ffffff; border-radius:10px; border-style: 15px solid;")
    self.select_data_classes_file_button.resize(160,35)
    self.select_data_classes_file_button.move(20,132)
    self.select_data_classes_file_button.clicked.connect(self.selectingDataClassesFile)

    # See File Path
    self.select_data_classes_file = QtWidgets.QLabel(self)
    self.select_data_classes_file.setText(" Selected Data Classes File : None")
    self.select_data_classes_file.setAlignment(QtCore.Qt.AlignLeft)
    self.select_data_classes_file.setAlignment(QtCore.Qt.AlignVCenter)
    self.select_data_classes_file.setFont(QtGui.QFont("MS Shell Dlg 2",8))
    self.select_data_classes_file.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")
    self.select_data_classes_file.resize(960,35)
    self.select_data_classes_file.move(200,132)
  
  # Selecet Folder Ui
  def selectFolderUi(self):
    
    # Select Folder Button
    self.select_folder_button = QtWidgets.QPushButton(self)
    self.select_folder_button.setText("Select Folder")
    self.select_folder_button.setFont(QtGui.QFont("MS Shell Dlg 2",8))
    self.select_folder_button.setStyleSheet("background:#00AAFF; color:#ffffff; border-radius:10px; border-style: 15px solid;")
    self.select_folder_button.resize(160,35)
    self.select_folder_button.move(20,82)
    self.select_folder_button.clicked.connect(self.selectingFolder)

    # See Folder Path
    self.select_folder = QtWidgets.QLabel(self)
    self.select_folder.setText(" Selected Folder : None")
    self.select_folder.setAlignment(QtCore.Qt.AlignLeft)
    self.select_folder.setAlignment(QtCore.Qt.AlignVCenter)
    self.select_folder.setFont(QtGui.QFont("MS Shell Dlg 2",8))
    self.select_folder.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")
    self.select_folder.resize(960,35)
    self.select_folder.move(200,82)
  
  # DrawLine
  def paintEvent(self, event):
    self.painter = QtGui.QPainter(self)
    self.painter.setPen(QtCore.Qt.black)
    self.painter.drawLine(25,125,1155,125)
    self.painter.end()
    self.painter1 = QtGui.QPainter(self)
    self.painter1.setPen(QtCore.Qt.black)
    self.painter1.drawLine(25,175,1155,175)
    self.painter1.end()

  # Page building
  def pageBuilded(self):
    self.setStyleSheet("background: white;")
    self.setWindowTitle("Image Prosessing Create Dataset")
    self.setMinimumSize(1200,700)
    self.setMaximumSize(1200,700)

  # Title
  def pageTitle(self):
    self.title = QtWidgets.QLabel(self)
    self.title.setScaledContents(True)
    self.title.setText("IMAGE PROSESSİNG CREATE DATASET")
    self.title.setFont(QtGui.QFont("MS Shell Dlg 2",18,QtGui.QFont.Bold))
    self.title.setStyleSheet("background-color:#c39435;color:#ffffff;border-radius:10px;border-style: solid;")
    self.title.setAlignment(QtCore.Qt.AlignCenter)
    self.title.resize(600, 50)
    self.title.move(300,20)

  # Selecting Folder
  def selectingFolder(self):
    self.folderPath = str(QtWidgets.QFileDialog.getExistingDirectory(self,"Please, Images saving for selecting folder"))
    self.select_folder.setText((" Selected Folder : "+self.folderPath))
    self.showDataItemsControl()

 # Seleceting data classes file
  def selectingDataClassesFile(self):
    self.dataClassesFilePath = QtWidgets.QFileDialog.getOpenFileName(self,"Please, Images classes types for selecting file",'',"Document Files (*.txt)")
    self.dataClassesFilePath = str(self.dataClassesFilePath[0])
    self.select_data_classes_file.setText(" Selected Data Classes File : "+self.dataClassesFilePath)
    self.showDataItemsControl()

  # Selected Folder Item List
  def showDataItemsControl(self):
      if self.folderPath!="" and self.dataClassesFilePath!="":
        self.folderItemList=FileSystemView(self.folderPath,self.dataClassesFilePath)
        self.folderItemList.show()

def main():
  app = QtWidgets.QApplication(sys.argv)
  main = MainWindow()
  main.showMaximized()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()