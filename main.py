"""
New-Item -ItemType file -Name subdomain.txt
paycharm terminalinde bu kodla yeni txt dosyası oluşturduk

"""

import requests

def make_requests(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_input = "google.com"

with open("subdomain.txt","r") as subdomain_list:
    for word in subdomain_list:
        word = word.strip() #boşlukları temizler
        url = "http://"+word+"."+target_input
        response = make_requests(url)
        print(response)
        if response: #if response is not none = if response
            print("found subdomain -->" + url)

