from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    doctor_id = db.Column(db.Integer, nullable=False)
    appointment_date = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Scheduled")

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/appointments', methods=['POST'])
def create_appointment():
    appointment_data = request.get_json()
    appointment = Appointment(
        patient_id=appointment_data['patient_id'],
        doctor_id=appointment_data['doctor_id'],
        appointment_date=appointment_data['appointment_date']
    )
    db.session.add(appointment)
    db.session.commit()
    return jsonify({
        'id': appointment.id,
        'patient_id': appointment.patient_id,
        'doctor_id': appointment.doctor_id,
        'appointment_date': appointment.appointment_date,
        'status': appointment.status
    }), 201

@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment:
        return jsonify({
            'id': appointment.id,
            'patient_id': appointment.patient_id,
            'doctor_id': appointment.doctor_id,
            'appointment_date': appointment.appointment_date,
            'status': appointment.status
        })
    else:
        return jsonify({'error': 'Appointment not found'}), 404

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def cancel_appointment(appointment_id):
    appointment = Appointment.query.get(appointment_id)
    if appointment:
        appointment.status = 'Cancelled'
        db.session.commit()
        return jsonify({
            'message': 'Appointment cancelled',
            'id': appointment.id,
            'patient_id': appointment.patient_id,
            'doctor_id': appointment.doctor_id,
            'appointment_date': appointment.appointment_date,
            'status': appointment.status
        })
    else:
        return jsonify({'error': 'Appointment not found'}), 404

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

