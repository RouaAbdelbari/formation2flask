import json
from flask import Flask, render_template, request

app = Flask(__name__)

registered_users = []

def is_valid_email(email):
    return email.count('@') == 1

def is_valid_password(password):
    return len(password) >= 6

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not is_valid_email(email):
            return "Veuillez entrer une adresse email valide."

        if not is_valid_password(password):
            return "Le mot de passe doit contenir au moins 6 caractères."

        return "Connexion réussie !"

def read_data_from_json():
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return [] 

def write_data_to_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not is_valid_email(email):
            return "Veuillez entrer une adresse email valide."

        if not is_valid_password(password):
            return "Le mot de passe doit contenir au moins 6 caractères."

        registered_users.append({'email': email, 'password': password})
        write_data_to_json(registered_users)
        return "Inscription réussie !"
    
@app.route('/users')
def show_users():
    registered_users = read_data_from_json()
    return render_template('users.html', users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)
