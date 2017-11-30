#!/usr/bin/env python
#coding=utf-8

from flask_mail import Mail,Message
from flask import render_template, current_app
from app import mail
from utils.read_config import config
from threading import Thread


# 异步发送邮件
def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config["MAIL_SUBJECT_PREFIX"] + subject, sender=app.config["MAIL_SENDER"],recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    # mail.send(msg)
    thr = Thread(target=send_async_email,args=[app,msg])
    thr.start()
    return thr