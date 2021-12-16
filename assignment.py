import requests
import json
response_API = requests.get('https://s3.amazonaws.com/open-to-cors/assignment.json')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
l=[]
pd=parse_json["products"]
for i in pd:
    temp=[]
    temp.append(parse_json["products"][i]["title"])
    temp.append(parse_json["products"][i]["price"])
    l.append(temp)
for i in range(len(l)):
    print(f'{l[i][0]}:{l[i][1]}')