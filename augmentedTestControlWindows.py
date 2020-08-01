# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import walk
import cv2
import os
from augmented import *

class ControlAugmentedWindows(QWidget):
    def __init__(self,checked_list:list,position_list:list,rotate_list:list,blur_list:list,central_crop_list:list,resize_list:list,adjust_brightness_list:list,noise_list:list,rgb_to_gray_list:list,rgb_to_bgr_list:list,bgr_to_gray_list:list,gray_to_rgb_list:list):
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
        self.original_image_path = './images/cat.jpg'
        super().__init__()
        self.mainWindows()
    
    def mainWindows(self):
        
        # Page Building
        self.setGeometry(400, 100, 1100, 840)
        self.setMaximumSize(1100,850)
        self.setMinimumSize(1100,840)
        self.setStyleSheet("background: white;")
        self.setWindowTitle("Augmented Assignment Control")
        self.setWindowIcon(QIcon('images/plus.png'))

        
        self.title = QLabel(self)
        self.title.setScaledContents(True)
        self.title.setText("Augmented Assignment Control".upper())
        self.title.setFont(QFont("MS Shell Dlg 2",18,QFont.Bold))
        self.title.setStyleSheet("background-color:#c39435;color:#ffffff;border-radius:10px;border-style: solid;")
        self.title.setAlignment(Qt.AlignCenter)

        # main layout
        v_main_layout = QVBoxLayout(self)

        # original image
        v_original_data_layout = QVBoxLayout(self)
        h_layout_original_image = QHBoxLayout(self)
        self.original_image_title = QLabel(self)
        self.original_image_title.setText(" Original Image ")
        self.original_image_title.setFont(QFont("MS Shell Dlg 2",12))    
        self.original_image=QLabel(self)
        self.original_image.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
        self.original_image.setPixmap(QPixmap(self.original_image_path))
        self.original_image.setScaledContents(True)

        #add Widget
        v_original_data_layout.addWidget(self.original_image_title,alignment=Qt.AlignCenter)
        h_layout_original_image.addWidget(QLabel(" "),1)
        h_layout_original_image.addWidget(self.original_image,1)
        h_layout_original_image.addWidget(QLabel(" "),1)

        v_original_data_layout.addLayout(h_layout_original_image)
        
        #Grid Layout
        grid_layout = QGridLayout(self)

        # 1.Augmented
        v_layout_augmented_1_image = QVBoxLayout(self)
        self.augmented_1_image_title = QLabel(self)
        self.augmented_1_image_title.setText(" 1. Augmented Image")
        self.augmented_1_image_title.setFont(QFont("MS Shell Dlg 2",12))    
        self.augmented_1_image=QLabel(self)
        self.augmented_1_image.setStyleSheet("border: 5px solid black;border-radius: 1augmented_0px;background: white;")
        
        if self.checked_list[0]==1:
            augmented_result_image_path_1 = self.image_augmented(index=0,image_path=self.original_image_path)
            self.augmented_1_image.setPixmap(QPixmap(augmented_result_image_path_1))
        else:
            self.augmented_1_image.setPixmap(QPixmap(self.original_image_path))
        # self.augmented_1_image.setPixmap(QPixmap(self.original_image_path))
        self.augmented_1_image.setScaledContents(True)

        # add Widget
        v_layout_augmented_1_image.addWidget(self.augmented_1_image_title,alignment=Qt.AlignCenter)
        v_layout_augmented_1_image.addWidget(self.augmented_1_image)
 
        # 2.Augmented
        v_layout_augmented_2_image = QVBoxLayout(self)
        self.augmented_2_image_title = QLabel(self)
        self.augmented_2_image_title.setText(" 2. Augmented Image")
        self.augmented_2_image_title.setFont(QFont("MS Shell Dlg 2",12))    
        self.augmented_2_image=QLabel(self)
        self.augmented_2_image.setStyleSheet("border: 5px solid black;border-radius: 1augmented_0px;background: white;")
        if self.checked_list[1]==1:
            augmented_result_image_path_2 = self.image_augmented(index=1,image_path=self.original_image_path)
            self.augmented_2_image.setPixmap(QPixmap(augmented_result_image_path_2))
        else:
            self.augmented_2_image.setPixmap(QPixmap(self.original_image_path))
        self.augmented_2_image.setScaledContents(True)

        # add Widget
        v_layout_augmented_2_image.addWidget(self.augmented_2_image_title,alignment=Qt.AlignCenter)
        v_layout_augmented_2_image.addWidget(self.augmented_2_image)

        # 3.Augmented
        v_layout_augmented_3_image = QVBoxLayout(self)
        self.augmented_3_image_title = QLabel(self)
        self.augmented_3_image_title.setText(" 3. Augmented Image")
        self.augmented_3_image_title.setFont(QFont("MS Shell Dlg 2",12))    
        self.augmented_3_image=QLabel(self)
        self.augmented_3_image.setStyleSheet("border: 5px solid black;border-radius: 1augmented_0px;background: white;")
        if self.checked_list[2]==1:
            augmented_result_image_path_3 = self.image_augmented(index=2,image_path=self.original_image_path)
            self.augmented_3_image.setPixmap(QPixmap(augmented_result_image_path_3))
        else:
            self.augmented_3_image.setPixmap(QPixmap(self.original_image_path))
        self.augmented_3_image.setScaledContents(True)

        # add Widget
        v_layout_augmented_3_image.addWidget(self.augmented_3_image_title,alignment=Qt.AlignCenter)
        v_layout_augmented_3_image.addWidget(self.augmented_3_image)
 
        # 4.Augmented
        v_layout_augmented_4_image = QVBoxLayout(self)
        self.augmented_4_image_title = QLabel(self)
        self.augmented_4_image_title.setText(" 4. Augmented Image")
        self.augmented_4_image_title.setFont(QFont("MS Shell Dlg 2",12))    
        self.augmented_4_image=QLabel(self)
        self.augmented_4_image.setStyleSheet("border: 5px solid black;border-radius: 1augmented_0px;background: white;")
        if self.checked_list[3]==1:
            augmented_result_image_path_4 = self.image_augmented(index=3,image_path=self.original_image_path)
            self.augmented_4_image.setPixmap(QPixmap(augmented_result_image_path_4))
        else:
            self.augmented_4_image.setPixmap(QPixmap(self.original_image_path))        
        self.augmented_4_image.setScaledContents(True)

        # add Widget
        v_layout_augmented_4_image.addWidget(self.augmented_4_image_title,alignment=Qt.AlignCenter)
        v_layout_augmented_4_image.addWidget(self.augmented_4_image)

        # 5.Augmented
        v_layout_augmented_5_image = QVBoxLayout(self)
        self.augmented_5_image_title = QLabel(self)
        self.augmented_5_image_title.setText(" 5. Augmented Image")
        self.augmented_5_image_title.setFont(QFont("MS Shell Dlg 2",12))    
        self.augmented_5_image=QLabel(self)
        self.augmented_5_image.setStyleSheet("border: 5px solid black;border-radius: 1augmented_0px;background: white;")
        if self.checked_list[4]==1:
            augmented_result_image_path_5 = self.image_augmented(index=3,image_path=self.original_image_path)
            self.augmented_5_image.setPixmap(QPixmap(augmented_result_image_path_5))
        else:
            self.augmented_5_image.setPixmap(QPixmap(self.original_image_path))        
        self.augmented_5_image.setScaledContents(True)

        # add Widget
        v_layout_augmented_5_image.addWidget(self.augmented_5_image_title,alignment=Qt.AlignCenter)
        v_layout_augmented_5_image.addWidget(self.augmented_5_image)

        # 6.Augmented
        v_layout_augmented_6_image = QVBoxLayout(self)
        self.augmented_6_image_title = QLabel(self)
        self.augmented_6_image_title.setText(" 6. Augmented Image")
        self.augmented_6_image_title.setFont(QFont("MS Shell Dlg 2",12))    
        self.augmented_6_image=QLabel(self)
        self.augmented_6_image.setStyleSheet("border: 5px solid black;border-radius: 1augmented_0px;background: white;")
        if self.checked_list[5]==1:
            augmented_result_image_path_6 = self.image_augmented(index=5,image_path=self.original_image_path)
            self.augmented_6_image.setPixmap(QPixmap(augmented_result_image_path_6))
        else:
            self.augmented_6_image.setPixmap(QPixmap(self.original_image_path))        
        self.augmented_6_image.setScaledContents(True)

        # add Widget
        v_layout_augmented_6_image.addWidget(self.augmented_6_image_title,alignment=Qt.AlignCenter)
        v_layout_augmented_6_image.addWidget(self.augmented_6_image)
 
        # Grid Add Layout
        grid_layout.addLayout(v_layout_augmented_1_image,0,0)
        grid_layout.addLayout(v_layout_augmented_2_image,0,1)
        grid_layout.addLayout(v_layout_augmented_3_image,0,2)
        grid_layout.addLayout(v_layout_augmented_4_image,1,0)
        grid_layout.addLayout(v_layout_augmented_5_image,1,1)
        grid_layout.addLayout(v_layout_augmented_6_image,1,2)

        # add main layout
        v_main_layout.addWidget(self.title,1)
        v_main_layout.addLayout(v_original_data_layout,1)
        v_main_layout.addLayout(grid_layout,3)
        self.setLayout(v_main_layout)

    def image_augmented(self,index:int,image_path:str):
        control=0
        augmented_result_image_path = "./augmenteds/{0}.augmented_image.png".format(index+1)
        augmented_result_image = None

        # Position
        if self.position_list[index]==1:
            if control==0:
                augmented_result_image = horizantally_flipped(image_path,1)
                control=1
            else:
                augmented_result_image = horizantally_flipped(augmented_result_image_path,1)
        
        elif self.position_list[index]==2:
            if control==0:
                augmented_result_image = vertically_flipped(image_path,1)
                control=1
            else:
                augmented_result_image = vertically_flipped(augmented_result_image_path,1)
                
        # Rotate
        if self.rotate_list[index]!=0.0:
            if control==0:
                augmented_result_image = rotate_image(image_path,self.rotate_list[index],1)
                control=1
            else:
                augmented_result_image = rotate_image(augmented_result_image_path,self.rotate_list[index],1)
        
        # Blur
        if self.blur_list[index]!=0:
            if control==0:
                augmented_result_image = blur_image(image_path,self.blur_list[index],1)
                control=1
            else:
                augmented_result_image = blur_image(augmented_result_image_path,self.blur_list[index],1)
        
        # Central Crop
        if self.central_crop_list[index]!=0:
            if control==0:
                augmented_result_image = central_crop(image_path,self.central_crop_list[index],1)
                control=1
            else:
                augmented_result_image = central_crop(augmented_result_image_path,self.central_crop_list[index],1)
        
        # Resize
        if self.resize_list[index][0]!=0 or self.resize_list[index][1]!=0:
            if control==0:
                augmented_result_image = image_resize(image_path,self.resize_list[index][0],self.resize_list[index][1],1)
                control=1
            else:
                augmented_result_image = image_resize(augmented_result_image_path,self.resize_list[index][0],self.resize_list[index][1],1)
        
        # Adjust Brightness
        if self.adjust_brightness_list[index]!=0.0:
            if control==0:
                augmented_result_image = adjust_brightness(image_path,self.adjust_brightness_list[index],1)
                control=1
            else:
                augmented_result_image = adjust_brightness(augmented_result_image_path,self.adjust_brightness_list[index],1)
        
        # Noise
        if self.noise_list[index]!=0:
            if control==0:
                augmented_result_image = image_adding_noise(image_path,1)
                control=1
            else:
                augmented_result_image = image_adding_noise(augmented_result_image_path,1)
        
        # RGB to GRAY
        if self.rgb_to_gray_list[index]!=0:
            if control==0:
                augmented_result_image = rgb_to_gray(image_path,1)
                control=1
            else:
                augmented_result_image = rgb_to_gray(augmented_result_image_path,1)
       
        # RGB to BGR
        if self.rgb_to_bgr_list[index]!=0:
            if control==0:
                augmented_result_image = rgb_to_bgr(image_path,1)
                control=1
            else:
                augmented_result_image = rgb_to_bgr(augmented_result_image_path,1)
        
        # BGR to GRAY
        if self.bgr_to_gray_list[index]!=0:
            if control==0:
                augmented_result_image = bgr_to_gray(image_path,1)
                control=1
            else:
                augmented_result_image = bgr_to_gray(augmented_result_image_path,1)

        # GRAY to RGB
        if self.gray_to_rgb_list[index]!=0:
            if control==0:
                augmented_result_image = gray_to_rgb(image_path,1)
                control=1
            else:
                augmented_result_image = gray_to_rgb(augmented_result_image_path,1)
        
        # Write Image
        if self.position_list[index]!=0 or self.rotate_list[index]!=0.0 or  self.blur_list[index]!=0 or self.central_crop_list[index]!=0 or self.resize_list[index][0]!=0 or self.resize_list[index][1]!=0 or self.adjust_brightness_list[index]!=0.0 or self.noise_list[index]!=0 or self.rgb_to_gray_list[index]!=0 or self.rgb_to_gray_list[index]!=0 or  self.bgr_to_gray_list[index]!=0 or self.rgb_to_gray_list[index]!=0: 
            cv2.imwrite(augmented_result_image_path,augmented_result_image)
        
        else:
            augmented_result_image_path = image_path

        return augmented_result_image_path

# def main():
#     app = QApplication(sys.argv)

#     main = ControlAugmentedWindows()
#     main.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#   main()