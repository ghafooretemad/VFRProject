import cv2
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QImage
from picamera import PiCamera
from picamera.array import PiRGBArray
from PyQt5 import QtCore,  QtWidgets
import time

from CreateButton import *
class StartCamera(QWidget):
    def __init__(self,  selectedMode,  empID,  parent = None):
        super(StartCamera,  self).__init__(parent)
        self.parent = parent
        self.selectedMode = selectedMode
        self.empID = empID
        self.counter = 0
        self.camera = PiCamera()
        self.title = "Starting Camera"
        self.layout = QVBoxLayout()
        self.width = 300
        self.height = 300
        self.top = 20
        self.left = 30
        self.face_cascade = cv2.CascadeClassifier('../../../opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
        self.setWindowTitle("Capture Face")
        self.setupUi()
        self.setLayout(self.layout)
    def setupUi(self):
        self.video_frame = QLabel()
        self.layout.addWidget(self.video_frame)
        self.setGeometry(self.top,  self.left,  self.width,  self.height)
        self.buttons = CreateButton()
        self.path = "../../Icons/face.png"      
      
        if(self.selectedMode.get("normal",  False) == True):
           self.normalButton()
        if(self.selectedMode.get("excited",  False) == True):
           self.excitedButton()
        if(self.selectedMode.get("glasses",  False) == True):
            self.glassesButton()
        if(self.selectedMode.get("laugh",  False) == True):        
            self.laughButton()
        self.closeButton ()
    def nextFrameSlot(self):
        try:
            self.camera.resolution = (640, 480)
            self.camera.framerate = 30
            rawCapture = PiRGBArray(self.camera, size=(640, 480))
            # allow the camera to warmup
            time.sleep(0.1)
            # capture frames from the camera
            for frame in self.camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                # grab the raw NumPy array representing the image, then initialize the timestamp
                self.image = frame.array
                self.faces = self.face_cascade.detectMultiScale(self.image,  1.3,  5)
                for (x, y,  w,  h) in self.faces:
                    self.x = x
                    self.y = y
                    self.w = w
                    self.h = h
                    cv2.rectangle(self.image,  (x, y),  (x+w,  y+h),  (255, 0, 0),  2)
                img = QImage(self.image, self.image.shape[1], self.image.shape[0], QImage.Format_RGB888)
                # show the frame
                pixmap = QPixmap.fromImage(img)
                self.video_frame.setPixmap(pixmap)
                key = cv2.waitKey(1) & 0xFF
                # clear the stream in preparation for the next frame
                rawCapture.truncate(0)
                if key == ord("q"):
                    break
        except:
            QtWidgets.QMessageBox.critical(self,  "Starting Camera ",  "There is some problem with starting camera!, please check the camera and try again!")
            self.parent.close()
            self.camera.close()

    def start(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.nextFrameSlot)
        self.timer.start(100/30)
    def captureNormalFace(self):
        try:
            self.title = "Normal Face"
            sub_face = self.image[self.y:self.y+self.h, self.x:self.x+self.w]
            sub_file_name = self.empID+ "n.jpg"
            #print("face is : ",  sub_face)
            cv2.imwrite("Faces/"+sub_file_name, sub_face)
            self.photoButton.setEnabled(False)
            self.counter +=1
        except:
            QtWidgets.QMessageBox.warning(self,  "Capture Face ",  "Face not detected, please try again!")
    def captureExcitedFace(self):
            try:
                self.title = "Excited Face"
                sub_face = self.image[self.y:self.y+self.h, self.x:self.x+self.w]
                sub_file_name = self.empID + "e.jpg"
                #print("face is : ",  sub_face)
                cv2.imwrite("Faces/"+sub_file_name, sub_face)
                self.excited.setEnabled(False)
                self.counter +=1
            except:
                QtWidgets.QMessageBox.warning(self,  "Capture Face ",  "Face not detected, please try again!")
    def captureGlassesFace(self):
            try:
                self.title = "Glasses Face"
                sub_face = self.image[self.y:self.y+self.h, self.x:self.x+self.w]
                sub_file_name = self.empID+ "g.jpg"
                #print( " face is  : ",  sub_face)
                cv2.imwrite("Faces/"+sub_file_name, sub_face)
                self.glasses.setEnabled(False)
                self.counter +=1
            except:
                QtWidgets.QMessageBox.warning(self,  "Capture Face ",  "Face not detected, please try again!")
    def captureLaughFace(self):
            try:
                self.title = "Laugh Face"
                sub_face = self.image[self.y:self.y+self.h, self.x:self.x+self.w]
                sub_file_name = self.empID + "l.jpg"
                cv2.imwrite("Faces/"+sub_file_name, sub_face)
                #print( " face is  : ",  sub_face)
                self.laugh.setEnabled(False)
                self.counter +=1
            except:
                QtWidgets.QMessageBox.warning(self,  "Capture Face ",  "Face not detected, please try again!")
    def normalButton(self):
        self.photoButton = self.buttons.getButton("Normal Face", self.path )
        self.layout.addWidget(self.photoButton)
        self.photoButton.clicked.connect(self.captureNormalFace)
    def excitedButton(self):
        self.excited = self.buttons.getButton("Excited Face",  self.path)
        self.layout.addWidget(self.excited)
        self.excited.clicked.connect(self.captureExcitedFace)
    def glassesButton(self):
        self.glasses = self.buttons.getButton("Glasses Face",  self.path)
        self.layout.addWidget(self.glasses)
        self.glasses.clicked.connect(self.captureGlassesFace)
    def laughButton(self):
        self.laugh = self.buttons.getButton("Laugh Face",  self.path)
        self.layout.addWidget(self.laugh)
        self.laugh.clicked.connect(self.captureLaughFace)
    def closeButton(self):
        path = "Images/close.png"
        self.closeBtn = self.buttons.getButton("Close",  path)
        self.layout.addWidget(self.closeBtn)
        self.closeBtn.clicked.connect(self.closeWindow)
    def closeWindow(self):
        self.parent.close()
        self.cameraFlag = False
        if(self.counter == len(self.selectedMode)):
            QtWidgets.QMessageBox.information(self,  "Employee Registration ",  "Record SuccessFully Inserted!")
            self.parent.close()
            self.camera.close()
        else:
            QtWidgets.QMessageBox.warning(self,  "Employee Registration ",  "Record SuccessFully Inserted! But you didn't capture all faces that you select!")
            self.parent.close()
            self.camera.close()


