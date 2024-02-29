import requests

url = 'http://localhost:8000/hongbo/yeouijus/'

response = requests.get(url)
print(response.json())