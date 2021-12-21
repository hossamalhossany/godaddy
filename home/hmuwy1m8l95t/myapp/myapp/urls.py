from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('', views.index, name='index'),
    # here this issue # hossam
    path('put_data_to_databasa', views.put_data_to_databasa, name='put_data_to_databasa'),
# here this issue # hossam
    path("back_to_hossamweb", views.back_to_hossamweb, name='back_to_hossamweb')
]
