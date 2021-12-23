import requests 
for i in range(10000):
    path = str(i).zfill(4)
    url = 'https://www.larvalabs.com/public/images/cryptopunks/punk' + path + '.png'
    r = requests.get(url)
    with open(path+'.png','wb') as f:
        f.write(r.content)
    

