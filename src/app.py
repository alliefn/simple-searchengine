from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import readfile
import vector

app = Flask(__name__)

#database blum selesai

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/kali/Tubes Algeo 2/database/database.db' #database path
db = SQLAlchemy(app)

class FileContainer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	data = db.Column(db.LargeBinary)
#sampe sini database

@app.route('/')
def home():
	return render_template('index.html') #render template di homepage.html

@app.route('/index.html')
def home2():
	return render_template('index.html') #render template di homepage.html

@app.route('/aboutus.html') # Pindah dari localhost:5000 ke localhost:5000/aboutus.html
def about():
	return render_template('aboutus.html')

@app.route('/howtouse.html')  # Pindah dari localhost:5000 ke localhost:5000/howtouse.html
def howuse():
	return render_template('howtouse.html')


@app.route('/', methods=['GET'])
def keyboard_input():
    return readfile('GET')

@app.route('/index.html', methods=['GET']) # Backup kalo user nginput di /index.html
def keyboard_input():
    return readfile('GET')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(debug=True)
