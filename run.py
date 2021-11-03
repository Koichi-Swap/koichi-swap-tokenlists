import json
import os
import requests


dels = ['originAddress', 'originName', 'originSymbol', 'originLogoURI', 'originDecimals']

d = json.load(open("./conflux.tokenlist.json", 'r'))
for token in d['tokens']:
    address: str = token['address']
    path = os.path.join('logos', address.replace(':', '-'))
    img_path = os.path.join(path, 'logo.png')
    #url = token['logoURI']
    #r = requests.get(url, allow_redirects=True)
    #open(img_path, 'wb').write(r.content)
    #os.makedirs(os.path.join('logos', address.replace(':', '-')), exist_ok=True)
    #url = 'https://raw.githubusercontent.com/Koichi-Swap/koichi-swap-tokenlists/main/logos/{}/logo.png'.format(address.replace(':', '-'))
    #print(url)
    #token['logoURI'] = url
    #print(json.dumps(token), ',')
    url = 'https://confluxscan.io/stat/tokens/by-address?address={}'.format(address)
    r = requests.get(url, allow_redirects=True).json()
    token['name'] = r['name']
    token['symbol'] = r['symbol']
    print(json.dumps(token), ',')
    """
    if 'iconUrl' in r and r['iconUrl'] is not None and 'png' in r['iconUrl']:
        print(r['iconUrl'])
        r = requests.get(r['iconUrl'], allow_redirects=True)
        open(img_path, 'wb').write(r.content)
    """