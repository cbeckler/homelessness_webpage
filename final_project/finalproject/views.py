from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, FormView
from .forms import SearchForm
import google.generativeai as genai
from .secrets import GOOGLE_API_KEY


def show_population(request):

    pop_data = HomelessCities.objects.all()

    return render(request, 'templates/population.html', {'pop_data':pop_data})


def show_homeless(request):

    homeless_data = HomelessCities.objects.all()

    return render(request, 'templates/homeless.html', {'homeless_data':homeless_data})

def show_proportion(request):

    proportion_data = HomelessCities.objects.all()

    return render(request, 'templates/proportion.html', {'proportion_data':proportion_data})


class HomePageView(TemplateView):
    
    template_name = 'home.html'


class SearchView(FormView):
    
    template_name = 'search.html'
    
    form_class = SearchForm

    success_url = '/chat'

    def form_valid(self, form):

        variable = form.cleaned_data['text']

        genai.configure(api_key=GOOGLE_API_KEY)

        model = genai.GenerativeModel('gemini-2.0-flash')

        response = model.generate_content(variable)

        edited_response = response.text
        edited_response = edited_response.replace("**", "")

        context = self.get_context_data(output=edited_response)
        
        return self.render_to_response(context)




