from django.shortcuts import render
from .forms import contact_form
from .models import test1
from django.db import connection
from datetime import datetime
import pytz

def index(request):
    time2 = datetime.now(pytz.timezone('egypt'))
    html_page = 'myapp/index.html'
    return render(request, html_page, {'contact_form': contact_form, 'time2': time2})


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
