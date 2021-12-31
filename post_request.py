import requests,json
import base64

url = 'http://192.168.0.102:5000/chain'

#post_data = json.dumps({'data': 'post post post request'})

#creating an NFT
with open("icon/kogan-atlas.png", "rb") as NFT_data:
    #imagestr = NFT_data.read()
    imagestr = base64.b64encode(NFT_data.read())
    print(imagestr)

post_data = json.dumps({'data': imagestr.decode('utf-8')})
headers = {"Content-Type": 'application/json', 'username': 'daniel'}

post = requests.post(url, headers=headers, data=post_data)
print(post.content, post.status_code)