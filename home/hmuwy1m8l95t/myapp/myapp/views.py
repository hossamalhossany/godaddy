from django.http import HttpResponse
from datetime import datetime
import pytz


def index(request):
    date_1 = str(datetime.now(pytz.timezone('egypt')))
    msg = "HI ya hossam this first page at first Django Project at Godday "+date_1
    return HttpResponse(msg)
    # return HttpResponse("asd asd asd")