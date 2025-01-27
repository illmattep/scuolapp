from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from modules.models import User, db  # Import models and database
from modules.forms import LoginForm, RegisterForm  # Import forms
from modules.config import Logger
# Create a Blueprint for auth-related routes
auth = Blueprint('auth', __name__)

# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # Redirect if already logged in
        return redirect(url_for('home'))  # Replace 'home' with your homepage route

    form = LoginForm()
    if form.validate_on_submit():
        Logger.logthis(f'Login attempt for {form.username.data}', 'INFO')
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)  # Log the user in
            Logger.logthis(f'{user.username} logged in successfully', 'INFO')
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))  # Redirect to the homepage or dashboard
        else:
            Logger.logthis(f'Invalid login attempt for {form.username.data}', 'WARNING')
            flash('Invalid username or password', 'error')
    return render_template('login.html', form=form)

# Logout route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'warning')
    return redirect(url_for('auth.login'))

# Registration route
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
        Logger.logthis(f'New user registration: {form.username.data}', 'INFO')
        print(f'New user registration: {form.username.data}')
        new_user = User(username=form.username.data, password=hashed_password, role='student')
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')
    return render_template('register.html', form=form)
