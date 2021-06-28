from django.shortcuts import render
import json
from . models import users
from django.http import JsonResponse
import os
import datetime
from . forms import LoginForm, fileUpload

def handle_file_form(f, file_name):
    try:
        with open(os.path.join("Files", file_name), "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return True
    except:
        return False
    



def recieveImage(request, file_extension, file_name, senderID,) -> bool:
    """
    Gets the image from the user and stores in the Files directory
    """
    try:
        todaydate = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_storage_name = str(senderID) + str(todaydate) + str(file_name)
        with open(os.path.join("Files", file_storage_name), "w") as f:
            f.write(request.content)
        return JsonResponse({"request" : True, "message" : file_storage_name})
    except Exception as e:
        return JsonResponse({"request" : False, "message" : f"There was an error with storing the photos+{e}"})


def loginDetatils(request):
    """
    Gets the login details and evaluates and
    returns an JSON Response with True or False
    """
    if request.method == "POST":
        form  = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data['username']
            password = cleaned_data['password']
            if  users.objects.filter(username = username).exists()  and users.objects.filter(password = password).exists():
                return JsonResponse({"request":True})
            return JsonResponse({"request":False})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})



def UploadFile(request):
    if request.method == 'POST':
        form = fileUpload(request.POST, request.FILES)
        if form.is_valid():
            name = request.FILES['file_upload'].name
            if handle_file_form(request.FILES['file_upload'], name):
                return JsonResponse({"request":True})
            return JsonResponse({"request":False})
            
    else:
        form = fileUpload()
    return render(request, 'uploadfile.html', {'form':form})