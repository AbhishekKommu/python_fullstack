import sqlite3

from flask import Flask,render_template,jsonify,request,redirect,url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            dob TEXT NOT NULL,
            gender TEXT NOT NULL,
            course TEXT
        )
    """)
    conn.commit()
    cursor.execute("PRAGMA table_info(users)")
    existing_columns = [row[1] for row in cursor.fetchall()]
    if 'course' not in existing_columns:
        cursor.execute('ALTER TABLE users ADD COLUMN course TEXT')
        conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/trainers')
def trainers():
    return render_template("trainers.html")

@app.route('/register',methods=["POST","GET"])
def register():
    return render_template("register.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route('/api/register', methods=["POST"])
def api_register():
    data = request.get_json()
    email = data.get("email")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"status": "error", "message": "User already exists with this email!"}), 400
        
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, password, dob, gender, course) VALUES (?, ?, ?, ?, ?, ?)",
                   (data.get("name"), email, data.get("password"), data.get("dob"), data.get("gender"), data.get("course")))
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": "Registration successful!"})

@app.route('/api/login', methods=["POST"])
def api_login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()

    if user and user['password'] == password:
        return jsonify({"status": "success", "message": "Login successful! Welcome back."})
    else:
        return jsonify({"status": "error", "message": "Invalid email or password!"}), 401

if __name__ == '__main__':
    app.run(debug=True)