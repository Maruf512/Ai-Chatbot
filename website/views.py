from flask import blueprints, render_template
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db


views = blueprints("views", __name__, static_url_path="/static")

@views.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', user=current_user)




