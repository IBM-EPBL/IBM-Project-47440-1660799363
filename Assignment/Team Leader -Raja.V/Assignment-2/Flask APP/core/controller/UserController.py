from flask import request, Blueprint, jsonify, redirect, url_for,flash, render_template,session,json
from flask import session, app
from random import randint
import datetime
from datetime import timedelta,date,datetime,time
import requests, json
import hashlib
from werkzeug.utils import secure_filename

from os.path import join, dirname, realpath
import os
import flask
import functools 
import operator  

import urllib.parse
from flask import Flask
import pytz

# from twilio.rest import Client
# from translate import Translator

from core import app

from flask import Flask
from flask_mail import Mail, Message


mail = Mail(app)


app = Blueprint('user', __name__)




@app.route('/base')
def Base():
	return render_template('Test/base.html')  	

@app.route('/signup')
def Signup():
	return render_template('Test/signup.html')



@app.route('/login')
def Login():
	return render_template('Test/login.html')

@app.route('/home')
def Home():
	return render_template('Test/home.html')


@app.route('/blog')
def Blog():
	return render_template('Test/blog.html')			








	


			



	