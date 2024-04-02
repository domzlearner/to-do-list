from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

# import requests 
# from bs4 import BeautifulSoup

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'main/tasks.html'

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'details'
    template_name = 'main/details.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    context_object_name = 'create'
    template_name = 'main/create.html'
    
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    context_object_name = 'update'
    template_name = 'main/update.html'

class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    context_object_name = 'delete'
    template_name = 'main/delete.html'

""" def home(request):
    city = "Santa Rosa"
    
    # url and requests 
    url = "https://www.google.com/search?q=" + "weather" + city 
    html = requests.get(url).content 
    
    # getting raw data 
    soup = BeautifulSoup(html, 'html.parser') 
    temperature = soup.find('div', 
                            attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text 
    time_sky = soup.find('div',  
                        attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text 
    
    # formatting data 
    sky = time_sky.split('\n')[1]

    data = {
        "sky": str(sky),
        "temp": str(temperature),
        "city": str(city)
    }
    
    print(data)

    return render(request, 'main/home.html', data)
 """