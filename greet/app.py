from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome_route():
  return 'welcome'

@app.route('/welcome/home')
def welc_home_route():
  return 'welcome home'

@app.route('/welcome/back')
def welc_back_route():
  return 'welcome back'