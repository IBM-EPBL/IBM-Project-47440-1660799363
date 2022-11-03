from flask import Flask, url_for, request ,redirect
import os, time
import datetime
from datetime import datetime as dt
import traceback
import logging
app = Flask(__name__,static_url_path='/static')





config = app.config


current_app = app


from core.controller.UserController import app as user






app.register_blueprint(user, url_prefix='')




class SQLAlchemyHandler(logging.Handler):

    def emit(self, record):
        trace = None
        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc()

        path = request.path
        method = request.method
        ip = request.remote_addr    

        data = {
        		'url':path,
        		'logger_name':record.__dict__['name'],
                'level':record.__dict__['levelname'],
                'context':trace,
                'message':record.__dict__['msg'],
                'created_at':dt.now(),
                'ip_address':ip
            }    
        Log().insert(data)    
        # log = Log(
        #     logger=record.__dict__['name'],
        #     level=record.__dict__['levelname'],
        #     trace=trace,
        #     msg=record.__dict__['msg'],)
        # DB.session.add(log)
        # DB.session.commit()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ch = SQLAlchemyHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)




loggers = [logger, logging.getLogger('sqlalchemy'), logging.getLogger('flask.app')]

for l in loggers:
    l.addHandler(ch)


