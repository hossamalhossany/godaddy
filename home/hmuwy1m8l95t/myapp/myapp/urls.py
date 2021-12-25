from django.urls import path, include, re_path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('', admin.site.urls),
    path('put_data_to_databasa', views.put_data_to_databasa, name='put_data_to_databasa'),
    path(r"^back_to_hossamweb/$", views.back_to_hossamweb, name='back_to_hossamweb'),
    # path(r'back_to_google/', views.back_to_google, name='back_to_google'),
    # url(r'(?P<subdomain>[a-z]+)/sigin/$', 'view'),
]
