from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    medical_history = db.Column(db.Text, nullable=True)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/patients', methods=['POST'])
def create_patient():
    patient_data = request.get_json()
    patient = Patient(
        name=patient_data['name'],
        age=patient_data['age'],
        gender=patient_data['gender'],
        medical_history=patient_data.get('medical_history', '')
    )
    db.session.add(patient)
    db.session.commit()
    return jsonify({'id': patient.id, 'name': patient.name, 'age': patient.age, 'gender': patient.gender, 'medical_history': patient.medical_history}), 201

@app.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if patient:
        return jsonify({'id': patient.id, 'name': patient.name, 'age': patient.age, 'gender': patient.gender, 'medical_history': patient.medical_history})
    else:
        return jsonify({'error': 'Patient not found'}), 404

@app.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    patient_data = request.get_json()
    patient = Patient.query.get(patient_id)
    if patient:
        # Update only the fields provided in the request
        patient.name = patient_data.get('name', patient.name)
        patient.age = patient_data.get('age', patient.age)
        patient.gender = patient_data.get('gender', patient.gender)
        patient.medical_history = patient_data.get('medical_history', patient.medical_history)
       
        db.session.commit()
        return jsonify({'id': patient.id, 'name': patient.name, 'age': patient.age, 'gender': patient.gender, 'medical_history': patient.medical_history})
    else:
        return jsonify({'error': 'Patient not found'}), 404

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

