from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from .models import DetailsModel
from .forms import DetailForm
# Create your views here.
def fv_crud(request):
    return HttpResponse("hello")

class DetailListview(ListView):
    model = DetailsModel
    template_name = 'index.html'
    context_object_name = 'Details_List'

class FormView(CreateView):
    model = DetailsModel
    form_class = DetailForm
    template_name = 'form.html'
    success_url ='/'

