from flask import Flask, request, jsonify, make_response, render_template, redirect, url_for
import jwt  
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5f99d87a7864861b1d614c72a8095ab'

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return render_template('error.html', message="Token is missing!"), 403
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return render_template('error.html', message="Token has expired"), 403
        except jwt.InvalidTokenError:
            return render_template('error.html', message="Invalid token"), 403

        return func(*args, **kwargs) 
    return decorated 

# Public route
@app.route('/public')
def public():
    return render_template('public.html')   

# Authenticated route
@app.route('/auth')
@token_required
def auth():
    return render_template('auth.html')

# Home route    
@app.route('/')
def home():
    return render_template('login.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if not request.form.get('username') or not request.form.get('password'):
            return render_template('login.html', error='Username and password required')
        
        if request.form['password'] == "12345":
            token = jwt.encode(
                {
                    'user': request.form['username'],
                    'exp': datetime.now() + timedelta(seconds=120)
                },
                app.config['SECRET_KEY'],
                algorithm='HS256'
            )
            
            return render_template('success.html', token=token)
        else:
            return render_template('login.html', error='Authentication failed')
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, port=9001)