from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_email', methods=['POST'])
def check_email():
    email = request.form['email']
    if re.match(r'^[\w\.-]+@[a-zA-Z]+\.(com|in|org)$', email):
        result = "Valid"
    else:
        result = "Invalid"
    return render_template('result.html', email=email, result=result)

if __name__ == '__main__':
    app.run(debug=True)
