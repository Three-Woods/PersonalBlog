from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
        url('register/', views.register,name='register'),

        ]
