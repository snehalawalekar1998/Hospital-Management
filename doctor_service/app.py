from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doctors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    specialization = db.Column(db.String(80), nullable=False)
    available = db.Column(db.Boolean, default=True)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/doctors', methods=['POST'])
def create_doctor():
    doctor_data = request.get_json()
    doctor = Doctor(
        name=doctor_data['name'],
        specialization=doctor_data['specialization'],
        available=doctor_data.get('available', True)
    )
    db.session.add(doctor)
    db.session.commit()
    return jsonify({'id': doctor.id, 'name': doctor.name, 'specialization': doctor.specialization, 'available': doctor.available}), 201

@app.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if doctor:
        return jsonify({'id': doctor.id, 'name': doctor.name, 'specialization': doctor.specialization, 'available': doctor.available})
    else:
        return jsonify({'error': 'Doctor not found'}), 404

@app.route('/doctors', methods=['GET'])
def list_doctors():
    doctors = Doctor.query.all()
    return jsonify([{'id': d.id, 'name': d.name, 'specialization': d.specialization, 'available': d.available} for d in doctors])

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
