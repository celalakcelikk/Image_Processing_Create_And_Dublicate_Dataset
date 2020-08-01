# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import walk
import cv2
import os
from augmented import *
from augmentedTestControlWindows import ControlAugmentedWindows
from dublicateDataWindows import DublicateDataWindows

class AugmentedWindows(QWidget):
    def __init__(self,folderPath,dataClassesFilePath,checkedRadio_Image):
        self.folderPath = folderPath
        self.dataClassesFilePath = dataClassesFilePath
        self.checkedRadio_Image = checkedRadio_Image
        self.checked_list= [0 for i in range(6)]
        self.position_list= [0 for i in range(6)]
        self.rotate_list= [0.0 for i in range(6)]
        self.blur_list= [0 for i in range(6)]
        self.central_crop_list= [0 for i in range(6)]
        self.resize_list= [[0,0] for i in range(6)]
        self.adjust_brightness_list= [0.0 for i in range(6)]
        self.noise_list= [0 for i in range(6)]
        self.rgb_to_gray_list= [0 for i in range(6)]
        self.rgb_to_bgr_list= [0 for i in range(6)]
        self.bgr_to_gray_list= [0 for i in range(6)]
        self.gray_to_rgb_list= [0 for i in range(6)]
        super().__init__()
        self.augmentedWindow()

    def augmentedWindow(self):
        # Page Building
        self.setGeometry(300, 300, 1100, 670)
        self.setMaximumSize(1100,680)
        self.setMinimumSize(1100,670)
        self.setStyleSheet("background: white;")
        self.setWindowTitle("Augmented Assignment")
        self.setWindowIcon(QIcon('images/plus.png'))

        self.title = QLabel(self)
        self.title.setScaledContents(True)
        self.title.setText("Augmented Assignment".upper())
        self.title.setFont(QFont("MS Shell Dlg 2",18,QFont.Bold))
        self.title.setStyleSheet("background-color:#c39435;color:#ffffff;border-radius:10px;border-style: solid;")
        self.title.setAlignment(Qt.AlignCenter)

        # main layout
        v_main_layout = QVBoxLayout(self)

        #1 horizontal
        h_layout_1 = QHBoxLayout(self)
        #1
        self.groupBox1 = QGroupBox("1")
        self.groupBox1.setCheckable(True)
        self.groupBox1.setChecked(False)
        
        v_group_box1_layout = QVBoxLayout(self)
        
        form_1 = QFormLayout(self)
        
        self.select_position_combobox_1 = QComboBox(self)
        self.select_position_combobox_1.addItem("Selecting...")
        self.select_position_combobox_1.addItem("Horizontal")
        self.select_position_combobox_1.addItem("Vertical")
        
        form_1.addRow(QLabel("Position"),self.select_position_combobox_1)

        self.write_rotate_1_LineEdit = QLineEdit(self)
        self.write_rotate_1_LineEdit.setValidator(QDoubleValidator())
        self.write_rotate_1_LineEdit.setPlaceholderText("0.0")   
        form_1.addRow(QLabel("Rotate"),self.write_rotate_1_LineEdit)

        self.write_blur_1_LineEdit = QLineEdit(self)
        self.write_blur_1_LineEdit.setValidator(QIntValidator())   
        self.write_blur_1_LineEdit.setPlaceholderText("0")   
        form_1.addRow(QLabel("Blur"),self.write_blur_1_LineEdit)

        self.write_central_crop_1_LineEdit = QLineEdit(self)
        self.write_central_crop_1_LineEdit.setValidator(QIntValidator())   
        self.write_central_crop_1_LineEdit.setPlaceholderText("0")   
        form_1.addRow(QLabel("Central Crop"),self.write_central_crop_1_LineEdit)
        
        
        self.write_resize_y_1_LineEdit = QLineEdit(self)
        self.write_resize_y_1_LineEdit.setValidator(QIntValidator())   
        self.write_resize_y_1_LineEdit.setPlaceholderText("0")   
        self.write_resize_x_1_LineEdit = QLineEdit(self)
        self.write_resize_x_1_LineEdit.setValidator(QIntValidator())   
        self.write_resize_x_1_LineEdit.setPlaceholderText("0")   
        h_write_resize_1 = QHBoxLayout(self)
        h_write_resize_1.addWidget(self.write_resize_y_1_LineEdit)
        h_write_resize_1.addWidget(self.write_resize_x_1_LineEdit)
        form_1.addRow(QLabel("Resize(y,x)"),h_write_resize_1)
        
        self.write_adjust_brightness_1_LineEdit = QLineEdit(self)
        self.write_adjust_brightness_1_LineEdit.setValidator(QDoubleValidator())   
        self.write_adjust_brightness_1_LineEdit.setPlaceholderText("0.0")   
        form_1.addRow(QLabel("Adjust Brightness"),self.write_adjust_brightness_1_LineEdit)

        self.select_noise_1 = QCheckBox(self)
        form_1.addRow(QLabel("Random Noise"),self.select_noise_1)
        
        self.select_rgb_to_gray_1 = QCheckBox(self)
        form_1.addRow(QLabel("RGB to GRAY"),self.select_rgb_to_gray_1)

        self.select_rgb_to_bgr_1 = QCheckBox(self)
        form_1.addRow(QLabel("RGB to BGR"),self.select_rgb_to_bgr_1)

        self.select_bgr_to_gray_1 = QCheckBox(self)
        form_1.addRow(QLabel("BGR to GRAY"),self.select_bgr_to_gray_1)

        self.select_gray_to_rgb_1 = QCheckBox(self)
        form_1.addRow(QLabel("GRAY to RGB"),self.select_gray_to_rgb_1)

        v_group_box1_layout.addLayout(form_1)
        self.groupBox1.setLayout(v_group_box1_layout)
        #2
        self.groupBox2 = QGroupBox("2")
        self.groupBox2.setCheckable(True)
        self.groupBox2.setChecked(False)
        
        v_group_box2_layout = QVBoxLayout(self)
        
        form_2 = QFormLayout(self)
        
        self.select_position_combobox_2 = QComboBox(self)
        self.select_position_combobox_2.addItem("Selecting...")
        self.select_position_combobox_2.addItem("Horizontal")
        self.select_position_combobox_2.addItem("Vertical")
        
        form_2.addRow(QLabel("Position"),self.select_position_combobox_2)

        self.write_rotate_2_LineEdit = QLineEdit(self)
        self.write_rotate_2_LineEdit.setValidator(QDoubleValidator())
        self.write_rotate_2_LineEdit.setPlaceholderText("0.0")   
        form_2.addRow(QLabel("Rotate"),self.write_rotate_2_LineEdit)

        self.write_blur_2_LineEdit = QLineEdit(self)
        self.write_blur_2_LineEdit.setValidator(QIntValidator())   
        self.write_blur_2_LineEdit.setPlaceholderText("0")   
        form_2.addRow(QLabel("Blur"),self.write_blur_2_LineEdit)

        self.write_central_crop_2_LineEdit = QLineEdit(self)
        self.write_central_crop_2_LineEdit.setValidator(QIntValidator())   
        self.write_central_crop_2_LineEdit.setPlaceholderText("0")   
        form_2.addRow(QLabel("Central Crop"),self.write_central_crop_2_LineEdit)
        
        self.write_resize_y_2_LineEdit = QLineEdit(self)
        self.write_resize_y_2_LineEdit.setValidator(QIntValidator())   
        self.write_resize_y_2_LineEdit.setPlaceholderText("0")   
        self.write_resize_x_2_LineEdit = QLineEdit(self)
        self.write_resize_x_2_LineEdit.setValidator(QIntValidator())   
        self.write_resize_x_2_LineEdit.setPlaceholderText("0")   
        h_write_resize_2 = QHBoxLayout(self)
        h_write_resize_2.addWidget(self.write_resize_y_2_LineEdit)
        h_write_resize_2.addWidget(self.write_resize_x_2_LineEdit)
        form_2.addRow(QLabel("Resize(y,x)"),h_write_resize_2)
        
        self.write_adjust_brightness_2_LineEdit = QLineEdit(self)
        self.write_adjust_brightness_2_LineEdit.setValidator(QDoubleValidator())   
        self.write_adjust_brightness_2_LineEdit.setPlaceholderText("0.0")   
        form_2.addRow(QLabel("Adjust Brightness"),self.write_adjust_brightness_2_LineEdit)

        self.select_noise_2 = QCheckBox(self)
        form_2.addRow(QLabel("Random Noise"),self.select_noise_2)
        
        self.select_rgb_to_gray_2 = QCheckBox(self)
        form_2.addRow(QLabel("RGB to GRAY"),self.select_rgb_to_gray_2)

        self.select_rgb_to_bgr_2 = QCheckBox(self)
        form_2.addRow(QLabel("RGB to BGR"),self.select_rgb_to_bgr_2)

        self.select_bgr_to_gray_2 = QCheckBox(self)
        form_2.addRow(QLabel("BGR to GRAY"),self.select_bgr_to_gray_2)

        self.select_gray_to_rgb_2 = QCheckBox(self)
        form_2.addRow(QLabel("GRAY to RGB"),self.select_gray_to_rgb_2)

        v_group_box2_layout.addLayout(form_2)
        self.groupBox2.setLayout(v_group_box2_layout)

        #3
        self.groupBox3 = QGroupBox("3")
        self.groupBox3.setCheckable(True)
        self.groupBox3.setChecked(False)

        v_group_box3_layout = QVBoxLayout(self)
        
        form_3 = QFormLayout(self)
        
        self.select_position_combobox_3 = QComboBox(self)
        self.select_position_combobox_3.addItem("Selecting...")
        self.select_position_combobox_3.addItem("Horizontal")
        self.select_position_combobox_3.addItem("Vertical")
        
        form_3.addRow(QLabel("Position"),self.select_position_combobox_3)

        self.write_rotate_3_LineEdit = QLineEdit(self)
        self.write_rotate_3_LineEdit.setValidator(QDoubleValidator())
        self.write_rotate_3_LineEdit.setPlaceholderText("0.0")   
        form_3.addRow(QLabel("Rotate"),self.write_rotate_3_LineEdit)

        self.write_blur_3_LineEdit = QLineEdit(self)
        self.write_blur_3_LineEdit.setValidator(QIntValidator())   
        self.write_blur_3_LineEdit.setPlaceholderText("0")   
        form_3.addRow(QLabel("Blur"),self.write_blur_3_LineEdit)

        self.write_central_crop_3_LineEdit = QLineEdit(self)
        self.write_central_crop_3_LineEdit.setValidator(QIntValidator())   
        self.write_central_crop_3_LineEdit.setPlaceholderText("0")   
        form_3.addRow(QLabel("Central Crop"),self.write_central_crop_3_LineEdit)
        
        self.write_resize_y_3_LineEdit = QLineEdit(self)
        self.write_resize_y_3_LineEdit.setValidator(QIntValidator())   
        self.write_resize_y_3_LineEdit.setPlaceholderText("0")   
        self.write_resize_x_3_LineEdit = QLineEdit(self)
        self.write_resize_x_3_LineEdit.setValidator(QIntValidator())   
        self.write_resize_x_3_LineEdit.setPlaceholderText("0")   
        h_write_resize_3 = QHBoxLayout(self)
        h_write_resize_3.addWidget(self.write_resize_y_3_LineEdit)
        h_write_resize_3.addWidget(self.write_resize_x_3_LineEdit)
        form_3.addRow(QLabel("Resize(y,x)"),h_write_resize_3)
        
        self.write_adjust_brightness_3_LineEdit = QLineEdit(self)
        self.write_adjust_brightness_3_LineEdit.setValidator(QDoubleValidator())   
        self.write_adjust_brightness_3_LineEdit.setPlaceholderText("0.0")   
        form_3.addRow(QLabel("Adjust Brightness"),self.write_adjust_brightness_3_LineEdit)

        self.select_noise_3 = QCheckBox(self)
        form_3.addRow(QLabel("Random Noise"),self.select_noise_3)
        
        self.select_rgb_to_gray_3 = QCheckBox(self)
        form_3.addRow(QLabel("RGB to GRAY"),self.select_rgb_to_gray_3)

        self.select_rgb_to_bgr_3 = QCheckBox(self)
        form_3.addRow(QLabel("RGB to BGR"),self.select_rgb_to_bgr_3)

        self.select_bgr_to_gray_3 = QCheckBox(self)
        form_3.addRow(QLabel("BGR to GRAY"),self.select_bgr_to_gray_3)

        self.select_gray_to_rgb_3 = QCheckBox(self)
        form_3.addRow(QLabel("GRAY to RGB"),self.select_gray_to_rgb_3)

        v_group_box3_layout.addLayout(form_3)
        self.groupBox3.setLayout(v_group_box3_layout)

        #2
        h_layout_2 = QHBoxLayout(self)
        #4
        self.groupBox4 = QGroupBox("4")
        self.groupBox4.setCheckable(True)
        self.groupBox4.setChecked(False)
        
        v_group_box4_layout = QVBoxLayout(self)
        
        form_4 = QFormLayout(self)
        
        self.select_position_combobox_4 = QComboBox(self)
        self.select_position_combobox_4.addItem("Selecting...")
        self.select_position_combobox_4.addItem("Horizontal")
        self.select_position_combobox_4.addItem("Vertical")
        
        form_4.addRow(QLabel("Position"),self.select_position_combobox_4)

        self.write_rotate_4_LineEdit = QLineEdit(self)
        self.write_rotate_4_LineEdit.setValidator(QDoubleValidator())
        self.write_rotate_4_LineEdit.setPlaceholderText("0.0")   
        form_4.addRow(QLabel("Rotate"),self.write_rotate_4_LineEdit)

        self.write_blur_4_LineEdit = QLineEdit(self)
        self.write_blur_4_LineEdit.setValidator(QIntValidator())   
        self.write_blur_4_LineEdit.setPlaceholderText("0")   
        form_4.addRow(QLabel("Blur"),self.write_blur_4_LineEdit)

        self.write_central_crop_4_LineEdit = QLineEdit(self)
        self.write_central_crop_4_LineEdit.setValidator(QIntValidator())   
        self.write_central_crop_4_LineEdit.setPlaceholderText("0")   
        form_4.addRow(QLabel("Central Crop"),self.write_central_crop_4_LineEdit)
        
        
        self.write_resize_y_4_LineEdit = QLineEdit(self)
        self.write_resize_y_4_LineEdit.setValidator(QIntValidator())   
        self.write_resize_y_4_LineEdit.setPlaceholderText("0")   
        self.write_resize_x_4_LineEdit = QLineEdit(self)
        self.write_resize_x_4_LineEdit.setValidator(QIntValidator())   
        self.write_resize_x_4_LineEdit.setPlaceholderText("0")   
        h_write_resize_4 = QHBoxLayout(self)
        h_write_resize_4.addWidget(self.write_resize_y_4_LineEdit)
        h_write_resize_4.addWidget(self.write_resize_x_4_LineEdit)
        form_4.addRow(QLabel("Resize(y,x)"),h_write_resize_4)
        
        self.write_adjust_brightness_4_LineEdit = QLineEdit(self)
        self.write_adjust_brightness_4_LineEdit.setValidator(QDoubleValidator())   
        self.write_adjust_brightness_4_LineEdit.setPlaceholderText("0.0")   
        form_4.addRow(QLabel("Adjust Brightness"),self.write_adjust_brightness_4_LineEdit)

        self.select_noise_4 = QCheckBox(self)
        form_4.addRow(QLabel("Random Noise"),self.select_noise_4)
        
        self.select_rgb_to_gray_4 = QCheckBox(self)
        form_4.addRow(QLabel("RGB to GRAY"),self.select_rgb_to_gray_4)

        self.select_rgb_to_bgr_4 = QCheckBox(self)
        form_4.addRow(QLabel("RGB to BGR"),self.select_rgb_to_bgr_4)

        self.select_bgr_to_gray_4 = QCheckBox(self)
        form_4.addRow(QLabel("BGR to GRAY"),self.select_bgr_to_gray_4)

        self.select_gray_to_rgb_4 = QCheckBox(self)
        form_4.addRow(QLabel("GRAY to RGB"),self.select_gray_to_rgb_4)

        v_group_box4_layout.addLayout(form_4)
        self.groupBox4.setLayout(v_group_box4_layout)
        #5
        self.groupBox5 = QGroupBox("5")
        self.groupBox5.setCheckable(True)
        self.groupBox5.setChecked(False)
        
        v_group_box5_layout = QVBoxLayout(self)
        
        form_5 = QFormLayout(self)
        
        self.select_position_combobox_5 = QComboBox(self)
        self.select_position_combobox_5.addItem("Selecting...")
        self.select_position_combobox_5.addItem("Horizontal")
        self.select_position_combobox_5.addItem("Vertical")
        
        form_5.addRow(QLabel("Position"),self.select_position_combobox_5)

        self.write_rotate_5_LineEdit = QLineEdit(self)
        self.write_rotate_5_LineEdit.setValidator(QDoubleValidator())
        self.write_rotate_5_LineEdit.setPlaceholderText("0.0")   
        form_5.addRow(QLabel("Rotate"),self.write_rotate_5_LineEdit)

        self.write_blur_5_LineEdit = QLineEdit(self)
        self.write_blur_5_LineEdit.setValidator(QIntValidator())   
        self.write_blur_5_LineEdit.setPlaceholderText("0")   
        form_5.addRow(QLabel("Blur"),self.write_blur_5_LineEdit)

        self.write_central_crop_5_LineEdit = QLineEdit(self)
        self.write_central_crop_5_LineEdit.setValidator(QIntValidator())   
        self.write_central_crop_5_LineEdit.setPlaceholderText("0")   
        form_5.addRow(QLabel("Central Crop"),self.write_central_crop_5_LineEdit)
        
        self.write_resize_y_5_LineEdit = QLineEdit(self)
        self.write_resize_y_5_LineEdit.setValidator(QIntValidator())   
        self.write_resize_y_5_LineEdit.setPlaceholderText("0")   
        self.write_resize_x_5_LineEdit = QLineEdit(self)
        self.write_resize_x_5_LineEdit.setValidator(QIntValidator())   
        self.write_resize_x_5_LineEdit.setPlaceholderText("0")   
        h_write_resize_5 = QHBoxLayout(self)
        h_write_resize_5.addWidget(self.write_resize_y_5_LineEdit)
        h_write_resize_5.addWidget(self.write_resize_x_5_LineEdit)
        form_5.addRow(QLabel("Resize(y,x)"),h_write_resize_5)
        
        self.write_adjust_brightness_5_LineEdit = QLineEdit(self)
        self.write_adjust_brightness_5_LineEdit.setValidator(QDoubleValidator())   
        self.write_adjust_brightness_5_LineEdit.setPlaceholderText("0.0")   
        form_5.addRow(QLabel("Adjust Brightness"),self.write_adjust_brightness_5_LineEdit)

        self.select_noise_5 = QCheckBox(self)
        form_5.addRow(QLabel("Random Noise"),self.select_noise_5)
        
        self.select_rgb_to_gray_5 = QCheckBox(self)
        form_5.addRow(QLabel("RGB to GRAY"),self.select_rgb_to_gray_5)

        self.select_rgb_to_bgr_5 = QCheckBox(self)
        form_5.addRow(QLabel("RGB to BGR"),self.select_rgb_to_bgr_5)

        self.select_bgr_to_gray_5 = QCheckBox(self)
        form_5.addRow(QLabel("BGR to GRAY"),self.select_bgr_to_gray_5)

        self.select_gray_to_rgb_5 = QCheckBox(self)
        form_5.addRow(QLabel("GRAY to RGB"),self.select_gray_to_rgb_5)

        v_group_box5_layout.addLayout(form_5)
        self.groupBox5.setLayout(v_group_box5_layout)

        #6
        self.groupBox6 = QGroupBox("6")
        self.groupBox6.setCheckable(True)
        self.groupBox6.setChecked(False)

        v_group_box6_layout = QVBoxLayout(self)
        
        form_6 = QFormLayout(self)
        
        self.select_position_combobox_6 = QComboBox(self)
        self.select_position_combobox_6.addItem("Selecting...")
        self.select_position_combobox_6.addItem("Horizontal")
        self.select_position_combobox_6.addItem("Vertical")
        
        form_6.addRow(QLabel("Position"),self.select_position_combobox_6)

        self.write_rotate_6_LineEdit = QLineEdit(self)
        self.write_rotate_6_LineEdit.setValidator(QDoubleValidator())
        self.write_rotate_6_LineEdit.setPlaceholderText("0.0")   
        form_6.addRow(QLabel("Rotate"),self.write_rotate_6_LineEdit)

        self.write_blur_6_LineEdit = QLineEdit(self)
        self.write_blur_6_LineEdit.setValidator(QIntValidator())   
        self.write_blur_6_LineEdit.setPlaceholderText("0")   
        form_6.addRow(QLabel("Blur"),self.write_blur_6_LineEdit)

        self.write_central_crop_6_LineEdit = QLineEdit(self)
        self.write_central_crop_6_LineEdit.setValidator(QIntValidator())   
        self.write_central_crop_6_LineEdit.setPlaceholderText("0")   
        form_6.addRow(QLabel("Central Crop"),self.write_central_crop_6_LineEdit)
        
        self.write_resize_y_6_LineEdit = QLineEdit(self)
        self.write_resize_y_6_LineEdit.setValidator(QIntValidator())   
        self.write_resize_y_6_LineEdit.setPlaceholderText("0")   
        self.write_resize_x_6_LineEdit = QLineEdit(self)
        self.write_resize_x_6_LineEdit.setValidator(QIntValidator())   
        self.write_resize_x_6_LineEdit.setPlaceholderText("0")   
        h_write_resize_6 = QHBoxLayout(self)
        h_write_resize_6.addWidget(self.write_resize_y_6_LineEdit)
        h_write_resize_6.addWidget(self.write_resize_x_6_LineEdit)
        form_6.addRow(QLabel("Resize(y,x)"),h_write_resize_6)
        
        self.write_adjust_brightness_6_LineEdit = QLineEdit(self)
        self.write_adjust_brightness_6_LineEdit.setValidator(QDoubleValidator())   
        self.write_adjust_brightness_6_LineEdit.setPlaceholderText("0.0")   
        form_6.addRow(QLabel("Adjust Brightness"),self.write_adjust_brightness_6_LineEdit)

        self.select_noise_6 = QCheckBox(self)
        form_6.addRow(QLabel("Random Noise"),self.select_noise_6)
        
        self.select_rgb_to_gray_6 = QCheckBox(self)
        form_6.addRow(QLabel("RGB to GRAY"),self.select_rgb_to_gray_6)

        self.select_rgb_to_bgr_6 = QCheckBox(self)
        form_6.addRow(QLabel("RGB to BGR"),self.select_rgb_to_bgr_6)

        self.select_bgr_to_gray_6 = QCheckBox(self)
        form_6.addRow(QLabel("BGR to GRAY"),self.select_bgr_to_gray_6)

        self.select_gray_to_rgb_6 = QCheckBox(self)
        form_6.addRow(QLabel("GRAY to RGB"),self.select_gray_to_rgb_6)

        v_group_box6_layout.addLayout(form_6)
        self.groupBox6.setLayout(v_group_box6_layout)


        # Test Control Button
        h_test_and_create_button_layout = QHBoxLayout(self)
        # Back Windows Button
        self.test_image_button = QPushButton(self)
        self.test_image_button.setText(" Augmented Image Control ")
        self.test_image_button.setFont(QFont("MS Shell Dlg 2",15,QFont.Bold))
        self.test_image_button.setStyleSheet("background:#0B8BF5; color:#ffffff; border-radius:10px; border-style: 15px solid;")
        self.test_image_button.setIcon(QIcon('images/control_2.png'))
        self.test_image_button.setIconSize(QSize(20,20))
        self.test_image_button.clicked.connect(self.openTestAugmentedWindows)

        #SizePolicy
        sizePolicy = QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_image_button.sizePolicy().hasHeightForWidth())
        self.test_image_button.setSizePolicy(sizePolicy) 

        # Next Windows Button
        self.start_augmented_data_button = QPushButton(self)
        self.start_augmented_data_button.setText(" Augmented Image ")
        self.start_augmented_data_button.setFont(QFont("MS Shell Dlg 2",15,QFont.Bold))
        self.start_augmented_data_button.setStyleSheet("background:#E6C54C; color:#ffffff; border-radius:10px; border-style: 15px solid;")
        self.start_augmented_data_button.setIcon(QIcon('images/spaceship.png'))
        self.start_augmented_data_button.setIconSize(QSize(20,20))
        self.start_augmented_data_button.setLayoutDirection(Qt.RightToLeft)
        self.start_augmented_data_button.clicked.connect(self.openAugmentedWindows)
        #SizePolicy
        sizePolicy = QSizePolicy(QSizePolicy.Minimum,QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_augmented_data_button.sizePolicy().hasHeightForWidth())
        self.start_augmented_data_button.setSizePolicy(sizePolicy) 

        h_test_and_create_button_layout.addWidget(self.test_image_button)
        h_test_and_create_button_layout.addWidget(self.start_augmented_data_button)
        # add widget
        h_layout_1.addWidget(self.groupBox1,1)
        h_layout_1.addWidget(self.groupBox2,1)
        h_layout_1.addWidget(self.groupBox3,1)
        h_layout_2.addWidget(self.groupBox4,1)
        h_layout_2.addWidget(self.groupBox5,1)
        h_layout_2.addWidget(self.groupBox6,1)

        # add main layout
        v_main_layout.addWidget(self.title,2)
        v_main_layout.addLayout(h_layout_1,8)
        v_main_layout.addLayout(h_layout_2,8)
        v_main_layout.addLayout(h_test_and_create_button_layout,2)
        self.setLayout(v_main_layout)

    def control_augmented(self):
        if self.groupBox1.isChecked()==True:
            self.checked_list[0]=1
            self.change_lists(0,
                                self.select_position_combobox_1.currentText(),
                                self.write_rotate_1_LineEdit.text(),
                                self.write_blur_1_LineEdit.text(),
                                self.write_central_crop_1_LineEdit.text(),
                                self.write_resize_y_1_LineEdit.text(),
                                self.write_resize_x_1_LineEdit.text(),
                                self.write_adjust_brightness_1_LineEdit.text(),
                                self.select_noise_1.isChecked(),
                                self.select_rgb_to_gray_1.isChecked(),
                                self.select_rgb_to_bgr_1.isChecked(),
                                self.select_bgr_to_gray_1.isChecked(),
                                self.select_gray_to_rgb_1.isChecked())

        elif self.groupBox1.isChecked()==False:
            self.checked_list[0]=0
            self.remove_lists_value(0)

        if self.groupBox2.isChecked()==True:
            self.checked_list[1]=1
            self.change_lists(1,
                                self.select_position_combobox_2.currentText(),
                                self.write_rotate_2_LineEdit.text(),
                                self.write_blur_2_LineEdit.text(),
                                self.write_central_crop_2_LineEdit.text(),
                                self.write_resize_y_2_LineEdit.text(),
                                self.write_resize_x_2_LineEdit.text(),
                                self.write_adjust_brightness_2_LineEdit.text(),
                                self.select_noise_2.isChecked(),
                                self.select_rgb_to_gray_2.isChecked(),
                                self.select_rgb_to_bgr_2.isChecked(),
                                self.select_bgr_to_gray_2.isChecked(),
                                self.select_gray_to_rgb_2.isChecked())

        elif self.groupBox2.isChecked()==False:
            self.checked_list[1]=0
            self.remove_lists_value(1)

        if self.groupBox3.isChecked()==True:
            self.checked_list[2]=1
            self.change_lists(2,
                                self.select_position_combobox_3.currentText(),
                                self.write_rotate_3_LineEdit.text(),
                                self.write_blur_3_LineEdit.text(),
                                self.write_central_crop_3_LineEdit.text(),
                                self.write_resize_y_3_LineEdit.text(),
                                self.write_resize_x_3_LineEdit.text(),
                                self.write_adjust_brightness_3_LineEdit.text(),
                                self.select_noise_3.isChecked(),
                                self.select_rgb_to_gray_3.isChecked(),
                                self.select_rgb_to_bgr_3.isChecked(),
                                self.select_bgr_to_gray_3.isChecked(),
                                self.select_gray_to_rgb_3.isChecked())

        elif self.groupBox3.isChecked()==False:
            self.checked_list[2]=0
            self.remove_lists_value(2)

        if self.groupBox4.isChecked()==True:
            self.checked_list[3]=1
            self.change_lists(3,
                                self.select_position_combobox_4.currentText(),
                                self.write_rotate_4_LineEdit.text(),
                                self.write_blur_4_LineEdit.text(),
                                self.write_central_crop_4_LineEdit.text(),
                                self.write_resize_y_4_LineEdit.text(),
                                self.write_resize_x_4_LineEdit.text(),
                                self.write_adjust_brightness_4_LineEdit.text(),
                                self.select_noise_4.isChecked(),
                                self.select_rgb_to_gray_4.isChecked(),
                                self.select_rgb_to_bgr_4.isChecked(),
                                self.select_bgr_to_gray_4.isChecked(),
                                self.select_gray_to_rgb_4.isChecked())

        elif self.groupBox4.isChecked()==False:
            self.checked_list[3]=0
            self.remove_lists_value(3)

        if self.groupBox5.isChecked()==True:
            self.checked_list[4]=1
            self.change_lists(4,
                                self.select_position_combobox_5.currentText(),
                                self.write_rotate_4_LineEdit.text(),
                                self.write_blur_5_LineEdit.text(),
                                self.write_central_crop_5_LineEdit.text(),
                                self.write_resize_y_5_LineEdit.text(),
                                self.write_resize_x_5_LineEdit.text(),
                                self.write_adjust_brightness_5_LineEdit.text(),
                                self.select_noise_5.isChecked(),
                                self.select_rgb_to_gray_5.isChecked(),
                                self.select_rgb_to_bgr_5.isChecked(),
                                self.select_bgr_to_gray_5.isChecked(),
                                self.select_gray_to_rgb_5.isChecked())

        elif self.groupBox5.isChecked()==False:
            self.checked_list[5]=0
            self.remove_lists_value(4)

        if self.groupBox6.isChecked()==True:
            self.checked_list[5]=1
            self.change_lists(5,
                                self.select_position_combobox_6.currentText(),
                                self.write_rotate_4_LineEdit.text(),
                                self.write_blur_6_LineEdit.text(),
                                self.write_central_crop_6_LineEdit.text(),
                                self.write_resize_y_6_LineEdit.text(),
                                self.write_resize_x_6_LineEdit.text(),
                                self.write_adjust_brightness_6_LineEdit.text(),
                                self.select_noise_6.isChecked(),
                                self.select_rgb_to_gray_6.isChecked(),
                                self.select_rgb_to_bgr_6.isChecked(),
                                self.select_bgr_to_gray_6.isChecked(),
                                self.select_gray_to_rgb_6.isChecked())

        elif self.groupBox6.isChecked()==False:
            self.checked_list[5]=0
            self.remove_lists_value(5)
        
        # print("--------------------------------------------")
        # print("position : ",self.position_list)
        # print("--------------------------------------------")
        # print("rotate : ",self.rotate_list)
        # print("--------------------------------------------")
        # print("blur : ",self.blur_list)
        # print("--------------------------------------------")
        # print("central crop : ",self.central_crop_list)
        # print("--------------------------------------------")
        # print("resize : ",self.resize_list)
        # print("--------------------------------------------")
        # print("adjust : ",self.adjust_brightness_list)
        # print("--------------------------------------------")
        # print("noise : ",self.noise_list)
        # print("--------------------------------------------")
        # print("rgb to gray : ",self.rgb_to_gray_list)
        # print("--------------------------------------------")
        # print("rgb to bgr : ",self.rgb_to_bgr_list)
        # print("--------------------------------------------")
        # print("bgr to gray : ",self.bgr_to_gray_list)
        # print("--------------------------------------------")
        # print("gray to rgb : ",self.gray_to_rgb_list)
        # print("--------------------------------------------")

    def remove_lists_value(self,index:int):
        self.position_list[index]=0
        self.rotate_list[index]=0
        self.blur_list[index]=0
        self.central_crop_list[index]=0
        self.resize_list[index]=[0,0]
        self.adjust_brightness_list[index] = 0
        self.rgb_to_gray_list[index]=0
        self.rgb_to_bgr_list[index]=0
        self.bgr_to_gray_list[index]=0
        self.gray_to_rgb_list[index]=0

    def change_lists(self,index:int,combobox_value:str,rotate_value:str,blur_value:str,central_crop_value:str,resize_y:str,resize_x:str,adjust_value:str,
                        noise_value:bool,rgb_to_gray:bool,rgb_to_bgr:bool,bgr_to_gray:bool,gray_to_rgb:bool):
        
        # position
        if combobox_value == "Horizontal":
            self.position_list[index] = 1
        elif combobox_value == "Vertical":
            self.position_list[index] = 2
        else:
            self.position_list[index] = 0
        
        # rotate
        try:
            if rotate_value != "":
                rotate_value = float(rotate_value.replace(",","."))
                if rotate_value != 0.0:
                    self.rotate_list[index] = rotate_value
                else:
                    self.rotate_list[index] = 0.0
            else:
                self.rotate_list[index] = 0.0
        except Exception as e:
            print(e)

        # blur
        try:
            if blur_value != "":
                blur_value = float(blur_value.replace(",","."))
                if blur_value != 0.0:
                    self.blur_list[index] = blur_value
                else:
                    self.blur_list[index] = 0.0
            else:
                self.blur_list[index] = 0.0
        except Exception as e:
            print(e)

        # Central Crop
        try:
            if central_crop_value != "":
                central_crop_value = int(central_crop_value)
                if central_crop_value != 0:
                    self.central_crop_list[index] = central_crop_value
                else:
                    self.central_crop_list[index] = 0
            else:
                self.central_crop_list[index] = 0
        except Exception as e:
            print(e)
        
        # Resize(y,x)
        try:
            if resize_y =="":
                resize_y=0
            if resize_x =="":
                resize_x=0

            resize_y = int(resize_y)
            resize_x= int(resize_x)
            if resize_y !=0 or resize_x!=0:
                self.resize_list[index] = [resize_y,resize_x]
            else:
                self.resize_list[index] = [0,0]
        except Exception as e:
            print(e)

        # Adjust Brightness
        try:
            if adjust_value != "":
                adjust_value = float(adjust_value)
                if adjust_value != 0.0:
                    self.adjust_brightness_list[index] = adjust_value
                else:
                    self.adjust_brightness_list[index] = 0.0
            else:
                self.adjust_brightness_list[index] = 0.0
        except Exception as e:
            print(e)

        # Random Noise
        if noise_value == True:
            self.noise_list[index]=1
        else:
            self.noise_list[index]=0

        # RGB to GRAY
        if rgb_to_gray == True:
            self.rgb_to_gray_list[index]=1
        else:
            self.rgb_to_gray_list[index]=0

        # RGB to BGR
        if rgb_to_bgr == True:
            self.rgb_to_bgr_list[index]=1
        else:
            self.rgb_to_bgr_list[index]=0

        # BGR to GRAY
        if bgr_to_gray == True:
            self.bgr_to_gray_list[index]=1
        else:
            self.bgr_to_gray_list[index]=0

        # GRAY to RGB
        if gray_to_rgb == True:
            self.gray_to_rgb_list[index]=1
        else:
            self.gray_to_rgb_list[index]=0

    def openTestAugmentedWindows(self):
        self.control_augmented()
        if 1 in self.checked_list:
            self.augmentedTestWindows = ControlAugmentedWindows(checked_list=self.checked_list,position_list=self.position_list,rotate_list=self.rotate_list,blur_list=self.blur_list,
                                                        central_crop_list=self.central_crop_list,resize_list=self.resize_list,adjust_brightness_list=self.adjust_brightness_list,
                                                        noise_list=self.noise_list,rgb_to_gray_list=self.rgb_to_gray_list,rgb_to_bgr_list=self.rgb_to_bgr_list,bgr_to_gray_list=self.bgr_to_gray_list,
                                                        gray_to_rgb_list=self.gray_to_rgb_list)
            self.augmentedTestWindows.show()
        else:
            self.control_message()
    def openAugmentedWindows(self):
        print(self.checked_list)
        self.control_augmented()
        if 1 in self.checked_list:
            self.hide()
            self.augmentedWindows = DublicateDataWindows(folderPath=self.folderPath,dataClassesFilePath=self.dataClassesFilePath,checkedRadio_Image=self.checkedRadio_Image,checked_list=self.checked_list,position_list=self.position_list,rotate_list=self.rotate_list,blur_list=self.blur_list,
                                                        central_crop_list=self.central_crop_list,resize_list=self.resize_list,adjust_brightness_list=self.adjust_brightness_list,
                                                        noise_list=self.noise_list,rgb_to_gray_list=self.rgb_to_gray_list,rgb_to_bgr_list=self.rgb_to_bgr_list,bgr_to_gray_list=self.bgr_to_gray_list,
                                                        gray_to_rgb_list=self.gray_to_rgb_list)
            self.augmentedWindows.show()
        else:
            self.control_message()

    def control_message(self):
        self.message = QMessageBox(self)
        self.message.setWindowTitle("Dublicate Data")
        self.message.setText("You must select at least one checkbox!!!")
        self.message.setWindowIcon(QIcon('images/error.png'))
        self.message.show()
# def main():
#     app = QApplication(sys.argv)

#     main = AugmentedWindows()
#     main.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#   main()