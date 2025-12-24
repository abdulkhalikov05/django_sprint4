from django.urls import path
from blog import views

app_name = 'auth'

urlpatterns = [
    path('', views.register, name='register'),
]
