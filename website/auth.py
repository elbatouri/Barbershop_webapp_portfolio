from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

# Create a Blueprint for authentication
auth = Blueprint('auth', __name__)

# Route for user login
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve email and password from the login form
        email = request.form.get('email')
        password = request.form.get('password')

        # Query the database for the user with the provided email
        user = User.query.filter_by(email=email).first()
        
        # Check if the user exists and the password is correct
        if user and check_password_hash(user.password, password):
            # Log in the user and redirect to the home page
            flash('Logged in successfully!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        else:
            # Display an error message if login fails
            flash('Incorrect email or password. Please try again.', category='error')

    return render_template("login.html", user=current_user)

# Route for user logout
@auth.route('/logout')
@login_required
def logout():
    # Log out the user and redirect to the home page
    logout_user()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('views.home'))

# Route for user sign-up
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Retrieve user information from the sign-up form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check for existing email, validate inputs, and create a new user
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists. Please choose a different email.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match. Please enter the same password in both fields.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Create a new user, add to the database, and log in
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                            password1, method='pbkdf2:sha256', salt_length=8))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully. You are now logged in.', category='success')
            return redirect(url_for('views.home'))

    # Render the sign-up template with the current user information
    return render_template("sign_up.html", user=current_user)
