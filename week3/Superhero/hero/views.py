from os import terminal_size
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    
    # def get_context_data(self, **kwargs):
    #     return {
    #         'title': 'About this Class', 
    #         'body': 'Once upon a time ...',
    #     }
class wonderWomanView(TemplateView):
    template_name = 'wonderWoman.html'
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'About this Class', 
            'body': 'Once upon a time ...',
        }
 
class blackWidowView(TemplateView):
    template_name = "blackWidow.html"

class gamoraView(TemplateView):
    template_name = 'gamora.html'