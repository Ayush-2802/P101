# understanding get and post verbs

from flask import Flask,render_template,request,redirect,url_for
from pip._internal import req
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<html><h1>Hello Flask</h1></html>"

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"hello! {name}"
    return render_template('form.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score > 50 :
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html',results=res)

@app.route('/successres/<int:score>')
def successres (score):
    res = ""
    if score > 50 :
        res = "PASS"
    else:
        res = "FAIL"

    exp = {"score":score,"result":res}
    return render_template('result1.html',results=exp)

@app.route('/successif/<int:score>')
def successif (score):
    return render_template('result2.html',results=score)

@app.route('/res')
def res():
    return render_template('getresult.html')

@app.route('/sres',methods=['GET','POST'])
def sres():
    total = 0
    if request.method == 'POST':
        science = float(request.form.get('science'))
        maths = float(request.form.get('maths'))
        c = float(request.form.get('c'))
        datascience = float(request.form.get('datascience'))

        total = (science+maths+c+datascience)/4

    return redirect(url_for('successres',score=total))

if __name__=='__main__':
    app.run(debug=True)
