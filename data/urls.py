from django.urls import path

from . import views

urlpatterns = [
    path('getlogindetails/', view = views.loginDetatils),
    path('sendimage/<str:file_extension>/<str:file_name>/<str:senderID>/', view = views.recieveImage),
    path('home/', view = views.UploadFile)
]