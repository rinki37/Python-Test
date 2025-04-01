# API development guide -

# APIs (Application Programming Interfaces) allow applications to talk to each other. 

############################################

# Consuming an API

# import requests
# import json

# # a get request to get the resource. 
# response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# if response.status_code == 200:
    #print(response.json())

# for questions in response.json()['items']:
#     if questions['answer_count'] == 0:
#         print(questions['title'])
#         print(questions['link'])
#     else:
#         print("Skipped")


############################################

# Concepts of API development

#HTTP Methods or verbs

# Get - retrive data
# POST - Create new data
# PUT - Update existing data
# DELETE - Remove data
# PATCH - Partial update 



############################################
# Status code - denotes the return status of an API

# 200s: Success
# 400s: Client errors
# 500s: Server errors


############################################

# Data formats in API

# JSON (JavaScript Object Notation)
# XML
# Form data

############################################
# Create a simple flask API
# # Install - pip install flask

# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return "Hello world!"

# if __name__ == '__main__':
#     app.run(debug=True)



############################################

# Create a simple flask API to return json

# from flask import Flask, jsonify
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return jsonify({"message": "Hello, API"})

# if __name__ == '__main__':
#     app.run(debug=True)
    
############################################

