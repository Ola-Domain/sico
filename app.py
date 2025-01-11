from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database initialization
def init_db():
    conn = sqlite3.connect('database.db')
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    conn.execute('CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, filepath TEXT, caption TEXT)')
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.execute('SELECT filepath, caption FROM videos')
    videos = [{'filepath': row[0], 'caption': row[1]} for row in cursor.fetchall()]
    conn.close()
    return render_template('index.html', videos=videos)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Add authentication logic here
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        video = request.files['video']
        caption = request.form['caption']
        filepath = 'uploads/' + video.filename
        video.save('static/' + filepath)

        conn = sqlite3.connect('database.db')
        conn.execute('INSERT INTO videos (filepath, caption) VALUES (?, ?)', (filepath, caption))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('upload.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
