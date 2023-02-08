from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
    return "Hello Word"
@app.route('/home')
def home():
    return "home page"

if __name__ == '__main__':
    app.run()