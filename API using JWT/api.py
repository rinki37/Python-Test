from flask import Flask, request, jsonify, make_response, render_template
import jwt  
from datetime import datetime, timedelta
from functools import wraps
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5f99d87a7864861b1d614c72a8095ab'
app.config['REFRESH_SECRET_KEY'] = 'a5f99d87a7864861b1d614c72a80ab'

# In-memory db
users_db = {
    "admin": {
        "username": "admin",
        "password": "admin123", 
        "role": "admin"
    },
    "user1": {
        "username": "user1",
        "password": "password123",
        "role": "user"
    }
}

refresh_tokens_store = set()
revoked_tokens = set()
blacklisted_access_token = set()

# Initilize the limiter
limiter = Limiter(app=app, key_func=get_remote_address, default_limits=["200 per day"])

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
       # token = request.args.get('token') # If coming from query string
        token = None
        
        # If authorization header is present, extract the token from bearer token
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
            
        if not token:
            return jsonify({'message': "Token is missing!"}), 401 # Unauthorized
        
        
        if token in blacklisted_access_token:
            return jsonify({"message" : "Token has been revoked"}), 403
        
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': "Token has expired"}), 403 # Forbidden
        except jwt.InvalidTokenError:
            return jsonify({'message': "Invalid token"}), 403

        return func(*args, **kwargs) 
    return decorated 

# Public route (can be accessed without token)
@app.route('/public')
def public():
    return jsonify({"message" : 'For everyone'}), 200 # Ok   

# Authenticated route( requires token)
@app.route('/auth')
@token_required
@limiter.limit("2 per minute")
def auth():
    return jsonify({"message" : 'JWT authentication successful.'}), 200 # Ok

# Home route (login page) 
@app.route('/')
def home():
    return jsonify({"message" : "This is home page"}), 200 # Ok

# Registration route
@app.route('/register', methods =['POST'])
def register():
    if not request.is_json:
        return jsonify({"message" : "Request must be JSON"}), 400
    
    data = request.get_json()
    
    if not data.get('username') or not data.get('password'):
        return jsonify({'message' : "Username and password are required"}), 400
    
    username = data['username']
    if username in users_db:
        return jsonify({"message" : "User already exists"}), 409 # Conflict
    
    users_db[username] = {
        "username" : username,
        "password" : data['password'],
        "role" : 'user'
    }
    
    return jsonify({"message" :  "Registration successful"}), 201 # Created
         
# Login route (if user exists, generate jwt token for them) 
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"message" : "Request must be JSON"}), 400 # Bad request
    
    data  = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    
    if username not in users_db:
        return jsonify({"message" : "User not found"}), 404 # Not found
    
    # Check if password is correct
    if not users_db[username]['password'] ==  password:
        return jsonify({"message" : "Invalid password"}), 401 # Unauthorized
      
    access_token = jwt.encode(
        {
            'user': username,
            'exp': datetime.now() + timedelta(minutes=1)
        },
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )
    
    refresh_token = jwt.encode(
        {
            'user' : username,
            'exp' : datetime.now() + timedelta(minutes = 10)
        },
        app.config['REFRESH_SECRET_KEY'],
        algorithm='HS256'
    )
    refresh_tokens_store.add(refresh_token)
        
    return jsonify({
        'access_token': access_token, 
        'refresh_token' : refresh_token
    }), 200

@app.route('/refresh', methods=['POST'])
def refresh():
    if not request.is_json:
        return jsonify({"message": "Request must be JSON"}), 400

    refresh_token = request.get_json().get('refresh_token')
    if not refresh_token:
        return jsonify({"message": "Request must contain refresh token"}), 400

    if refresh_token not in refresh_tokens_store:
        return jsonify({"message": "Invalid refresh token"}), 403

    try:
        payload = jwt.decode(
            refresh_token,
            app.config['REFRESH_SECRET_KEY'],
            algorithms=['HS256']  # ✅ Fixed: Plural 'algorithms'
        )
    except jwt.ExpiredSignatureError:
        refresh_tokens_store.discard(refresh_token)
        return jsonify({"message": "Refresh token expired. Login again."}), 403
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid refresh token"}), 403

    new_access_token = jwt.encode(
        {
            'user': payload['user'],
            'exp': datetime.now() + timedelta(minutes=1)
        },
        app.config['SECRET_KEY'],
        algorithm='HS256'  # ✅ Singular 'algorithm'
    )

    return jsonify({"access_token": new_access_token}), 200

# Logout to remove refresh token from store
@app.route('/logout', methods=['POST'])
def logout():
    if not request.is_json:
        return jsonify({"message" : "Request must be JSON"}), 400
    
    refresh_token = request.get_json().get('refresh_token')
    access_token = request.headers['Authorization'].split(" ")[1]
    if not refresh_token:
        return jsonify({"message" : "Refresh token required"}), 400
    
    blacklisted_access_token.add(access_token)
    
    if refresh_token in refresh_tokens_store:
        revoked_tokens.add(refresh_token)
        refresh_tokens_store.discard(refresh_token)
        return jsonify({
            "message" : "Logout successful",
            "access_token_revoked" :  True,
            "refresh_token_revoked" : True
            }), 200
    else:
        return jsonify({
            "message" : "Partial logout. Invalid refresh token",
            "access_token_revoked" : True,
            "refresh_token_revoked" : False
            }), 200
        
if __name__ == '__main__':
    app.run(debug=True, port=9001)