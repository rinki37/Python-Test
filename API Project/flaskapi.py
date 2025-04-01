# Create a simple flask API to return json

# from flask import Flask, jsonify
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return jsonify({"message": "Hello, API"})

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, request
app = Flask(__name__)


students = [
    {"id": 1, "name":"Riya", "age":24},
    {"id": 2, "name":"Sara", "age":22}
]

# GET - Get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


# GET - Get a student by id
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404


# POST - Add a new student. 
# In postman, after entering the route and selecting POST - In Body, raw, json enter below -
# {
#     "name" : "Akansha",
#     "age" : 23
# }
 
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    if "name" not in data or "age" not in data:
        return jsonify({"error" : "Invalid data"}), 400
    
    new_student = {
        "id": len(students) + 1,
        "name": data["name"],
        "age": data["age"]
    }
    
    students.append(new_student)
    return jsonify(new_student), 201


# PUT - Update details
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    
    if not student:
        return jsonify({"error": "Student not found"})
    
    data  = request.json
    student["name"] = data.get("name", student["name"]) # Here, by using get method, we are ensuring if we are unable to get this key in the data, then we will use whatever data is present in student["name"] previously. 
    student["age"] = data.get("age", student["age"])
    
    return jsonify(student)

# Delete a record
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    student = next((s for s in students if s["id"] == student_id), None)
    
    if not student:
        return jsonify({"error" : "Student not found"})
    
    students = [s for s in students if s["id"] != student_id]
    return jsonify({"message" : "Student deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
    

