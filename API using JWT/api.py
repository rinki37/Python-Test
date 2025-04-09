from flask import Flask, request, jsonify, make_response, render_template
import jwt  
from datetime import datetime, timedelta
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a5f99d87a7864861b1d614c72a8095ab'

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
    print("Request Data:", request.data)  
    print("Request JSON:", request.get_json())  
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
      
    token = jwt.encode(
        {
            'user': username,
            'exp': datetime.now() + timedelta(minutes=1)
        },
        app.config['SECRET_KEY'],
        algorithm='HS256'
    )
        
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(debug=True, port=9001)