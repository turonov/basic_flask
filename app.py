from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
    return "Hello Word"

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