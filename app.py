from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "demo_secret_key")  # keep secret key in .env

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Dummy user class
class User(UserMixin):
    id = 1
    username = "demo"

@login_manager.user_loader
def load_user(user_id):
    return User()

# ------------------ ROUTES ------------------

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Login Page
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = User()
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('login.html')

# Signup Page (Placeholder)
@app.route('/signup')
def signup():
    return "Signup page coming soon"

# Dashboard (User Area)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Upload Lab Report
@app.route('/upload', methods=['GET','POST'])
@login_required
def upload():
    if request.method == 'POST':
        f = request.files['report']
        # Save uploaded report
        f.save(f'reports/{f.filename}')
        return "Report uploaded! AI explanation coming soon."
    return render_template('upload.html')

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
