import datetime as dt
from django.http  import HttpResponse,Http404
from .models import Category,Image
from django.shortcuts import render,redirect


# Create your views here.
def allpics(request):
    date = dt.date.today()
    image = Image.objects.all()
    return render(request, 'index.html', {"date": date,"image":image})

def moringa(request):
    date = dt.date.today()
    slypics = Image.objects.filter(Location=3)
    return render(request, 'all-pics/moringa.html', {"date": date,"slypics":slypics})

def westlands(request):
    date = dt.date.today()
    slypics = Image.objects.filter(Location=5)
    return render(request, 'all-pics/westlands.html', {"date": date,"slypics":slypics})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"slypics": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})

