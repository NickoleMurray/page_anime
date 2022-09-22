#Contiene las vistas 
from pyexpat.errors import messages
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from main.forms import BlogForm, CreateUserForm
from .models import (
        #UserProfile,
        Blog,
        #Portfolio,
        #Testimonial,
        #Certificate
    )

# Create your views here.
#Vista de Index
class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.filter(is_active=True)
        context["blogs"] = blogs
        return context
    
#Vista de Blog
class BlogsView(generic.TemplateView):
    template_name = "main/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.filter(is_active=True)
        context["blogs"] = blogs
        return context


#Vista de Login
class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/perfil.html'
    
#class registerView(generic.TemplateView):
    #template_name = 'accounts/register.html'
    

 
#Vista de Registro 
def registerPage(request):
	if request.user.is_authenticated:
		return redirect("main:index")
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				#messages.success(request, 'Account was created for ' + user)

				return redirect('main:index')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)


#Vista de agregar blogs a la website
def BlogAddInfo(request):
    form = None
    if request.method=="POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, "main/Blogaddinfo.html",{"form":form})







        
    
    
  
