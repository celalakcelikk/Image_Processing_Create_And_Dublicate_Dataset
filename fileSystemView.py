# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from createDataSetWindows import CreateDataSetWindows
from augmentedWindows import AugmentedWindows


class FileSystemView(QWidget):
  def __init__(self,folderPath,dataClassesFilePath,dataSupportFolderPath,dataEpochsNumber,checkedRadio,checkedRadio_Image=0):
    self.appWidth=1200
    self.appHeight=350
    self.folderPath = folderPath
    self.dataClassesFilePath=dataClassesFilePath
    self.dataSupportFolderPath=dataSupportFolderPath
    self.dataEpochsNumber=dataEpochsNumber
    self.checkedRadio=checkedRadio
    self.checkedRadio_Image=checkedRadio_Image
    self.image_endwith=".png"

    if self.checkedRadio_Image==1:
          self.image_endwith=".jpeg"
    if self.checkedRadio_Image==2:
          self.image_endwith=".jpg"
    else:
          self.image_endwith=".png"    

    super().__init__()
    self.showDataList()

  def showDataList(self):
    self.setWindowTitle("File System Viewer")
    self.setWindowIcon(QIcon('images/folder.png'))
    self.setGeometry(300, 300, self.appWidth, self.appHeight)
    v_mainlayout = QVBoxLayout(self)
    mainlayout = QHBoxLayout(self)

    layout_1 = QVBoxLayout(self)
    self.model = QFileSystemModel(self)
    self.model.setRootPath(self.folderPath)
    self.tree = QTreeView(self)
    self.tree.setModel(self.model)
    self.tree.setRootIndex(self.model.index(self.folderPath))
    self.tree.setColumnWidth(0, 125)
    self.tree.setAlternatingRowColors(True)
    self.folder_title = QLabel(self)
    self.folder_title.setText(" Selected Folder Items List ")
    self.folder_title.setFont(QFont("MS Shell Dlg 2",12))
    self.folder_title.setStyleSheet("border-radius:5px; border-style: 15px solid;")
    layout_1.addWidget(self.folder_title,alignment=Qt.AlignCenter)
    layout_1.addWidget(self.tree)

    layout_3 = QVBoxLayout(self)
    self.model = QFileSystemModel(self)
    self.model.setRootPath(self.dataSupportFolderPath)
    self.tree = QTreeView(self)
    self.tree.setModel(self.model)
    self.tree.setRootIndex(self.model.index(self.dataSupportFolderPath))
    self.tree.setColumnWidth(0, 125)
    self.tree.setAlternatingRowColors(True)
    self.folder_title = QLabel(self)
    self.folder_title.setText(" Selected Support Folder Items List ")
    self.folder_title.setFont(QFont("MS Shell Dlg 2",12))
    self.folder_title.setStyleSheet("border-radius:5px; border-style: 15px solid;")

    layout_3.addWidget(self.folder_title,alignment=Qt.AlignCenter)
    layout_3.addWidget(self.tree)

    layout_2 = QVBoxLayout(self)
    self.list_1 = QListWidget(self)
    response = [file.replace("\n","").strip(" ") for file in open(self.dataClassesFilePath,"r",encoding="utf-8")]
    self.list_1.addItems(response)
    self.data_list_title = QLabel(self)
    self.data_list_title.setText(" Selected Data Classes Items List ")
    self.data_list_title.setFont(QFont("MS Shell Dlg 2",12))
    self.data_list_title.setStyleSheet("border-radius:5px; border-style: 15px solid;")

    self.data_epochs_title = QLabel(self)
    self.data_epochs_title.setText(" Epochs Numbers ")
    self.data_epochs_title.setFont(QFont("MS Shell Dlg 2",12))
    self.data_epochs_title.setStyleSheet("border-radius:5px; border-style: 15px solid;")
    
    self.data_epochs = QLabel(self)
    self.data_epochs.setText(str(self.dataEpochsNumber))
    self.data_epochs.setFont(QFont("MS Shell Dlg 2",12))
    self.data_epochs.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")

    self.create_data_title = QLabel(self)
    self.create_data_title.setText(" Checked Radio Button Type ")
    self.create_data_title.setFont(QFont("MS Shell Dlg 2",12))
    self.create_data_title.setStyleSheet("border-radius:5px; border-style: 15px solid;")
    
    self.create_data = QLabel(self)
    if self.checkedRadio==0:    
      self.create_data.setText(str(self.checkedRadio)+" -> Create New Dataset")
    if self.checkedRadio==1:    
      self.create_data.setText(str(self.checkedRadio)+" -> Create Dublicate Dataset")
    self.create_data.setFont(QFont("MS Shell Dlg 2",12))
    self.create_data.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")
    
    layout_2.addWidget(self.data_epochs_title,alignment=Qt.AlignCenter)
    layout_2.addWidget(self.data_epochs)
    layout_2.addWidget(self.create_data_title,alignment=Qt.AlignCenter)
    layout_2.addWidget(self.create_data)
    layout_2.addWidget(self.data_list_title,alignment=Qt.AlignCenter)
    layout_2.addWidget(self.list_1)
    
    mainlayout.addLayout(layout_1,2)
    mainlayout.addLayout(layout_3,2)
    mainlayout.addLayout(layout_2,1)


    # back and next button
    h_back_and_next_button_layout = QHBoxLayout(self)
    # Back Windows Button
    self.back_window_button = QPushButton(self)
    self.back_window_button.setText(" Return To Previous Page ")
    self.back_window_button.setFont(QFont("MS Shell Dlg 2",15,QFont.Bold))
    self.back_window_button.setStyleSheet("background:#EC4A6F; color:#ffffff; border-radius:10px; border-style: 15px solid;")
    self.back_window_button.clicked.connect(self.openMainWindow)
    self.back_window_button.setIcon(QIcon('images/back_arrow.png'))
    self.back_window_button.setIconSize(QSize(20,20))
    #SizePolicy
    sizePolicy = QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.back_window_button.sizePolicy().hasHeightForWidth())
    self.back_window_button.setSizePolicy(sizePolicy) 

    # Next Windows Button
    self.next_window_button = QPushButton(self)
    self.next_window_button.setText(" Return To Next Page ")
    self.next_window_button.setFont(QFont("MS Shell Dlg 2",15,QFont.Bold))
    self.next_window_button.setStyleSheet("background:#DABF6A; color:#ffffff; border-radius:10px; border-style: 15px solid;")

    if self.checkedRadio==0:
          self.next_window_button.clicked.connect(self.openCreateDataSetWindows)
    elif self.checkedRadio==1:
          self.next_window_button.clicked.connect(self.openAugmentedWindows)
          
    self.next_window_button.setIcon(QIcon('images/next_arrow.png'))
    self.next_window_button.setIconSize(QSize(20,20))
    self.next_window_button.setLayoutDirection(Qt.RightToLeft)
    #SizePolicy
    sizePolicy = QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.next_window_button.sizePolicy().hasHeightForWidth())
    self.next_window_button.setSizePolicy(sizePolicy) 

    h_back_and_next_button_layout.addWidget(self.back_window_button)
    h_back_and_next_button_layout.addWidget(self.next_window_button)
    v_mainlayout.addLayout(mainlayout,7)
    v_mainlayout.addLayout(h_back_and_next_button_layout,1)
    self.setLayout(v_mainlayout)

  def openMainWindow(self):
    self.hide()
    from mainWindows import MainWindows
    self.mainwindow = MainWindows()
    self.mainwindow.show()
    
  def openCreateDataSetWindows(self):
    self.hide()
    self.createwindows  = CreateDataSetWindows(folderPath=self.folderPath,dataClassesFilePath=self.dataClassesFilePath,dataSupportFolderPath=self.dataSupportFolderPath,dataEpochsNumber=self.dataEpochsNumber,checkedRadio=self.checkedRadio)
    self.createwindows.show()
  
  def openAugmentedWindows(self):
    self.close()
    self.augmented = AugmentedWindows(folderPath=self.folderPath,dataClassesFilePath=self.dataClassesFilePath,checkedRadio_Image=self.checkedRadio_Image)
    self.augmented.show()
