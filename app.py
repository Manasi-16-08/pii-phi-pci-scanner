from flask import Flask, request, render_template, jsonify
from database import db, Scan
from scanner import scan_file
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scans.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db.init_app(app)
# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def index():
    return render_template('upload.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        # Scan the file
        with open(filepath, 'r') as f:
            content = f.read()
        results = scan_file(content)

        # Store results in the database
        for result in results:
            scan_entry = Scan(
                file_name=filename,
                found_data=str(result["matches"]),
                data_type=result["data_type"],
                file_path=filepath,
            )
            db.session.add(scan_entry)
        db.session.commit()
        return f"File '{filename}' uploaded and scanned successfully!"
    return "Invalid file type", 400
@app.route('/scans', methods=['GET'])
def get_scans():
    scans = Scan.query.all()
    return render_template('scans.html', scans=scans)
@app.route('/delete/<int:id>', methods=['POST'])
def delete_scan(id):
    scan = Scan.query.get(id)
    if scan:
        os.remove(scan.file_path)  # Remove uploaded file
        db.session.delete(scan)
        db.session.commit()
        return f"Scan {id} deleted successfully!", 200
    return "Scan not found", 404
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)
