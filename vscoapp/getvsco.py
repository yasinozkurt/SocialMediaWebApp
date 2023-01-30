import requests
from bs4 import BeautifulSoup as bs
from getuseragent import UserAgent


ua=UserAgent()


class vsco:
    raw_url="https://vsco.co/"
    div=""
    link=""
    def __init__(self,username):
        cu=ua.Random()
        h={'user-agent':cu}
        url=self.raw_url+username+"/gallery"
        page=requests.get(url,headers=h)
        soup=bs(page.text,"lxml") # lxml faster than html parse
        self.div=str((soup.find_all(class_="css-gf3foo ezmwuux1"))[0])

    def find_link(self):
        start=self.div.find("//i.vsc")
        end=self.div.find('"/><')
        self.link=self.div[start:end-26]
        print(self.link)
        return self.link