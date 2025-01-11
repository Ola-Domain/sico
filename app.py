from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired
from flask_wtf.csrf import CSRFProtect
import sqlite3

app = Flask(__name__)
app.secret_key = '903d40cfdaf17dab3e286e6ffe7a15d8783585bd1360cb6f6c9256ede2bf6a47'  # Set a secret key for CSRF protection
csrf = CSRFProtect(app)

# Database initialization
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, filepath TEXT, caption TEXT)')
    conn.close()

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    video = FileField('Video', validators=[InputRequired()])
    caption = StringField('Caption', validators=[InputRequired()])

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT filepath, caption FROM videos')
    videos = [{'filepath': row[0], 'caption': row[1]} for row in cursor.fetchall()]
    conn.close()
    return render_template('index.html', videos=videos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        conn = sqlite3.connect('database.db')
        cursor = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        if user:
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        conn = sqlite3.connect('database.db')
        cursor = conn.execute('SELECT * FROM users WHERE username = ?', (username,))
        if cursor.fetchone():
            flash('Username already exists')
        else:
            conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        video = form.video.data
        caption = form.caption.data
        filepath = 'uploads/' + video.filename
        video.save('static/' + filepath)
        conn = sqlite3.connect('database.db')
        conn.execute('INSERT INTO videos (filepath, caption) VALUES (?, ?)', (filepath, caption))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
