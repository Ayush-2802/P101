from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Hello Flask New World'

@app.route('/index')
def index():
    return 'This is index'

if __name__=='__main__':
    app.run(debug=True)

