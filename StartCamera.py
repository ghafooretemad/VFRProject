import cv2
from picamera.array import PiRGBArray
from PyQt5.QtWidgets import QLabel,  QWidget,  QVBoxLayout
from PyQt5.QtGui import QPixmap
from picamera import PiCamera
class StartCamera(QWidget):
    def __init__(self,  selectedMode,  empID, parent = None):
        super(StartCamera,  self).__init__(parent)
        self.selectedMode = selectedMode
        self.empID = empID
        self.layout = QVBoxLayout()
        self.width = 500
        self.height  = 400
        self.top = 20
        self.left = 30
        self.setupUi()
        self.show()
    def setupUi(self):
        self.setGeometry(self.top,  self.left,  self.width,  self.height)
        self.start()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
    def start(self):
        face_cascade = cv2.CascadeClassifier('../../../opencv-3.1.0/data/haarcascades/haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('../../../opencv-3.1.0/data/haarcascades/haarcascade_eye.xml')
       
        camera = PiCamera()
        camera.framerate  = 30
        camera.resolution = (640, 480)
        rawCapture = PiRGBArray(camera,  size = (640,  480))
        #fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.label = QLabel()
        #out = cv2.VideoWriter('output.mkv',  fourcc,  20.0 ,  (640, 480))
        for frame in camera.capture_continuous(rawCapture,  format='bgr',  use_video_port = True):
            grayImage = frame.array
            #grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(grayImage,  1.3,  5)
            for (x, y,  w,  h) in faces:
                cv2.rectangle(grayImage,  (x, y),  (x+w,  y+h),  (255, 0, 0),  2)
                roi_gray = grayImage[y:y+h,  x:x+w]
                roi_color = grayImage[y:y+h,  x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,  ey,  ew, eh) in eyes:
                    cv2.rectangle(roi_color,  (ex,  ey),  (ex+ew,  ey+eh),  (0,  255,  0),  2)
            #pixmap = QPixmap(grayImage)
            #self.label.setPixmap(pixmap)
            cv2.imshow("Camera",  grayImage)
            rawCapture.truncate(0)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        #out.release()
        cv2.destroyAllWindows()
