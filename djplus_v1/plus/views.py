from django.http import HttpResponse
from plus.models import Status

def my_status(request):
    status = Status.objects.all()
    count = len(status)
    text = "There are %s statuses" %(count)
    return HttpResponse(text)

