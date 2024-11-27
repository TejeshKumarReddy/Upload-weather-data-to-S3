import requests
import os
import json
import boto3
import datetime
city = input('enter city: ')
API_key = input('enter api key')
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+ city +'&appid='+ API_Key)
print(response.json())
with open('fil','w') as file:
    json.dump(response.json(), file)

s3 = boto3.client('s3')
try:
        result = s3.upload_file("fil", "web-tkr", "fil"+"-"+ city + str(datetime.datetime.now()))
        print(result)
except Exception as e:
        print(e)
