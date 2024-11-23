from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define a Scan model for storing file scan details
class Scan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(120), nullable=False)
    scan_timestamp = db.Column(db.DateTime, default=db.func.now())
    found_data = db.Column(db.Text, nullable=False)  # JSON string of found data
    data_type = db.Column(db.String(50), nullable=False)  # PII, PHI, PCI
    file_path = db.Column(db.String(200), nullable=False)
