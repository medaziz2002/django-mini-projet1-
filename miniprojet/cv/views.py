from audioop import reverse
from tempfile import template
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from cv.models import Stage,Formation,Competance




def index (request):
      template =loader.get_template('index.html')
      return HttpResponse (template.render())

def info (request):
      template =loader.get_template('info.html')
      return HttpResponse (template.render())

def stage (request):
    stage = Stage.objects.all().values()
    template = loader.get_template('stage.html')
    context = { 'stage' : stage,}
    return HttpResponse (template.render(context,request))

def formation (request):
    formation = Formation.objects.all().values()
    template = loader.get_template('formation.html')
    context = { 'formation' : formation,}
    return HttpResponse (template.render(context,request))

def competance (request):
    competance = Competance.objects.all().values()
    template = loader.get_template('competance.html')
    context = { 'competance' : competance,}
    return HttpResponse (template.render(context,request))

