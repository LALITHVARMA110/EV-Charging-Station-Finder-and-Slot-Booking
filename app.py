from flask import Flask, render_template, request, redirect, url_for
from models import db, ChargingStation, Slot, Booking
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///charging_stations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    stations = ChargingStation.query.all()
    return render_template('index.html', stations=stations)

@app.route('/station/<int:station_id>')
def station(station_id):
    station = ChargingStation.query.get_or_404(station_id)
    return render_template('station.html', station=station)

@app.route('/book_slot', methods=['POST'])
def book_slot():
    station_id = request.form.get('station_id')
    slot_id = request.form.get('slot_id')
    user_name = request.form.get('user_name')
    
    slot = Slot.query.get(slot_id)
    if slot.is_available:
        booking = Booking(
            station_id=station_id,
            slot_id=slot_id,
            user_name=user_name,
            booking_time=datetime.now()
        )
        db.session.add(booking)
        slot.is_available = False
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return "Slot already booked!"

if __name__ == '__main__':
    app.run(debug=True)
