import json
import jwt
from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'ma_cle_secrete'

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

        # Vérifier les informations d'authentification ici (à compléter selon vos besoins)
        if email == 'votre_email_valide' and password == 'votre_mot_de_passe_valide':
            # Créer un JWT avec l'e-mail de l'utilisateur
            payload = {'email': email}
            token = jwt.encode(payload, app.secret_key, algorithm='HS256')
            
            # Enregistrez le JWT dans la session de l'utilisateur
            session['user_token'] = token
            
            return redirect(url_for('show_users'))
        else:
            return "Identifiants invalides. Veuillez réessayer."

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

def get_user_data(email):
    for user in registered_users:
        if user['email'] == email:
            return user
    return None

@app.route('/users')
def show_users():
    # Vérifier si l'utilisateur est authentifié en vérifiant la présence du JWT dans la session
    if 'user_token' in session:
        try:
            # Décoder le JWT pour obtenir l'e-mail de l'utilisateur
            token = session['user_token']
            payload = jwt.decode(token, app.secret_key, algorithms=['HS256'])
            email = payload['email']

            # Utilisez l'e-mail pour obtenir les informations de l'utilisateur à afficher
            user_data = get_user_data(email)

            return render_template('users.html', users=[user_data])
        except jwt.ExpiredSignatureError:
            return "Session expirée. Veuillez vous connecter à nouveau."
        except jwt.InvalidTokenError:
            return "Session invalide. Veuillez vous connecter à nouveau."
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
