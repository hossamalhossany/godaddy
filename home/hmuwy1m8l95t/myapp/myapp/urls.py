from django.template.defaulttags import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('put_data_to_databasa', views.put_data_to_databasa, name='put_data_to_databasa'),
    path("myapp.hossamweb.com/back_to_hossamweb/", views.back_to_hossamweb, name='back_to_hossamweb'),
    # url("back_to_hossamweb", views.back_to_hossamweb),

    # path('', views.home),

    # here this issue # hossam

# # here this issue # hossam

# #     url(r'(?P<subdomain>[a-z]+)/sigin/$', 'view'),
#     url('myapp.hossamweb.com/back_to_hossamweb/', views.back_to_hossamweb),
]
