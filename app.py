from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not is_valid_email(email):
        return "Veuillez entrer une adresse email valide."
   
    if not is_valid_password(password):
        return "Le mot de passe doit contenir au moins 6 caractères."
  
    return "Connexion réussie !"

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')

    if not is_valid_email(email):
        return "Veuillez entrer une adresse email valide."


    if not is_valid_password(password):
        return "Le mot de passe doit contenir au moins 6 caractères."
    return "Inscription réussie !"

def is_valid_email(email):
   
    return True

def is_valid_password(password):
   
    return len(password) >= 6

if __name__ == '__main__':
    app.run(debug=True)

