from flask import Flask, render_template
from vercel_wsgi import handle_request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def handler(environ, start_response):
    return handle_request(app, environ, start_response)
