from asyncio import wait
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Testimonial, Barber, Booking, User
from . import db
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, timedelta

views = Blueprint('views', __name__)

@views.route('/gallery', methods=['GET', 'POST'])
@login_required
def gallery():
    user_testimonials = Testimonial.query.filter_by(user_id=current_user.id).all()
    all_testimonials = Testimonial.query.all()

    if request.method == 'POST':
        testimonial_text = request.form.get('testimonial')

        if not testimonial_text or len(testimonial_text.strip()) < 1:
            flash('Testimonial is too short!', category='error')
        else:
            new_testimonial = Testimonial(data=testimonial_text, user_id=current_user.id)
            db.session.add(new_testimonial)
            db.session.commit()
            flash('Testimonial added!', category='success')

    return render_template("gallery.html", user=current_user, user_testimonials=user_testimonials,
                           all_testimonials=all_testimonials)

@views.route('/home', methods=['GET'])
def home():
    return render_template("home.html")

@views.route('/', methods=['GET'])
def index():
    return render_template("home.html")

@views.route('/booking', methods=['GET', 'POST'])
@login_required
def booking():
    if request.method == 'POST':
        barber_id = request.form.get('barber')
        service = request.form.get('service')
        date = request.form.get('date')
        time = request.form.get('time')
        phone_number = request.form.get('phone')

        # Convert date and time strings to datetime object for comparison
        booking_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

        try:
            # Check if the barber is free at the chosen time
            existing_bookings = Booking.query.filter(
                Booking.barber_id == barber_id,
                Booking.date == date
            ).all()

            barber_is_free = all(
                booking_datetime < datetime.strptime(f"{b.date} {b.time}", "%Y-%m-%d %H:%M") or
                booking_datetime > datetime.strptime(f"{b.date} {b.time}", "%Y-%m-%d %H:%M") + timedelta(minutes=30)
                for b in existing_bookings
            )

            if barber_is_free:
                new_booking = Booking(
                    barber_id=barber_id,
                    service=service,
                    date=date,
                    time=time,
                    phone_number=phone_number,
                    user_id=current_user.id
                )

                db.session.add(new_booking)
                db.session.commit()

                flash('Booking submitted successfully!', category='success')
                return redirect(url_for('views.booking'))
            else:
                flash('Barber is not available at the chosen time. Please select another time.', category='error')

        except SQLAlchemyError as e:
            db.session.rollback()
            flash('Error submitting booking. Please try again.', category='error')

    barbers = Barber.query.all()
    return render_template("appointement.html", user=current_user, barbers=barbers)

@views.route('/dashboard', methods=['GET', 'POST'])
@login_required
def appointment_dashboard():
    # Fetch all barbers for the filter dropdown
    all_barbers = Barber.query.all()

    # Initialize variables for filtering
    selected_date = request.form.get('selected_date')  # Get the selected date from the form

    # Fetch booked appointments with associated barber information, optionally filtered by date
    if selected_date:
        booked_appointments = db.session.query(Booking, Barber).join(Barber).filter(Booking.date == selected_date).all()
    else:
        booked_appointments = db.session.query(Booking, Barber).join(Barber).all()

    # Pass the appointments, barbers, and selected date to the template
    return render_template('appointment_dashboard.html', appointments=booked_appointments, all_barbers=all_barbers, selected_date=selected_date)

