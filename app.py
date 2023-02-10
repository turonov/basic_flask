from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello_word():
    r=request.args
    name=r['name']
    data = {
        "apple":14,
        "banana":1,
        "orange":4,
        "grape":10
    }
    return {name:data.get(name,'Not Found')}

@app.route('/home')
def home():
    return "Home page"

@app.route('/index')
def index():
    return "Index page"

@app.route('/page')
def page():
    return "page"

if __name__ == '__main__':
    app.run()