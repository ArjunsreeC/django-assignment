from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from . import models,forms
from django.views.generic import View,TemplateView
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from rest_framework.response import Response
from student_app.models import student

class IndexView(TemplateView):
    template_name = 'index.html'


class StudentsListView(ListView):
    model = models.student
    template_name = 'student_list.html'



class StudentsCreateView(CreateView):
    fields = ('regno','name','email')
    model = models.student
    template_name = 'student_form.html'


class StudentsUpdateView(UpdateView):
    fields = ('name','email')
    model = models.student
    template_name = 'student_form.html'


class StudentDeleteView(DeleteView):
    model = models.student
    success_url = reverse_lazy("student_app:list")
    template_name = 'student_confirm_delete.html'
