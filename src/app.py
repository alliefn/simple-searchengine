from flask import Flask, render_template, request, redirect, url_for
import readfile
import vector


data = []
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

'''
@app.route('/', methods=['POST'])
def keyboard_input():
	userinput = request.files['q']
	content = userinput.read()
	content_list = content.split()
    counts = dict()
    for i in content_list:
      counts[i] = counts.get(i, 0) + 1
    data.append(counts)
    return "<h1>data: {}</h1>".format(data)

@app.route('/index.html', methods=['POST']) # Backup kalo user nginput di /index.html
def keyboard_input2():
	userinput = request.files['q']
	content = userinput.read()
	content_list = content.split()
    counts = dict()
    for i in content_list:
      counts[i] = counts.get(i, 0) + 1
    data.append(counts)
    return "<h1>data: {}</h1>".format(data)
'''

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    content = uploaded_file.read()
    content_list = content.split()
    
    counts = dict()
    for i in content_list:
      counts[i] = counts.get(i, 0) + 1
    data.append(counts)
    return "<h1>data: {}</h1>".format(data)
"""
@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('index'))
"""
if __name__ == "__main__":
	app.run(debug=True)
