import requests,json
import base64

url = 'http://192.168.0.102:5000/chain'

#post_data = json.dumps({'data': 'post post post request'})

#creating an NFT
with open("t.png", "rb") as imageFile:
    imagestr = base64.b64encode(imageFile.read())


headers = {"Content-Type": 'application/json', 'username': 'daniel'}

post = requests.post(url, headers=headers, data=post_data)
print(post.content, post.status_code)