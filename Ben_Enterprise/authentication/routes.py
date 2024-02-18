from datetime import datetime
from flask import Blueprint, redirect, render_template, url_for
from .forms import SignupForm
from .models import User

signup_blueprint = Blueprint('signup', __name__, template_folder='templates')

@signup_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    password=form.password.data,
                    token='',
                    date_created=datetime.datetime.utcnow())
        user.save()
        flash('Signup successful!')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)