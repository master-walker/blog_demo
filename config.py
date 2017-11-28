#!/usr/bin/env python
#coding=utf-8

import os
from utils.read_config import config

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SUBJECT_PREFIX = "[FLASK]"
    MAIL_SENDER = "FLASK ADMIN <{0}>".format(config.email_address)

    @staticmethod
    def init_app():
        pass

class DevConfig(Config):
    DEBUG = True
    MAIL_SERVER = config.mail_server
    MAIL_PORT = config.mail_port
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.email_address
    MAIL_PASSWORD = config.password
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(config.base_path, 'data-dev.sqlite')

config = {
    "devConfig": DevConfig
}
