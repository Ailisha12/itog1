import requests

res=requests.get('http://http://192.168.43.198:5000/api/main')
print(res.json())
