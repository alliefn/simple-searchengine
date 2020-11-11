from flask import Flask, render_template
import prosesinput
import cosines

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html') #render template di homepage.html

@app.route('/index.html')
def home2():
	return render_template('index.html') #render template di homepage.html

@app.route('/aboutus.html') # Pindah dari localhost:5000 ke localhost:5000/about
def about():
	return render_template('aboutus.html')

@app.route('/howtouse.html')
def howuse():
	return render_template('howtouse.html')

@app.route('/', methods=['GET'])
def my_form_post():
    return prosesinput('GET')

@app.route('/index.html', methods=['GET']) # Backup kalo user nginput di /index.html
def my_form_post2():
    return prosesinput('GET')

if __name__ == "__main__":
	app.run(debug=True)
