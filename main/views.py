from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from .models import Task

class UserLogin(LoginView):
    fields = '__all__'
    template_name = 'main/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class UserLogout(LogoutView):
    next_page = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        request.session.flush()
        return redirect(self.next_page)

class UserRegister(FormView):
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

            subject = 'Welcome to My To-Do'
            message = f'Hi {user.username}, You have successfully created an account!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.username,]
            send_mail(subject, message, email_from, recipient_list)
        return super(UserRegister, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(UserRegister, self).get(*args, **kwargs)
    
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'main/tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-here') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'details'
    template_name = 'main/details.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    context_object_name = 'create'
    template_name = 'main/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    context_object_name = 'update'
    template_name = 'main/update.html'

class TaskDelete(LoginRequiredMixin, DeleteView):
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