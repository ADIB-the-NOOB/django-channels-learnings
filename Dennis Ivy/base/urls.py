from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('messages/', views.MessageView.as_view(), name='messages'),
]