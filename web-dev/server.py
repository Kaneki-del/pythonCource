from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

def write_to(data):
    with open("data-base.txt", "a") as f:
        email = data['email']
        name = data['name']
        subject = data['subject']
        message = data['subject']
        f.write(f'email: {email}\nname: {name}\nsubject: {subject}\nmessage: {message}\n')


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            write_to(data)
    except:
        return  'noting has ben saved in the data-base'
    return 'somthing is went wrong '
