import cv2
from model import FacialExpressionModel
import numpy as np
import base64
import io
from PIL import Image


facec = cv2.CascadeClassifier(
    './facedetect/haarcascade_frontalface_default.xml')
model = FacialExpressionModel()
font = cv2.FONT_HERSHEY_SIMPLEX


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    # returns camera frames along with bounding boxes and predictions
    def get_frame(self):
        _, fr = self.video.read()
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)

        for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]

            roi = cv2.resize(fc, (100, 100))
            roi = roi/255.0
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

            cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
            cv2.rectangle(fr, (x, y), (x+w, y+h), (255, 0, 0), 2)

        _, jpeg = cv2.imencode('.jpg', fr)
        return jpeg.tobytes()


class UploadImage(object):

    def get_image(self, img):
        gray_fr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)
        if len(faces) == 0:
            return 0
        else:
            for (x, y, w, h) in faces:
                fc = gray_fr[y:y+h, x:x+w]

                roi = cv2.resize(fc, (100, 100))
                roi = roi/255.0
                pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

                cv2.putText(img, pred, (x, y), font, 1, (255, 255, 0), 2)
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                #cv2.imwrite("D:/facial_emotion/img/image.jpg", img)

            img = Image.fromarray(img.astype("uint8"))
            rawBytes = io.BytesIO()
            img.save(rawBytes, "JPEG")
            rawBytes.seek(0)
            img_base64 = base64.b64encode(rawBytes.getvalue()).decode('ascii')
            mime = "image/jpeg"
            uri = "data:%s;base64,%s" % (mime, img_base64)
            return uri

       # _, jpeg = cv2.imencode('.jpg', img)
       # return base64.b64encode(img.tobytes())

    def predictEmotionOfImage(self, img):
        gray_fr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = facec.detectMultiScale(gray_fr, 1.3, 5)
        if len(faces) == 0:
            pred = "No face"
        else:
            for (x, y, w, h) in faces:
                fc = gray_fr[y:y+h, x:x+w]
                roi = cv2.resize(fc, (100, 100))
                roi = roi/255.0
                pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

        return pred
