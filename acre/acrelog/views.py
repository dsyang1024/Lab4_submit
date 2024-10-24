from django.shortcuts import render
from .models import location, log, operation, operator, seed, fertilizer, spray
# Create your views here.
from django.http import HttpResponse
from django.http import Http404




def index(request):
    latest_fields = location.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'index.html', context)
    # return HttpResponse("Hello, world! You're at the farmnotes index, or 'home' page.")




def fields(request, location_name):
    logs = log.objects.filter(location=location_name)
    context = {'location_name':location_name, 'logs': logs}

    return render(request, 'fields.html', context)


'''
from .models import Field

#Show all the fields in my farm
def index(request):
    latest_fields = Field.objects.all()
    context = {'latest_fields': latest_fields}
    return render(request, 'farmnotes/index.html', context)
'''