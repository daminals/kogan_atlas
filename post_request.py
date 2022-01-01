import requests,json
import base64

url = 'http://192.168.0.102:5000/chain'

#post_data = json.dumps({'data': 'post post post request'})

#creating an NFT
with open("icon/kogan-atlas.png", "rb") as NFT_data:
    #imagestr = NFT_data.read()
    imagestr = base64.b64encode(NFT_data.read())
    print(imagestr)

stringified_image = imagestr.decode('utf-8')
full_data = {'data': 'hey amongus', 'owner': 'daniel lmao', 'amongus': 'amongus'}
post_data = json.dumps({'data': full_data})
headers = {"Content-Type": 'application/json', 'username': 'daniel'}

"""
with open('test.json', 'w') as outf:
    json.dump({'data': full_data}, outf)
"""

print(post_data)

post = requests.post(url, headers=headers, data=post_data)
print(post.content, post.status_code)