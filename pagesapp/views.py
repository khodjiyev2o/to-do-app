from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post
# Create your views here.
class UyPageView(ListView):
        model = Post
        template_name = 'home.html'
class HomePageView(TemplateView):
        template_name='home.html'

class AboutPageView(TemplateView):
        template_name = 'about.html'