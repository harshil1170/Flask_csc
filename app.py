from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html")
    
print("Current working directory:", os.getcwd())

if __name__ == '__main__':
    app.run(debug=True)
