import requests
import json


# a get request to get the resource. 
response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

#print(response.json())
for questions in response.json()['items']:
    if questions['answer_count'] == 0:
        print(questions['title'])
        print(questions['link'])
    else:
        print("Skipped")