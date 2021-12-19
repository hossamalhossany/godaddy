# from django.http import HttpResponse
from datetime import datetime
# import pytz
from django.shortcuts import render
from .forms import contact_form
from .models import test1
from django.db import connection


def index(request):
    # date_1 = str(datetime.now(pytz.timezone('egypt')))
    # msg = "HI ya hossam this first page at first Django Project at Godday "+date_1
    html_page = 'myapp/index.html'
    return render(request, html_page, {'contact_form': contact_form})
    # return HttpResponse("asd asd asd")


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
