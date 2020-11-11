from flask import Flask, render_template, request, redirect, url_for
import readinput
import vector


data = []
querylist = []
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

@app.route('/query.html',methods =['POST']) #search input tapi belum rapih, 1 masalah 
def inputsearch():							#masalah : input sebelumnya blm kedelete
	query = request.form['q']				#input awal : aku kamu
	query_input = query.split()				#querynya : [{aku : 1, kamu :1}]
	counts = dict()							#terus kembali ke menu awal, input lagi
	for i in query_input:					#input selanjutnya : dia, suka
		counts[i] = counts.get(i, 0) + 1	# querynya : [{aku : 1, kamu : 1}, {dia : 1, suka :1}] aku,kamunya masih ada
	querylist.append(counts)
	return "<h1>querylist: {}</h1>".format(querylist) 


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

@app.route('/dbdic.html', methods=['POST'])
def upload_file():
    uploaded_file = request.files['Fileinput']
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
