from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def add(request):
    print ('in add function')
    template = loader.get_template('simplemath/add.html')
    sum = None
    if request.method == 'POST' :
        sum = int(request.POST['firstInt']) + int(request.POST['secondInt'])
    context = {
        'result' : sum
    }
    return HttpResponse(template.render(context,request))
