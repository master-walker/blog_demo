#!/usr/bin/env python
#coding=utf-8

from datetime import datetime
from flask import render_template, session, redirect, url_for, request, flash
from . import main
from .forms import LoginForm, RegistrationForm
from ..models import User
from .. import db
from flask_login import login_user, login_required, logout_user

@main.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get("next") or url_for("main.index"))
        flash("Invalid username or password")
    return render_template("login.html", form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for("main.index"))

@main.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        flash("You can login now")
        return redirect(url_for("main.login"))
    return render_template("register.html",form=form)