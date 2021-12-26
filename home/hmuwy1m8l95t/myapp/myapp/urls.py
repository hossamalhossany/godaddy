from django.urls import path, include, re_path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('', admin.site.urls),
    path('back_to_google', views.back_to_google),
    path('put_data_to_databasa', views.put_data_to_databasa, name='put_data_to_databasa'),
    # path('<myapp.hossamweb.com>/back_to_hossamweb/', views.put_data_to_databasa, name='back_to_hossamweb'),
    path('back_to_hossamweb/', views.put_data_to_databasa, name='back_to_hossamweb'),
   ]


