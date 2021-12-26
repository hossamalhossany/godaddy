from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpRequest
from django.conf import settings
from .forms import contact_form
from .models import test1
from django.db import connection

DEFAULT_REDIRECT_URL = getattr(settings, "DEFAULT_REDIRECT_URL","http://www.hossamweb.com")

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


def back_to_hossamweb(request):
    html_page = "hossamweb.com"
    return reversed(html_page)

def back_to_google(request):
    html_page = "www.google.com"
    return redirect(html_page)
#hhh
def wildcard_redirect(request, path=None):
    new_url = DEFAULT_REDIRECT_URL
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL + "/"+path
    return HttpResponseRedirect(new_url)



