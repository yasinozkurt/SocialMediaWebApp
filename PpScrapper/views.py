from django.shortcuts import render
from django.http import JsonResponse
from .models import SearchedUser as su
from getuseragent import UserAgent
from datetime import datetime
from .getp import getProxy
import requests
import json
import random
import shutil
import re

# define path for media folder
MEDIA_PATH="/media/"
PROXIES={
    # we test proxies here
    }
UA=UserAgent()


def index(request):
    return render(request, 'main.html')


def indexen(request):
    return render(request,"main-en.html")


"""
We create instagram account in order to open instagram page because sometimes need to login to see page.
However with new updates, https://www.instagram.com/{USERNAME}/?__a=1 link is not working
"""
def resmi_Gonder(request):
    searched = request.GET.dict()["username"]
    currentua=UA.Random()
    with requests.Session() as s:
        USERNAME = "" # instagram account username
        PASSWORD = "" # instagram account password
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'
        time = int(datetime.now().timestamp())
        payload = {
            'username': f'{USERNAME}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{PASSWORD}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }
        r = s.get(link, headers={'user-agent':currentua})
        csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
        r = s.post(login_url, data=payload, headers={
            "user-agent": currentua,
            "x-requested-with": "XMLHttpRequest",
            "referer": "https://www.instagram.com/accounts/login/",
            "x-csrftoken": csrf
        })
        r = s.get(
            f'https://www.instagram.com/{searched}/?__a=1',proxies=PROXIES,headers={'user-agent':currentua})
    js = json.loads(r.text)
    try:
        image_file = requests.get(
            js['graphql']['user']['profile_pic_url_hd'], stream=True)
        filename = str(random.randint(0, 1000000))+".png"
        file_location = MEDIA_PATH+filename
        if su.objects.filter(username=searched).exists():
            user = su.objects.filter(username=searched).get()
            user.searched += 1
        else:
            user = su(username=searched)
        user.save()
        with open(file_location, 'wb') as file:
            shutil.copyfileobj(image_file.raw, file)
        return JsonResponse({'image_url': "/media/"+filename})
    except:
        pass