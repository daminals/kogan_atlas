import requests,json

url = 'http://192.168.0.102:5000/chain'

post_data = json.dumps({'data': 'i just made the 3rd post request to the blockchain'})
headers = {"Content-Type": 'application/json', 'username': 'daniel'}

post = requests.post(url, headers=headers, data=post_data)
print(post.content, post.status_code)