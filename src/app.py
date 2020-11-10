from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html') #render template di homepage.html
@app.route('/aboutus.html') # Pindah dari localhost:5000 ke localhost:5000/about
def about():
	return render_template('aboutus.html')
@app.route('/howtouse.html')
def howuse():
	return render_template('howtouse.html')
@app.route('/logo.jpg')
def pics():
	return render_template('logo.jpg')
if __name__ == "__main__":
	app.run(debug=True)