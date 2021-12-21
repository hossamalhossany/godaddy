from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('', views.index, name='index'),
    path("put_data_to_databasa", views.put_data_to_databasa, name='put_data_to_databasa'),

    path("myapp.hossamweb.com/back_to_hossamweb", views.back_to_hossamweb, name='back_to_hossamweb')
]
