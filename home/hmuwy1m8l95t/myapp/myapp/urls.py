from django.urls import path
from . import views

urlpatterns = [
    path('myapp/', views.index, name='index'),
    path("myapp/put_data_to_databasa", views.put_data_to_databasa, name='put_data_to_databasa')
]
