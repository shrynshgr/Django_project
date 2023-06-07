from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . models import Sport

def home(request):
  template = loader.get_template('sample1.html')
  return HttpResponse(template.render({},request))

def signup(request):
  template = loader.get_template('signup.html')
  return HttpResponse(template.render({},request))

def table(request):
  template = loader.get_template('table.html')
  x=Sport.objects.all()
  c={'z':x}
  return HttpResponse(template.render(c,request))

def add(request):
  template = loader.get_template('signup.html')
  return HttpResponse(template.render({}, request))

def about(request):
  template = loader.get_template('aboutus1.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['name']
  y = request.POST['gender']
  a = request.POST['contact']
  b = request.POST['sport']
  c = request.POST['mem']
  d = request.POST['add']
  port = Sport(name=x, gender=y, contact=a, sport=b, mem=c, add=d)
  port.save()
  return HttpResponseRedirect('/home')

def delete(request, id):
  port = Sport.objects.get(id=id)
  port.delete()
  return HttpResponseRedirect("/home")

def update(request, id):
  port = Sport.objects.get(id=id)
  template = loader.get_template('updates.html')
  context = {
    'Sport': port,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  name = request.POST['name']
  gender = request.POST['gender']
  contact = request.POST['contact']
  sport = request.POST['sport']
  mem = request.POST['mem']
  add = request.POST['add']
  port = Sport.objects.get(id=id)
  port.name = name
  port.gender = gender
  port.contact = contact
  port.sport = sport
  port.mem = mem
  port.add = add
  port.save()
  return HttpResponseRedirect("/home")
