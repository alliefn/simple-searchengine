from flask import Flask, render_template, request, redirect, url_for
import readfile
import vector

app = Flask(__name__)

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
    return prosesinput('GET')

@app.route('/index.html', methods=['GET']) # Backup kalo user nginput di /index.html
def keyboard_input():
    return prosesinput('GET')

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(debug=True)
