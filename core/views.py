from django.shortcuts import render
from django.views.generic import TemplateView
import random
# Create your views here.
class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Warhammer Manager'
        return context
    
class SampleView(TemplateView):
    template_name = "core/sample.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sample Page'
        return context
    
    def get(self, request, *args, **kwargs):
        # You can add any custom logic here if needed
        return render(request, self.template_name ,self.get_context_data())
    
