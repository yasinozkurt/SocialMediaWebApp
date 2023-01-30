from django.shortcuts import render
from django.shortcuts import redirect

"""
We created home.html and english version of it(home-en) with this functions we show them to users.
"""


def hometr(request):
    return render(request,"home.html")

def homeen(request):
    return render(request,"home-en.html")

def redd(request):
    return redirect('/vsco/vsco-profil-resmi-buyutme')