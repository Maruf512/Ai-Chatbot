from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db


views = Blueprint("views", __name__, static_url_path='/static')


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', user=current_user)




