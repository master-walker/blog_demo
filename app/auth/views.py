#!/usr/bin/env python
#coding=utf-8

from datetime import datetime
from flask import render_template, session, redirect, url_for, request, flash
from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import User
from .. import db
from utils.common import send_mail
from flask_login import login_user, login_required, logout_user, current_user

@auth.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember_me.data)
            return redirect(request.args.get("next") or url_for("main.index"))
        flash("Invalid username or password")
    return render_template("login.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for("main.index"))

@auth.route("/confirm/<token>")
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for("main.index"))
    if current_user.confirm(token):
        db.session.commit()
        flash("You have confirmed your account,Thanks!")
    else:
        flash("The confirmation is invalid or has expired.")
    return redirect(url_for("main.index"))

@auth.route("/confirm")
@login_required
def resend_confirmation()
    pass

@auth.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_mail(user.email, "Confirm Your Account", "auth/email/confirm", user=user, token=token)
        flash("The confirmation email has been sent to you by email.")
        # flash("You can login now")
        return redirect(url_for("main.index"))
    return render_template("register.html",form=form)