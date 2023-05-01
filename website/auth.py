from flask import blueprints, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db

auth = blueprints("auth", __name__, static_url_path='/static')


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # get data from webpage
        email = request.form.get('email')
        password = request.form.get("password")
        # get data from database
        user = User.query.filter_by(email=email).first()
        print(user)
        if user:
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        
    return render_template('login.html', user=current_user)


