from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('myapp/', views.index, name='index'),
    path("myapp/put_data_to_databasa", views.put_data_to_databasa, name='put_data_to_databasa'),

    path("myapp/back_to_hossamweb/", views.back_to_hossamweb, name='back_to_hossamweb')
]
