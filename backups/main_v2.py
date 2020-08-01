# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:10:50 2020

@author: celal
"""
import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from FileSystemView import FileSystemView

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    self.folderPath=""
    self.dataClassesFilePath=""
    
    super().__init__()
    
    self.mainwindowui()

  def mainwindowui(self):
    self.setWindowTitle("Image Prosessing Create Dataset")
    self.setMinimumSize(1200,700)
    self.setMaximumSize(1200,700)
    
    # Create Main Layout
    mainLayout = QtWidgets.QVBoxLayout(self)
    
    # Page Title
    self.title = QtWidgets.QLabel(self)
    self.title.setScaledContents(True)
    self.title.setText(" IMAGE PROSESSİNG CREATE DATASET ")
    self.title.setFont(QtGui.QFont("MS Shell Dlg 2",18,QtGui.QFont.Bold))
    self.title.setStyleSheet("background-color:#c39435;color:#ffffff;border-radius:10px;border-style: solid;")
    self.title.setAlignment(QtCore.Qt.AlignCenter)
    
    # Selecting Folder Ui
    # Create Horizantiol Layout
    seleceting_folder_ui_layout = QtWidgets.QHBoxLayout(self)
    seleceting_folder_ui_layout.setContentsMargins(0,20,0,100)
    # Select Folder Button
    self.select_folder_button = QtWidgets.QPushButton(self)
    self.select_folder_button.setText("Select Folder")
    self.select_folder_button.setFont(QtGui.QFont("MS Shell Dlg 2",8))
    self.select_folder_button.setStyleSheet("background:#00AAFF; color:#ffffff; border-radius:10px; border-style: 15px solid;")
    self.select_folder_button.clicked.connect(self.selectingFolder)
    self.select_folder_button.setSizePolicy(
        QtGui.QSizePolicy.Preferred,
        QtGui.QSizePolicy.Expanding)
    # See Folder Path
    self.select_folder = QtWidgets.QLabel(self)
    self.select_folder.setText(" Selected Folder : None")
    self.select_folder.setAlignment(QtCore.Qt.AlignLeft)
    self.select_folder.setAlignment(QtCore.Qt.AlignVCenter)
    self.select_folder.setFont(QtGui.QFont("MS Shell Dlg 2",8))
    self.select_folder.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")

    # Add Horizantiol Layout
    seleceting_folder_ui_layout.addWidget(self.select_folder_button,1)
    seleceting_folder_ui_layout.addWidget(self.select_folder,2)
    
    
    
    # Selecting File Ui
    # Create Horizantiol Layout
    select_data_classes_file_ui_layout = QtWidgets.QHBoxLayout(self)
    
    # Select File Button
    self.select_data_classes_file_button = QtWidgets.QPushButton(self)
    self.select_data_classes_file_button.setText(" Select Data Classes File")
    self.select_data_classes_file_button.setFont(QtGui.QFont("MS Shell Dlg 2",8))
    self.select_data_classes_file_button.setStyleSheet("background:#00AAFF; color:#ffffff; border-radius:10px; border-style: 15px solid;")
    self.select_data_classes_file_button.clicked.connect(self.selectingDataClassesFile)

    # See File Path
    self.select_data_classes_file = QtWidgets.QLabel(self)
    self.select_data_classes_file.setText(" Selected Data Classes File : None")
    self.select_data_classes_file.setAlignment(QtCore.Qt.AlignLeft)
    self.select_data_classes_file.setAlignment(QtCore.Qt.AlignVCenter)
    self.select_data_classes_file.setFont(QtGui.QFont("MS Shell Dlg 2",8))
    self.select_data_classes_file.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")
    
    # Add Horizantiol Layout
    select_data_classes_file_ui_layout.addWidget(self.select_data_classes_file_button,1)
    select_data_classes_file_ui_layout.addWidget(self.select_data_classes_file,2)
    
    
    
    
    
    # Add Layouts
    mainLayout.addWidget(self.title,1)
    mainLayout.addLayout(seleceting_folder_ui_layout,2)
    mainLayout.addLayout(select_data_classes_file_ui_layout,2)

    # Create Widget
    widget = QtWidgets.QWidget()
    # Add Main Layout
    widget.setLayout(mainLayout)
    # Add Central Widget
    self.setCentralWidget(widget)
  
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