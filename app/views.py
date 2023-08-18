from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import contact

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        msg=request.POST['msg']
        mydata=contact(name=name,email=email,msg=msg)
        mydata.save()


    return render(request, 'index.html')

