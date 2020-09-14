from django.urls import path

from .views import BaseView

app_name = 'notebook'
urlpatterns = [
    path('', BaseView, name='home-view'),
    
]
