from django.shortcuts import render, redirect

from .forms import contact_form
from .models import test1
from django.db import connection


# from django.http import HttpResponse


def index(request):
    html_page = 'myapp/index.html'
    return render(request, html_page, {'contact_form': contact_form})


def put_data_to_databasa(request):
    test = test1()
    test.first_name = request.POST.get('first_name')
    test.last_name = request.POST.get('last_name')
    test.save()
    with connection.cursor() as cursor:
        sql = ''' select * from mydb2.myapp_test1 '''
        cursor.execute(sql)
        rows = cursor.fetchall()
    html_page = "myapp/index.html"
    return render(request, html_page, {'rows': rows})

# this update - wordpress - 20-12-2021
def back_to_hossamweb(request):

    html_page = "www.hossamweb.com"
    # html_page = "www.google.com"
    # html_page = "myapp/index.html"
    return redirect(html_page)
#
# def home(request):
#     return redirect("www.hossamweb.com")