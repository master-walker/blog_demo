#!/usr/bin/env python
#coding=utf-8

import os, json
from app import create_app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager,Shell
from app.models import User,Role

app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app,db)
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
    #json.dumps()

manager.add_command("shell",Shell(make_context=make_shell_context()))
manager.add_command("db",MigrateCommand)


if __name__ == "__main__":
    manager.run()