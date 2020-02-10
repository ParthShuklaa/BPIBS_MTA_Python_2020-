import flask
from flask import Flask
from flask import render_template

app = Flask(__name__,template_folder='template')

@app.route('/index')
def message():
    return "<h1>Welcome to my Web Page ......</h1><h2>developed using Flask </h2>"

@app.route('/contactUs')
def Contact():
    return "You can contact us on our official Website"

@app.route('/AboutMySelf')
def Info():
    return render_template('Myinfo.html')

if __name__ == '__main__':
    app.run()
