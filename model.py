from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ChargingStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    slots = db.relationship('Slot', backref='station', lazy=True)

class Slot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.Integer, db.ForeignKey('charging_station.id'), nullable=False)
    is_available = db.Column(db.Boolean, default=True, nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.Integer, db.ForeignKey('charging_station.id'), nullable=False)
    slot_id = db.Column(db.Integer, db.ForeignKey('slot.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    booking_time = db.Column(db.DateTime, nullable=False)
