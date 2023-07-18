from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    
    if email == 'example@example.com' and password == 'password':
        return 'Connexion réussie !'
    else:
        return 'Identifiants invalides. Veuillez réessayer.'

if __name__ == '__main__':
    app.run(debug=True)
