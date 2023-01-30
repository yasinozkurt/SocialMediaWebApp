from django.http.response import JsonResponse
from django.shortcuts import render
from .getvsco import vsco
from .models import SearchedUser as su

def vscomain(request):
        return render(request,"vsco.html")

def vscomainen(request):
        return render(request,"vsco-en.html")

def send_pic(request):
    try:
            username=request.GET.dict()["username"]
            user=vsco(username)
            link=user.find_link()
            if su.objects.filter(username=username).exists():
                user = su.objects.filter(username=username).get()
                user.searched += 1
            else:
                user = su(username=username)
            user.save()
            return JsonResponse({'vscolink':link})
    except:
            link="https://cdn.freelogovectors.net/wp-content/uploads/2012/04/warning.png"
            return JsonResponse({'vscolink':link})
