# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import walk
import cv2
import os

class CreateDataSetWindows(QWidget):
  def __init__(self,folderPath:list,dataClassesFilePath:list,dataSupportFolderPath:list,dataEpochsNumber:int,checkedRadio:int,checkedRadio_Image=0):

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

    self.image = []
    self.step=0
    self.folder_list=[]

    for line in open(dataClassesFilePath,"r",encoding="utf-8"):
      self.folder_list.append(line.replace("\n",""))

    # print("folder name list:",self.folder_list)

    self.timer = QTimer()
    self.timer.timeout.connect(self.kamerayi_ac)
    self.zaman_kontrol()

    super().__init__()
    self.createDataSetWindows()

  def createDataSetWindows(self):
    # Page Building
    self.setGeometry(300, 300, 1100, 650)
    self.setMaximumSize(1100,650)
    self.setMinimumSize(1100,650)
    self.setStyleSheet("background: white;")
    self.setWindowTitle("Image Prosessing Create Dataset ")
    self.setWindowIcon(QIcon('images/plus.png'))

    v_main_layout = QVBoxLayout(self)

    # ProgressBar Ui

    # Support Data Folder Item File Name List
    # self.supportDataFolderItemFileNameList()

    
    v_progressbar_layout = QVBoxLayout(self)
    self.general_progress_bar = QProgressBar(self)
    self.general_progress_bar.setGeometry(25, 25, 300, 40)
    self.general_progress_bar.setMaximum(len(self.folder_list))
    self.general_progress_bar.setValue(0)
    self.general_progress_bar.setFormat('{0} % ({1}/{2})'.format(int((100*0)/len(self.folder_list)),0,len(self.folder_list)))
    self.general_progress_bar.setAlignment(Qt.AlignCenter)

    self.general_progress_bar_title = QLabel(self)
    self.general_progress_bar_title.setText(" General Class ProgressBar ")
    self.general_progress_bar_title.setFont(QFont("MS Shell Dlg 2",12))

    self.epochs_progress_bar = QProgressBar(self)
    self.epochs_progress_bar.setGeometry(25, 25, 300, 40)
    self.epochs_progress_bar.setMaximum(self.dataEpochsNumber)
    self.epochs_progress_bar.setValue(0)
    self.epochs_progress_bar.setFormat('{0} % ({1}/{2})'.format(int((100*0)/self.dataEpochsNumber),0,self.dataEpochsNumber))
    self.epochs_progress_bar.setAlignment(Qt.AlignCenter)

    self.epochs_progress_bar_title = QLabel(self)
    self.epochs_progress_bar_title.setText(" Epochs Numbers ProgressBar ")
    self.epochs_progress_bar_title.setFont(QFont("MS Shell Dlg 2",12))
    

    # İşlemlerin Yapılacağı Yer
    h_layout = QHBoxLayout(self)
    #Kamera
    v_camera_layout = QVBoxLayout(self)
    self.camera_title = QLabel(self)
    self.camera_title.setText(" Camera ")
    self.camera_title.setFont(QFont("MS Shell Dlg 2",12))
    self.camera=QLabel(self)
    self.camera.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
    self.camera.setScaledContents(True)



    # Resmin gözükeceği yer
    v_support_data_layout = QVBoxLayout(self)
    
    self.support_image_title = QLabel(self)
    self.support_image_title.setText(" Support Image ")
    self.support_image_title.setFont(QFont("MS Shell Dlg 2",12))    
    self.support_image=QLabel(self)
    self.support_image.setStyleSheet("border: 5px solid black;border-radius: 10px;background: white;")
    image_url = self.supportDataFolderItemFileNameList()
    self.support_image.setPixmap(QPixmap(image_url))
    self.support_image.setScaledContents(True)

    # Start Button
    self.start_save_image_button = QPushButton(self)
    self.start_save_image_button.setText("Start New Create Dataset")
    self.start_save_image_button.setFont(QFont("MS Shell Dlg 2",25,QFont.Bold))
    self.start_save_image_button.setStyleSheet("background:#000FFA; color:#ffffff; border-radius:10px; border-style: 15px solid;")
    self.start_save_image_button.clicked.connect(self.start_save_image)

    # Size Policy
    sizePolicy = QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.start_save_image_button.sizePolicy().hasHeightForWidth())
    self.start_save_image_button.setSizePolicy(sizePolicy)

    # Add Layot    
    v_progressbar_layout.addWidget(self.general_progress_bar_title,1,alignment=Qt.AlignCenter)
    v_progressbar_layout.addWidget(self.general_progress_bar,4)
    v_progressbar_layout.addWidget(self.epochs_progress_bar_title,1,alignment=Qt.AlignCenter)
    v_progressbar_layout.addWidget(self.epochs_progress_bar,4)
    v_progressbar_layout.addWidget(self.start_save_image_button,1)
    v_camera_layout.addWidget(self.camera_title,2,alignment=Qt.AlignCenter)
    v_camera_layout.addWidget(self.camera,4,alignment=Qt.AlignCenter)
    
    v_support_data_layout.addWidget(self.support_image_title,0,alignment=Qt.AlignCenter)
    v_support_data_layout.addWidget(self.support_image,4,alignment=Qt.AlignCenter)
    
    h_layout.addLayout(v_camera_layout)
    h_layout.addLayout(v_support_data_layout)

    # Add Main Layout
    v_main_layout.addLayout(v_progressbar_layout,1)
    v_main_layout.addLayout(h_layout,3)
    self.setLayout(v_main_layout)

  def supportDataFolderItemFileNameList(self):
    file_list=[]

    for (dirpath, dirnames, filenames) in walk(self.dataSupportFolderPath+"\\"+self.folder_list[self.step]):
      file_list.extend(filenames)
    try:
      image_url = self.dataSupportFolderPath+"\\"+self.folder_list[self.step]+"\\"+file_list[0]
    except:
      image_url = "images/error.png"
    # print("support data classes image url: ",image_url)
    return image_url

  def kamerayi_ac(self):
        ret, image = self.cap.read()
        x=100
        w=100
        y=500
        h=400
        cv2.rectangle(img=image,pt1=(x,w),pt2=(y,h),color=(0,255,0),thickness=4)

        self.image = image[x+10:h-10,w+10:y-10]

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channel = image.shape
        step = channel * width
        qImg = QImage(image.data, width, height, step, QImage.Format_RGB888)
        self.camera.setPixmap(QPixmap.fromImage(qImg))   
    
  def zaman_kontrol(self):
      if not self.timer.isActive():
          self.cap = cv2.VideoCapture(0)
          self.timer.start(20)
      else:
          self.timer.stop()
          self.cap.release()

  def file_control(self,fileName:str):
    directory = self.folderPath+"\\"+fileName
    if os.path.isdir(directory):
          return True
    else:
          os.makedirs(directory)
          return True

  def image_save(self,fileName:str):
    result_bool = self.file_control(fileName=fileName)
    if result_bool:
      directory = str(self.folderPath+"/"+fileName)
      
      data_folder_list=[]
      data_folder_list_len=0
      for (dirpath, dirnames, filenames) in walk(self.folderPath+"\\"+self.folder_list[self.step]):
          data_folder_list.extend(filenames)
      try:
        if data_folder_list!=[]:
          for item in data_folder_list:
                if item.endswith(".png"):
                      f=[int(item.replace(".png","")) for item in data_folder_list]
                elif item.endswith(".jpeg"):
                      f=[int(item.replace(".jpeg","")) for item in data_folder_list]
                elif item.endswith(".jpg"):
                  f=[int(item.replace(".jpg","")) for item in data_folder_list]
                      
          data_folder_list_len=len(f)
        else:
          data_folder_list_len=0
      except:
        data_folder_list_len=0
      print("folder item length: ",data_folder_list_len)
      # print("save image path: ",directory)
      for i in range(data_folder_list_len,(self.dataEpochsNumber+data_folder_list_len)):
        cv2.imwrite("{1}/{0}{2}".format(i,directory,self.image_endwith), self.image)
        self.epochs_progress_bar.setFormat('{0} % ({1}/{2})'.format(int((100*(i+1-data_folder_list_len))/self.dataEpochsNumber),(i+1-data_folder_list_len),self.dataEpochsNumber))
        self.epochs_progress_bar.setValue(i+1-data_folder_list_len)
      self.epochs_progress_bar.setFormat('{0} % ({1}/{2})'.format(int((100*0)/self.dataEpochsNumber),0,self.dataEpochsNumber))
      self.epochs_progress_bar.setValue(0)

  def start_save_image(self):

    print("{0} -----> {1}".format(self.step,self.folder_list[self.step]))
    self.image_save(fileName=self.folder_list[self.step])
    self.general_progress_bar.setFormat('{0} % ({1}/{2})'.format(int((100*(self.step+1))/len(self.folder_list)),self.step+1,len(self.folder_list)))
    self.general_progress_bar.setValue(self.step+1)
    self.count_step()

    if self.step < len(self.folder_list):
      image_url = self.supportDataFolderItemFileNameList()
      self.support_image.setPixmap(QPixmap(image_url))
    else:
      self.start_save_image_button.setEnabled(False)
      self.start_save_image_button.setStyleSheet("background:#E8F1F0; color:#ffffff; border-radius:10px; border-style: 15px solid;")

    if self.step == len(self.folder_list):
      self.general_progress_bar.setFormat('{0} % ({1}/{2})'.format(100,self.step,len(self.folder_list)))
      self.general_progress_bar.setValue(self.step+1)
          
  def count_step(self):
    if self.step < len(self.folder_list):
      self.step+=1

# def main():
#     app = QApplication(sys.argv)

#     main = CreateDataSetWindows(folderPath="D:\Projects\PythonProjects\ip_create_data\data\sign__language_data",
#                                 dataClassesFilePath="D:\Projects\PythonProjects\ip_create_data\create_data_classes_name.txt",
#                                 dataSupportFolderPath="D:\Projects\PythonProjects\sign_language_recognition\other_projects\Sign-Language-Recognition-master\Sign-Language-Recognition-master\Sign-Language-Recognition\data\images\\test",
#                                 dataEpochsNumber=120,
#                                 checkedRadio=1,
#                                 checkedRadio_Image=1)
#     main.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#   main()