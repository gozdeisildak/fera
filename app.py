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


@app.route('/')
def hello_world():
    return 'Hello World gozo!'

@app.route("/aboutUs")
def aboutUs():
    return render_template("tutorial-components.html")

if __name__ == '__main__':
    app.run()
