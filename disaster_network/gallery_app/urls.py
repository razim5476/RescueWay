from django.urls import path
from . import views

urlpatterns =[
    path('gallery/',views.gallery_view,name='gallery_view'),
    path('upload_image/',views.upload_image,name='upload_image'),
]