from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view


def signup(request):
    return render(request, 'signup.html')
@api_view(['POST'])
def registration(request):
        print('request.data',request.data)
        User.objects.create_user(first_name=request.data['name'], last_name="",
                                        password=request.data['mobile'],
                                        username=request.data['name'],
                                        email=request.data['name'],
                                        is_active=True)
        obj=Registration()
        obj.name=request.data['name']
        obj.lastname=request.data['lastname']
        obj.mobile=request.data['mobile']
        obj.save()
        return render(request, 'signup.html')

@api_view(['GET'])
def searchdata(request):
    query = request.GET.get('q')
    if query:
        search = Registration.objects.filter(Q(name__contains=query)|Q(lastname__contains=query)|Q(mobile__contains=query)).values()
    else:
        search=''
    return render(request, "signup.html", {"search": search})
