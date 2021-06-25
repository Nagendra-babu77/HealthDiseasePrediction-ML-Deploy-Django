from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('cancer/',views.cancer,name='cancer'),
    path('heart/',views.heart,name='heart'),
    path('diabetes/',views.diabetes,name='diabetes'),
]
