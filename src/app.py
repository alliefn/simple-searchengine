from flask import Flask, render_template, request, redirect, url_for
from dataclasses import dataclass
import readinput
import vector
import nltk
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
nltk.download('punkt')
   
ps = PorterStemmer()
@dataclass
class dokumen:
        namafile: str
        savedata: str
        data: dict()
        simar: float = 0

querylist = []
doc = []
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

@app.route('/result.html',methods =['POST'])
def inputsearch():
  query = request.form['q']
  word = query.split()
  query_input = []
  for w in word:
          query_input.append(ps.stem(w))
  counts = dict()
  for i in query_input:
    counts[i] = counts.get(i, 0) + 1
  querylist = counts
  for x in doc:
    x.simar = vector.sim(querylist,x.data)
  vector.sortD(doc)
  return render_template('result.html', doc=doc)

@app.route('/', methods=['POST'])
def upload_file():
  uploaded_file = request.files.getlist('Fileinput')
  doc.clear()
  for file_to_upload in uploaded_file:
    content = file_to_upload.read().decode("utf-8")
    namafile = file_to_upload.filename
    word = content.split()
    content_list = []
    for w in word:
            content_list.append(ps.stem(w))
    counts = dict()
    for i in content_list:
      counts[i] = counts.get(i, 0) + 1
    doc.append(dokumen(namafile, content, counts))
  return render_template('index.html')


@app.route('/result/<judul>')
def result(judul):
        for s in doc:
                if s.namafile == judul:
                        break
        return "<h1>{}</h1>".format(s.savedata)


if __name__ == "__main__":
	app.run(debug=True)



