# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from plotmap.models import *
import json

def home(request):
	data=location.objects.get(id=1)
	variables = RequestContext(request, {'data' : data})
     	template='home.html'
     	return render_to_response(template, variables)
def getLocation(request,id):
	id1=int(id)+1
	data=location.objects.filter(id=id1)
	dic={}
	if data:
		data=location.objects.get(id=id1)
		dic['id']=data.id
		dic['name']=data.name
		dic['lat']=float(data.lat)
		dic['long']=float(data.lang)
		return HttpResponse(json.dumps(dic))
	else:
		return HttpResponse("Finished")
		
		
	
