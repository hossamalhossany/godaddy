from django.urls import path, include, re_path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('', admin.site.urls),
    path('put_data_to_databasa', views.put_data_to_databasa, name='put_data_to_databasa'),
   ]