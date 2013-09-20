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
def getPath(request,id):
	path.objects.filter(id=id)
	if path:
		path1=path.objects.get(id=id)
		data=path1.pathid.all()[0]
		variables = RequestContext(request, {'data' : data})
     		template='home.html'
     		return render_to_response(template, variables)
		
def getLocation(request,incr=0):
	if request.is_ajax():
		incr=request.POST.get('incr', False)
		incr=int(incr)+1
		id1=request.POST.get('id', False)
	path1=path.objects.get(id=1)
	path2=path.objects.get(id=2)
	path3=path.objects.get(id=3)
	#data=data=path1.pathid.all()
	#dic={}
	#len1=len(path1.pathid.all())
	#print len1
	lst=[]
	print incr
	if (incr < len(path1.pathid.all())):
		data=path1.pathid.all()[incr]
		dic1 = {}
		dic1['id']=data.id
		dic1['incr']=incr
		dic1['name']=data.name
		dic1['lat']=float(data.lat)
		dic1['long']=float(data.lang)
		lst.append(dic1)
	else:
		return HttpResponse("Finished")
	if (incr < len(path2.pathid.all())):
		data=path2.pathid.all()[incr]
		dic2 = {}
		dic2['id']=data.id
		dic2['incr']=incr
		dic2['name']=data.name
		dic2['lat']=float(data.lat)
		dic2['long']=float(data.lang)
		lst.append(dic2)
	if (incr < len(path3.pathid.all())):
		data=path3.pathid.all()[incr]
		dic3 = {}
		dic3['id']=data.id
		dic3['incr']=incr
		dic3['name']=data.name
		dic3['lat']=float(data.lat)
		dic3['long']=float(data.lang)
		lst.append(dic3)
	print lst
	return HttpResponse(json.dumps(lst))

#	else:
#		return HttpResponse("Finished")
		
		
	
