from flask import Flask, redirect, url_for, render_template, request, session, Response
import re
from flask import Flask, redirect, url_for, render_template, request, session, Response
from datetime import timedelta
from flask import flash
from forms import RegistrationForm, LoginForm
import gc
from flask_mysqldb import MySQL
import yaml
import os
import cv2
import numpy as np
from camera import VideoCamera, UploadImage
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date
import MySQLdb


app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def hello_world():
    return 'Hello World gozo!'

@app.route("/aboutUs")
def aboutUs():
    return render_template("tutorial-components.html")

@app.route("/upload/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.files:
            # read image file string data
            filestr = request.files['image'].read()
            # convert string data to numpy array
            npimg = np.fromstring(filestr, np.uint8)
            # convert numpy array to image
            img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
            uri = upld.get_image(img)
            return render_template("upload.html", image=uri)
    flash("test")
    return render_template("upload.html")

@app.route('/video')
def index():
    return render_template('video.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
