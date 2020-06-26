from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView)
from . import models


class IndexView(TemplateView):
     template_name = 'index.html'






class SchoollistView(ListView):
    context_object_name = 'schools'
    model = models.School
    #it returns school_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name','prinicpal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','prinicpal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")































#
#
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'BASIC INJECTION!'
#         return context
#
#












# from django.http import HttpResponse
#
#
#
# class CBView(View):
#     def get(self,request):
#         return HttpResponse("CLASS BASED VIEWS ARE COOL!")
#
# # Create your views here.
# def index(request):
#     return render(request,'index.html')
