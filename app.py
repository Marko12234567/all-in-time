from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

@app.route('/')
def hello_world():
    return render_template('signing.html')

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    # Check if email and password are not empty
    if not email or not password:
        flash('Email and password are required.', 'error')
        return redirect('/')

    # Check if email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        flash('Email already exists. Please log in.', 'error')
        return redirect('/')

    # Hash the password and save the user
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    flash('Registration successful! You can now log in.', 'success')
    return redirect('/')

# Run the app
if __name__ == '__main__':
    with app.app_context():  # Create app context for database creation
        db.create_all()  # Create the database and tables (only first time)
    app.run(debug=True)
