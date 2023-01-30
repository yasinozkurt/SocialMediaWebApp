import requests
from bs4 import BeautifulSoup
from random import choice
import json
#request modülü versiyon 2.23.0 olmalı
class proxy:
    def GetProxy(self):
        url = 'https://free-proxy-list.net/'
        #yukarıdaki urlnin alternatifleri var
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return {'https': "https://"+choice(list(map(lambda x: x[0]+':'+x[1],list(zip(list(map(lambda x: x.text, soup.find_all('td')[::8])), list(map(lambda x: x.text, soup.find_all('td')[1::8])))))))}
    
    def UseProxy(self,url):
        while True:
            try:
    
                proxy = self.GetProxy()
                print(proxy)
                r = requests.get(url,proxies=proxy,timeout=4)
                if r.status_code == 200:
                    print("************")
                    print('Çalışan proxy = ',proxy)
                    break
            except:
                print('Yukarıdaki proxy denendi ancak çalışmıyor ^ ')
                pass
    
        return proxy