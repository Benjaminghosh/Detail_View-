from django.shortcuts import render,HttpResponse
from django.views.generic import *
from app.models import *
from django.urls import reverse_lazy
# Create your views here.

class InsertSchool(CreateView):
    model = School
    fields = "__all__"
    success_url = reverse_lazy('index')

class School_list(ListView):
    model = School
    fields = '__all__'
    context_object_name = 'schools'

class School_detail(DetailView):
    model = School
    context_object_name = 'schools'


def ghosh(request):
    return HttpResponse('Insertion of Student Is successfull')


def index(request):
    return HttpResponse('Insertion of School Is Successfull')

def wish_someone(request, name):
    return HttpResponse(f"<h1> Hello {name} </h1>" )

def obj(request,sname):
    obje = School.objects.get(sname=sname)
    d={'obje':obje}
    return render(request,'app/obj.html',d)