import requests

base_url = 'http://127.0.0.1:5000/students'

# Test the get students api
response = requests.get(base_url)
print("All students:", response.json())


# Test the get a particular student api
student_id = 1
response = requests.get(f"{base_url}/{student_id}")
print(f"Student with student id {student_id}:{response.json()}")

# Test the Post student api
new_student = {
    "name" : "Jaya",
    "age" : 32
}
response = requests.post(base_url, json=new_student)
print("Student added : ", response.json())


