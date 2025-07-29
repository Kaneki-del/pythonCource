from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
    return redirect('/tanks.html')

