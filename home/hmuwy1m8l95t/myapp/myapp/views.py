# from django.http import HttpResponse
from datetime import datetime
# import pytz
from django.shortcuts import render
from .forms import contact_form


def index(request):
    # date_1 = str(datetime.now(pytz.timezone('egypt')))
    # msg = "HI ya hossam this first page at first Django Project at Godday "+date_1
    html_page = 'myapp/index.html'
    return render(request, html_page, {'contact_form': contact_form})
    # return HttpResponse("asd asd asd")