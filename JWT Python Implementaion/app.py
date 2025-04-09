from flask import Flask, request, jsonify, make_response, render_template
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
            return jsonify({'message': "Token is missing!"}), 403
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': "Token has expired"}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': "Invalid token"}), 403

        return func(*args, **kwargs) 
    return decorated 

# Public
@app.route('/public')
def public():
    return 'For everyone'   

# Authenticated 
@app.route('/auth')
@token_required
def auth():
    return 'JWT authentication successful.'

# Home    
@app.route('/')
def home():
    return render_template('login.html')

# Login    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("Form Data:", request.form)
        if not request.form.get('username') or not request.form.get('password'):
            return make_response('Username and password required', 400)
        
        if request.form['password'] == "12345":
            token = jwt.encode(
                {
                    'user': request.form['username'],
                    'exp': datetime.now() + timedelta(seconds=120)
                },
                app.config['SECRET_KEY'],
                algorithm='HS256'
            )
            
            return jsonify({'token': token})
        else:
            return make_response('Could not verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication failed!"'})
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, port=9001)