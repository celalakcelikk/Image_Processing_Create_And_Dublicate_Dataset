# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import walk
import cv2
import os
from augmented import *

class DublicateDataWindows(QWidget):
    def __init__(self,folderPath:list,dataClassesFilePath:list,checkedRadio_Image:int,checked_list:list,position_list:list,rotate_list:list,blur_list:list,central_crop_list:list,resize_list:list,adjust_brightness_list:list,noise_list:list,rgb_to_gray_list:list,rgb_to_bgr_list:list,bgr_to_gray_list:list,gray_to_rgb_list:list):
        
        self.checked_list = checked_list
        self.position_list = position_list
        self.rotate_list = rotate_list
        self.blur_list = blur_list
        self.central_crop_list = central_crop_list
        self.resize_list = resize_list
        self.adjust_brightness_list = adjust_brightness_list
        self.noise_list = noise_list
        self.rgb_to_gray_list = rgb_to_gray_list
        self.rgb_to_bgr_list = rgb_to_bgr_list
        self.bgr_to_gray_list = bgr_to_gray_list
        self.gray_to_rgb_list = gray_to_rgb_list
        
        self.folderPath = folderPath
        self.dataClassesFilePath = dataClassesFilePath
        self.checkedRadio_Image = checkedRadio_Image
        self.image_endwith=".png"

        if self.checkedRadio_Image==1:
            self.image_endwith=".jpeg"
        if self.checkedRadio_Image==2:
            self.image_endwith=".jpg"
        else:
            self.image_endwith=".png"

        self.image = []
        self.step=0
        self.folder_list=[]
        self.checked_list_true_count=0
        for i in self.checked_list:
            if i==1:
                self.checked_list_true_count+=1

        for line in open(dataClassesFilePath,"r",encoding="utf-8"):
            self.folder_list.append(line.replace("\n",""))

        super().__init__()
        self.dublicate_main_windondows()

    def dublicate_main_windondows(self):
        # Page Building
        self.setGeometry(300, 300, 1100, 320)
        self.setMaximumSize(1100,330)
        self.setMinimumSize(1100,320)
        self.setStyleSheet("background: white;")
        self.setWindowTitle("Image Prosessing Dublicate Dataset ")
        self.setWindowIcon(QIcon('images/plus.png'))
        v_main_layout = QVBoxLayout(self)

        # ProgressBar Ui        
        v_progressbar_layout = QVBoxLayout(self)

        self.augmented_main_title = QLabel(self)
        self.augmented_main_title.setText(" Augmented Class Name : {0}".format(self.folder_list[0]))
        self.augmented_main_title.setFont(QFont("MS Shell Dlg 2",20))

        self.augmented_progress_bar = QProgressBar(self)
        self.augmented_progress_bar.setGeometry(25, 25, 300, 40)
        self.augmented_progress_bar.setMaximum(self.checked_list_true_count)
        self.augmented_progress_bar.setValue(0)

        self.augmented_progress_bar.setFormat('{0} % ({1}/{2})'.format(int((100*0)/self.checked_list_true_count),0,self.checked_list_true_count))
        self.augmented_progress_bar.setAlignment(Qt.AlignCenter)

        self.augmented_progress_bar_title = QLabel(self)
        self.augmented_progress_bar_title.setText(" Augmented ProgressBar ")
        self.augmented_progress_bar_title.setFont(QFont("MS Shell Dlg 2",12))

        self.general_progress_bar = QProgressBar(self)
        self.general_progress_bar.setGeometry(25, 25, 300, 40)
        self.general_progress_bar.setMaximum(len(self.folder_list))
        self.general_progress_bar.setValue(0)
        self.general_progress_bar.setFormat('{0} % ({1}/{2})'.format(int((100*0)/len(self.folder_list)),0,len(self.folder_list)))
        self.general_progress_bar.setAlignment(Qt.AlignCenter)

        self.general_progress_bar_title = QLabel(self)
        self.general_progress_bar_title.setText(" General Class ProgressBar ")
        self.general_progress_bar_title.setFont(QFont("MS Shell Dlg 2",12))

        self.file_progress_bar = QProgressBar(self)
        self.file_progress_bar.setGeometry(25, 25, 300, 40)
        self.file_progress_bar.setValue(0)
        self.file_progress_bar.setFormat("")
        self.file_progress_bar.setAlignment(Qt.AlignCenter)

        self.file_progress_bar_title = QLabel(self)
        self.file_progress_bar_title.setText(" Folder Items ProgressBar ")
        self.file_progress_bar_title.setFont(QFont("MS Shell Dlg 2",12))
        
        # Start Button
        self.start_dublicate_image_button = QPushButton(self)
        self.start_dublicate_image_button.setText("Start Dublicate Dataset")
        self.start_dublicate_image_button.setFont(QFont("MS Shell Dlg 2",25,QFont.Bold))
        self.start_dublicate_image_button.setStyleSheet("background:#000FFA; color:#ffffff; border-radius:10px; border-style: 15px solid;")
        self.start_dublicate_image_button.clicked.connect(self.start_augmented_save_image)

        # Size Policy
        sizePolicy = QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_dublicate_image_button.sizePolicy().hasHeightForWidth())
        self.start_dublicate_image_button.setSizePolicy(sizePolicy)

        # Add Layot    
        v_progressbar_layout.addWidget(self.augmented_main_title,2,alignment=Qt.AlignCenter)
        v_progressbar_layout.addWidget(self.general_progress_bar_title,1,alignment=Qt.AlignCenter)
        v_progressbar_layout.addWidget(self.general_progress_bar,4)
        v_progressbar_layout.addWidget(self.augmented_progress_bar_title,1,alignment=Qt.AlignCenter)
        v_progressbar_layout.addWidget(self.augmented_progress_bar,4)
        v_progressbar_layout.addWidget(self.file_progress_bar_title,1,alignment=Qt.AlignCenter)
        v_progressbar_layout.addWidget(self.file_progress_bar,4)
        v_progressbar_layout.addWidget(QLabel(),1)
        v_progressbar_layout.addWidget(self.start_dublicate_image_button,1)

        # Add Main Layout
        v_main_layout.addLayout(v_progressbar_layout,1)
        self.setLayout(v_main_layout)


    def file_control(self,fileName:str):
        directory = self.folderPath+"\\"+fileName
        if os.path.isdir(directory):
                return True
        else:
                os.makedirs(directory)
                return True

    def image_save(self):

        for j in range(len(self.folder_list)):
            fileName = self.folder_list[j]
            result_bool = self.file_control(fileName=fileName)
            if result_bool:
                directory = str(self.folderPath+"/"+fileName)
                data_folder_list=[]
                data_folder_list_len=0
                folder_path =self.folderPath+"\\"+self.folder_list[j]

                for (dirpath, dirnames, filenames) in walk(folder_path):
                    data_folder_list.extend(filenames)
                try:
                    if data_folder_list!=[]:                                            
                        for line in data_folder_list:
                            if line.endswith(self.image_endwith):
                                data_folder_list_len+=1
                    else:
                        data_folder_list_len=0
                except:
                    data_folder_list_len=0

                self.augmented_main_title.setText(" Augmented Class Name : {0}".format(fileName))
                self.file_progress_bar.setMaximum(data_folder_list_len)
                if data_folder_list_len>0:
                    for i in range(len(self.checked_list)):
                        if self.checked_list[i] == 1:
                            self.file_progress_bar.setFormat("100 % ({0}/{0})".format(data_folder_list_len))
                            self.file_progress_bar.setValue(data_folder_list_len)
                            for k in range(0,data_folder_list_len):
                                path = "{0}/{1}".format(directory,data_folder_list[k])
                                result_augmented = None
                                result_augmented = self.image_augmented(index=i,image_path=path)
                                augmentedPath="{0}/{1}{2}".format(directory,k+data_folder_list_len,self.image_endwith)
                                if type(result_augmented) != type(None):
                                    cv2.imwrite(augmentedPath, result_augmented)
                                    self.file_progress_bar.setFormat('{3} : {0} % ({1}/{2})'.format(int((100*(k+1))/data_folder_list_len),(k+1),data_folder_list_len,data_folder_list[k]))
                                    self.file_progress_bar.setValue(k+1)
                            self.augmented_progress_bar.setFormat('{0} % ({1}/{2})'.format(int((100*(i+1))/self.checked_list_true_count),i+1,self.checked_list_true_count))
                            self.augmented_progress_bar.setValue(i+1)

    def start_augmented_save_image(self):
        self.image_save()
        while self.step<len(self.folder_list):
            self.general_progress_bar.setFormat('{0} % ({1}/{2})'.format(int((100*(self.step+1))/len(self.folder_list)),self.step+1,len(self.folder_list)))
            self.general_progress_bar.setValue(self.step+1)
            self.step+=1
            if self.step == len(self.folder_list):
                self.general_progress_bar.setFormat('{0} % ({1}/{2})'.format(100,self.step,len(self.folder_list)))
                self.general_progress_bar.setValue(self.step+1)
        self.control_message()

    def control_message(self):
        self.message = QMessageBox(self)
        self.message.setWindowTitle("Dublicate Data")
        self.message.setText("Finished Augmented Data")
        self.message.setWindowIcon(QIcon('images/plus.png'))
        self.message.show()

    def image_augmented(self,index:int,image_path:str):
        control=0
        augmented_result_image = None

        # Position
        if self.position_list[index]==1:
            if control==0:
                augmented_result_image = horizantally_flipped(image_path,1)
                control=1
            else:
                augmented_result_image = horizantally_flipped(cv2.imread(image_path),0)
        
        elif self.position_list[index]==2:
            if control==0:
                augmented_result_image = vertically_flipped(image_path,1)
                control=1
            else:
                augmented_result_image = vertically_flipped(cv2.imread(image_path),0)
                
        # Rotate
        if self.rotate_list[index]!=0.0:
            if control==0:
                augmented_result_image = rotate_image(image_path,self.rotate_list[index],1)
                control=1
            else:
                augmented_result_image = rotate_image(cv2.imread(image_path),self.rotate_list[index],0)
        
        # Blur
        if self.blur_list[index]!=0:
            if control==0:
                augmented_result_image = blur_image(image_path,self.blur_list[index],1)
                control=1
            else:
                augmented_result_image = blur_image(cv2.imread(image_path),self.blur_list[index],0)
        
        # Central Crop
        if self.central_crop_list[index]!=0:
            if control==0:
                augmented_result_image = central_crop(image_path,self.central_crop_list[index],1)
                control=1
            else:
                augmented_result_image = central_crop(cv2.imread(image_path),self.central_crop_list[index],0)
        
        # Resize
        if self.resize_list[index][0]!=0 or self.resize_list[index][1]!=0:
            if control==0:
                augmented_result_image = image_resize(image_path,self.resize_list[index][0],self.resize_list[index][1],1)
                control=1
            else:
                augmented_result_image = image_resize(cv2.imread(image_path),self.resize_list[index][0],self.resize_list[index][1],0)
        
        # Adjust Brightness
        if self.adjust_brightness_list[index]!=0.0:
            if control==0:
                augmented_result_image = adjust_brightness(image_path,self.adjust_brightness_list[index],1)
                control=1
            else:
                augmented_result_image = adjust_brightness(cv2.imread(image_path),self.adjust_brightness_list[index],0)
        
        # Noise
        if self.noise_list[index]!=0:
            if control==0:
                augmented_result_image = image_adding_noise(image_path,1)
                control=1
            else:
                augmented_result_image = image_adding_noise(cv2.imread(image_path),0)
        
        # RGB to GRAY
        if self.rgb_to_gray_list[index]!=0:
            if control==0:
                augmented_result_image = rgb_to_gray(image_path,1)
                control=1
            else:
                augmented_result_image = rgb_to_gray(cv2.imread(image_path),0)
       
        # RGB to BGR
        if self.rgb_to_bgr_list[index]!=0:
            if control==0:
                augmented_result_image = rgb_to_bgr(image_path,1)
                control=1
            else:
                augmented_result_image = rgb_to_bgr(cv2.imread(image_path),0)
        
        # BGR to GRAY
        if self.bgr_to_gray_list[index]!=0:
            if control==0:
                augmented_result_image = bgr_to_gray(image_path,1)
                control=1
            else:
                augmented_result_image = bgr_to_gray(cv2.imread(image_path),0)

        # GRAY to RGB
        if self.gray_to_rgb_list[index]!=0:
            if control==0:
                augmented_result_image = gray_to_rgb(image_path,1)
                control=1
            else:
                augmented_result_image = gray_to_rgb(cv2.imread(image_path),0)

        return augmented_result_image
