# app/users/views.py

from flask import flash, render_template, redirect, url_for

from . import users
from .forms import CreateUserForm
from .. import db
from ..models import User


@users.route("/create_user", methods=['GET', 'POST'])
def create_user():
    """
    Creates a user on the database
    """
    form = CreateUserForm()
    if form.validate_on_submit():
        user = User(
                email=form.email.data, 
                password_hash=form.password.data, 
                name=form.name.data, 
                last_name=form.last_name.data
                )
        db.session.add(user)
        db.session.commit()
        flash('User creation successful')
        return redirect(url_for('auth.index'))

    return render_template('users/create_user.html', form=form, title='User Creation')

