# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:10:50 2020

@author: celal
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from fileSystemView import FileSystemView

class MainWindows(QWidget):
    def __init__(self):
        super().__init__()
        self.folderPath=""
        self.dataClassesFilePath=""
        self.dataSupportFolderPath=""
        self.dataEpochsNumber=0
        self.checkedRadio=None
        self.checkedRadio_Image=None
        self.main_windows()

    def main_windows(self):

        # Page Building
        self.setGeometry(300, 300, 1200, 380)
        self.setMaximumSize(1200,390)
        self.setMinimumSize(1200,380)
        self.setStyleSheet("background: white;")
        self.setWindowTitle("Image Prosessing Create Dataset")
        self.setWindowIcon(QIcon('images/logo.png'))
        # Main Vertical Layout
        main_vertical_layout = QVBoxLayout(self)
        
        # Title
        v_layout_title = QVBoxLayout(self)
        self.title = QLabel(self)
        self.title.setScaledContents(True)
        self.title.setText("IMAGE PROSESSİNG CREATE DATASET")
        self.title.setFont(QFont("MS Shell Dlg 2",18,QFont.Bold))
        self.title.setStyleSheet("background-color:#c39435;color:#ffffff;border-radius:10px;border-style: solid;")
        self.title.setAlignment(Qt.AlignCenter)
        v_layout_title.addWidget(self.title)
        main_vertical_layout.addLayout(v_layout_title)

        # Selecet Folder Ui
        h_layout_select_folder = QHBoxLayout(self)
        
        # Select Folder Button
        self.select_folder_button = QPushButton(self)
        self.select_folder_button.setText("Select Folder")
        self.select_folder_button.setFont(QFont("MS Shell Dlg 2",10,QFont.Bold))
        self.select_folder_button.setStyleSheet("background:#2F41E6; color:#ffffff; border-radius:10px; border-style: 15px solid;")
        self.select_folder_button.clicked.connect(self.selectingFolder)
        #Size Policy
        sizePolicy = QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_folder_button.sizePolicy().hasHeightForWidth())
        self.select_folder_button.setSizePolicy(sizePolicy)
        
        # See Folder Path
        self.select_folder = QLabel(self)
        self.select_folder.setText(" ")
        self.select_folder.setAlignment(Qt.AlignLeft)
        self.select_folder.setAlignment(Qt.AlignVCenter)
        self.select_folder.setFont(QFont("MS Shell Dlg 2",10))
        self.select_folder.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")
        
        #Select Data Classes File Ui
        h_layout_select_data_classes_file = QHBoxLayout(self)

        # Select File Button
        self.select_data_classes_file_button = QPushButton(self)
        self.select_data_classes_file_button.setText(" Select Data Classes File ")
        self.select_data_classes_file_button.setFont(QFont("MS Shell Dlg 2",10,QFont.Bold))
        self.select_data_classes_file_button.setStyleSheet("background:#E72F55; color:#ffffff; border-radius:10px; border-style: 15px solid;")
        self.select_data_classes_file_button.clicked.connect(self.selectingDataClassesFile)

        # Size Policy
        sizePolicy = QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_data_classes_file_button.sizePolicy().hasHeightForWidth())
        self.select_data_classes_file_button.setSizePolicy(sizePolicy)

        # Line1
        v_line1 = QVBoxLayout()
        v_line1.setContentsMargins(20, -1, 20, -1)
        line1 = QFrame(self)
        line1.setToolTipDuration(-1)
        line1.setFrameShape(QFrame.HLine)
        line1.setFrameShadow(QFrame.Sunken)
        

        # See File Path
        self.select_data_classes_file =QLabel(self)
        self.select_data_classes_file.setText(" ")
        self.select_data_classes_file.setAlignment(Qt.AlignLeft)
        self.select_data_classes_file.setAlignment(Qt.AlignVCenter)
        self.select_data_classes_file.setFont(QFont("MS Shell Dlg 2",10))
        self.select_data_classes_file.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")

        # Line2
        v_line2 = QVBoxLayout()
        v_line2.setContentsMargins(20, -1, 20, -1)
        line2 = QFrame(self)
        line2.setToolTipDuration(-1)
        line2.setFrameShape(QFrame.HLine)
        line2.setFrameShadow(QFrame.Sunken)

        #epochs and options
        v_epochs_and_options = QVBoxLayout(self)

        #Write Epochs Ui
        h_epochs_layout = QHBoxLayout(self)

        # Write Epocs Number Label
        self.write_epochs_number_label = QLabel(self)
        self.write_epochs_number_label.setText(" Writing Data Epocs Numbers")
        self.write_epochs_number_label.setFont(QFont("MS Shell Dlg 2",10,QFont.Bold))
        self.write_epochs_number_label.setAlignment(Qt.AlignLeft)
        self.write_epochs_number_label.setAlignment(Qt.AlignVCenter)

        # Write Epocs Number LineEdit
        self.write_epochs_number = QLineEdit(self)
        self.write_epochs_number.setValidator(QIntValidator())   
        self.write_epochs_number.setPlaceholderText("Writing Data Epocs Numbers")
        self.write_epochs_number.setAlignment(Qt.AlignLeft)
        self.write_epochs_number.setAlignment(Qt.AlignVCenter)
        self.write_epochs_number.setFont(QFont("MS Shell Dlg 2",10))
        self.write_epochs_number.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")
        #SizePolicy
        sizePolicy = QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.write_epochs_number.sizePolicy().hasHeightForWidth())
        self.write_epochs_number.setSizePolicy(sizePolicy)

        # Groupbox Create İmage Options
        h_cio_layout = QHBoxLayout(self)

        group_box = QGroupBox(" Select Create Image Methods ")
        h_radio_layout = QHBoxLayout(self)
        self.create_new_dataset = QRadioButton("Create New Dataset")
        self.create_new_dataset.setChecked(True)
        self.create_dublicate_dataset = QRadioButton("Create Dublicate Dataset")
        h_radio_layout.addWidget(self.create_new_dataset)
        h_radio_layout.addWidget(self.create_dublicate_dataset)
        group_box.setLayout(h_radio_layout)
        self.create_new_dataset.setStyleSheet("border: 0px solid black;border-radius: 5px;background: white;")
        self.create_dublicate_dataset.setStyleSheet("border: 0px solid black;border-radius: 5px;background: white;")
        group_box.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")
        group_box.setAlignment(Qt.AlignTop)
        # Select Image Endwiths
        group_box_image_endswith = QGroupBox(" Select Image Endswith ")
        h_radio_layout_image_endwiths = QHBoxLayout(self)
        self.select_png = QRadioButton("PNG")
        self.select_png.setChecked(True)
        self.select_jpeg = QRadioButton("JPEG")
        self.select_jpg = QRadioButton("JPG")
        h_radio_layout_image_endwiths.addWidget(self.select_png)
        h_radio_layout_image_endwiths.addWidget(self.select_jpeg)
        h_radio_layout_image_endwiths.addWidget(self.select_jpg)
        group_box_image_endswith.setLayout(h_radio_layout_image_endwiths)
        self.select_png.setStyleSheet("border: 0px solid black;border-radius: 5px;background: white;")
        self.select_jpeg.setStyleSheet("border: 0px solid black;border-radius: 5px;background: white;")
        self.select_jpg.setStyleSheet("border: 0px solid black;border-radius: 5px;background: white;")
        group_box_image_endswith.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")

        # Line3
        v_line3 = QVBoxLayout()
        v_line3.setContentsMargins(20, -1, 20, -1)
        line3 = QFrame(self)
        line3.setToolTipDuration(-1)
        line3.setFrameShape(QFrame.HLine)
        line3.setFrameShadow(QFrame.Sunken)

        # Selecting Support Data Folder Ui
        h_support_data_layout =QHBoxLayout(self)
        # Select Support Data Folder Button
        self.select_support_data_folder_button = QPushButton(self)
        self.select_support_data_folder_button.setText(" Select Support Data Folder ")
        self.select_support_data_folder_button.setFont(QFont("MS Shell Dlg 2",10,QFont.Bold))
        self.select_support_data_folder_button.setStyleSheet("background:#26D35A; color:#ffffff; border-radius:10px; border-style: 15px solid;")
        self.select_support_data_folder_button.clicked.connect(self.selectingSupportDataFolder)
        #SizePolicy
        sizePolicy = QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_support_data_folder_button.sizePolicy().hasHeightForWidth())
        self.select_support_data_folder_button.setSizePolicy(sizePolicy)
        # See Folder Path
        self.select_support_data_folder = QLabel(self)
        self.select_support_data_folder.setText(" ")
        self.select_support_data_folder.setAlignment(Qt.AlignLeft)
        self.select_support_data_folder.setAlignment(Qt.AlignVCenter)
        self.select_support_data_folder.setFont(QFont("MS Shell Dlg 2",10))
        self.select_support_data_folder.setStyleSheet("border: 2px solid black;border-radius: 5px;background: white;")

        # Line4
        v_line4 = QVBoxLayout()
        v_line4.setContentsMargins(20, -1, 20, -1)
        line4 = QFrame(self)
        line4.setToolTipDuration(-1)
        line4.setFrameShape(QFrame.HLine)
        line4.setFrameShadow(QFrame.Sunken)

        # Control Button Ui
        v_control_layout = QVBoxLayout(self)
        # Control Button
        self.control_button = QPushButton(self)
        self.control_button.setText("CONTROL")
        self.control_button.setFont(QFont("MS Shell Dlg 2",25,QFont.Bold))
        self.control_button.setStyleSheet("background:#000FFA; color:#ffffff; border-radius:10px; border-style: 15px solid;")
        self.control_button.clicked.connect(self.showDataItemsControl)
        
        # Size Policy
        sizePolicy = QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.control_button.sizePolicy().hasHeightForWidth())
        self.control_button.setSizePolicy(sizePolicy)



        # Add layout widget
        #1
        h_layout_select_folder.addWidget(self.select_folder_button,1)
        h_layout_select_folder.addWidget(self.select_folder,4)
        h_layout_select_folder.setContentsMargins(20, 5, 20, 5)
        h_layout_select_folder.setSpacing(20)
        #2
        v_line1.addWidget(line1)
        #3
        h_layout_select_data_classes_file.addWidget(self.select_data_classes_file_button,1)
        h_layout_select_data_classes_file.addWidget(self.select_data_classes_file,4)
        h_layout_select_data_classes_file.setContentsMargins(20, 5, 20, 5)
        h_layout_select_data_classes_file.setSpacing(20)
        #4
        v_line2.addWidget(line2)
        #5
        #5.1
        h_epochs_layout.addWidget(self.write_epochs_number_label,1)
        h_epochs_layout.addWidget(self.write_epochs_number,4)
        h_epochs_layout.setContentsMargins(0, 0, 0,5)
        v_epochs_and_options.addLayout(h_epochs_layout,3)
        #5.2
        h_cio_layout.addWidget(group_box,1)
        h_cio_layout.addWidget(group_box_image_endswith,1)
        v_epochs_and_options.addLayout(h_cio_layout,3)
        v_epochs_and_options.setContentsMargins(20, 0, 20, -1)
        #6
        v_line3.addWidget(line3)
        #7
        h_support_data_layout.addWidget(self.select_support_data_folder_button,1)
        h_support_data_layout.addWidget(self.select_support_data_folder,4)
        h_support_data_layout.setContentsMargins(20, 5, 20, 5)
        h_support_data_layout.setSpacing(20)
        #8
        v_line4.addWidget(line4)
        #9
        v_control_layout.addWidget(self.control_button)
        v_control_layout.setContentsMargins(20, 0, 20, 5)
        v_control_layout.setSpacing(20)

        # Main
        main_vertical_layout.addLayout(h_layout_select_folder)
        main_vertical_layout.addLayout(v_line1)
        main_vertical_layout.addLayout(h_layout_select_data_classes_file)
        main_vertical_layout.addLayout(v_line2)
        main_vertical_layout.addLayout(v_epochs_and_options)
        main_vertical_layout.addLayout(v_line3)
        main_vertical_layout.addLayout(h_support_data_layout)
        main_vertical_layout.addLayout(v_line4)
        main_vertical_layout.addLayout(v_control_layout)
        
        # ALL Strech
        strech_list=[4,4,1,4,1,10,1,4,1,4]
        for i in range(len(strech_list)):
            main_vertical_layout.setStretch(i,strech_list[i])

        self.setLayout(main_vertical_layout)

    # Selecting Folder
    def selectingFolder(self):
        self.folderPath = str(QFileDialog.getExistingDirectory(self,"Please, Images saving for selecting folder"))
        self.select_folder.setText((self.folderPath))
        
    # Seleceting data classes file
    def selectingDataClassesFile(self):
        self.dataClassesFilePath = QFileDialog.getOpenFileName(self,"Please, Images classes types for selecting file",'',"Document Files (*.txt)")
        self.dataClassesFilePath = str(self.dataClassesFilePath[0])
        self.select_data_classes_file.setText(self.dataClassesFilePath)
    
    # Radio Checked
    def checked_control(self):
        if self.create_new_dataset.isChecked() == True:
            self.checkedRadio=0
        elif self.create_dublicate_dataset.isChecked() == True:
            self.checkedRadio=1
        else:
            self.checkedRadio=0

    def checked_control_image(self):
        if self.select_png.isChecked() == True:
            self.checkedRadio_Image=0
        elif self.select_jpeg.isChecked() == True:
            self.checkedRadio_Image=1
        elif self.select_jpg.isChecked() == True:
            self.checkedRadio_Image=2
        else:
            self.checkedRadio_Image=0

      # Selecting Folder
    def selectingSupportDataFolder(self):
        self.dataSupportFolderPath = str(QFileDialog.getExistingDirectory(self,"Please, Images saving for selecting folder"))
        self.select_support_data_folder.setText((self.dataSupportFolderPath))

    # Selected Folder Item List
    def showDataItemsControl(self):
        self.checked_control()
        self.checked_control_image()
        if self.write_epochs_number.text()!="":  
            self.dataEpochsNumber = int(self.write_epochs_number.text())
        if self.folderPath!="" and self.dataClassesFilePath!="" and self.dataEpochsNumber>0 and self.dataSupportFolderPath!="" and self.checkedRadio!=None  and self.checkedRadio_Image!=None:
            self.folderItemList=FileSystemView(self.folderPath,self.dataClassesFilePath,self.dataSupportFolderPath,self.dataEpochsNumber,self.checkedRadio,self.checkedRadio_Image)
            self.hide()
            self.folderItemList.show()
        else:    
            self.control_message()

    def control_message(self):
        self.message = QMessageBox(self)
        self.message.setWindowTitle("Error!!!!")
        self.message.setText("Please fill in the required fields")
        self.message.setWindowIcon(QIcon('images/error.png'))
        self.message.show()

def main():
    app = QApplication(sys.argv)
    main = MainWindows()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
  main()