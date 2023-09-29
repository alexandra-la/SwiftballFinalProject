from django.shortcuts import render
from .Entry import SwiftEntry

# Create your views here.
def Home_page(request):
    context ={
        
        }
    return render(request, "Home.html", context)

def Enter_contest(request):
    context = {

    }
    context= {'form': SwiftEntry}
    return render(request, "Enter.html", context=context)

def Stats_page(request):
    context ={
         
    }
    return render(request, "Stats.html", context)

def Show_tracker(request):
    context= {

    }
    return render(request, "Tracker.html", context)

