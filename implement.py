##This .py is no longer applicable to this project
import base64
import json
import requests

url = "https://csciteam4bds.com/"
user = "csciteam"
password = "C5c!T3amF0ur"
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8')}
post = {
 'title'    : 'test123',
 'status'   : 'publish',
 'content'  : 'This is my first post created using rest API',
 'categories': 5,
 'date'   : '2020-01-05T10:00:00'
     }
response = requests.post(url, headers=header, json=post)
print(response)
