from django.shortcuts import render
from visits.models import PageVisit

def home_view(request, *args, **kwargs):
    print(request.user.is_authenticated, request.user)
    # Get all PageVisit objects from the database
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    try:
        percent = page_qs.count()/qs.count()*100
    except:
        percent = 0
    context = {
        "title":"Moom",
        "page_visit_count":page_qs.count(),
        "percent":percent,
        "total_visit_count":qs.count()
    }
    PageVisit.objects.create(path=request.path)
    return render(request,'home.html', context )


def dashbord_view(request,*args,**kwargs):
    return render(request,"dashbord.html",{})