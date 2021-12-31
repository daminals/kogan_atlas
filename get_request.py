import requests,json
import base64

url = 'http://192.168.0.102:5000/chain'

# reading the nft

get = requests.get(url)
#print(get.content, get.status_code)

json_data = json.loads(get.content.decode('utf-8'))
NFT_data = json_data['7']['data']
print(NFT_data + '\n\n')
#NFT_data = bytes(NFT_data, encoding='utf8')
NFT_data = NFT_data.encode('utf-8')
print(base64.b64decode(NFT_data))

with open('nft.png', 'wb') as nft:
    nft.write(base64.b64decode(NFT_data))