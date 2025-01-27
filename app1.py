from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Ініціалізація бази даних
def init_db():
    with sqlite3.connect('users.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

# Головна сторінка (з вашим HTML)
@app.route('/')
def home():
    return render_template('signing.html')  # Помістіть HTML-код в файл `templates/index.html`

# Обробка реєстрації
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']

    try:
        with sqlite3.connect('users.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
            conn.commit()
        return "Registration successful!"
    except sqlite3.IntegrityError:
        return "Email already exists!", 400

if __name__ == '__main__':
    init_db()  # Ініціалізуємо базу даних
    app.run(debug=True)
