#!/usr/bin/env python
#coding=utf-8


import sys, os
import codecs
import ConfigParser


src_path = os.path.abspath("..")
sys.path.append(src_path)
reload(sys)

base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
config_path =os.path.join(base_path,"utils","conf.ini")


class Read_Config(object):

    def __init__(self, path=config_path):

        config_parser = ConfigParser.ConfigParser()
        config_parser.readfp(codecs.open(path,"r","utf-8-sig"))

        self.base_path = base_path
        self.template_path = os.path.join(base_path,"requirements")

        # email data
        self.mail_server = config_parser.get("email","server")
        self.mail_port = config_parser.get("email","port")
        self.email_address = config_parser.get("email","email_address")
        self.password = config_parser.get("email","password")


if __name__ != "__main__":
    print config_path
    config = Read_Config()