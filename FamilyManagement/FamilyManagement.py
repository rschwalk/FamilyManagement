"""
Family Management application - rschwalk 2018
The main file for the Flask application.
"""

from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from wtforms import Form, TextAreaField, StringField, PasswordField, validators
from passlib.hash import sha256_crypt
from data import items, UserData


app = Flask(__name__)


DATA_ITEMS = items()
# DATA_USERS = UserData().read_all()

@app.route('/')
def home():
    """ Home page """
    return render_template('home.html')

@app.route('/about')
def about():
    """ About page """
    return render_template('about.html')

@app.route('/items')
def items_page():
    """ Items page """
    return render_template('items.html', items=DATA_ITEMS)

@app.route('/item/<string:id>/')
def item(id):
    """ Item page """
    user_data = UserData().read_all()
    return render_template('item.html', item=user_data)


class RegisterForm(Form):
    """ Register form from WTForms """
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
        ])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        username = form.username.data
        password = sha256_crypt.encrypt(form.password.data)

        data = UserData()
        data.add_user(name, username, password)

        # flash('You are now registered, and can log in', 'success')
        return redirect(url_for('index'))
    
    return render_template('register.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
