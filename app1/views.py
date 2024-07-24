from django.shortcuts import render
from .models import app1
from .forms import app1form,UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    return render(request,'index.html')
#creating_list

def blog_list(request):
    blog=app1.objects.all().order_by('-created_at')
    return render (request,'blog_list.html',{'blogs':blog})

#creating_blog
@login_required
def blog_create(request):
   if request.method=="POST":
      form = app1form(request.POST, request.FILES)
      if form.is_valid():
        blog = form.save(commit=False)
        blog.user = request.user
        blog.save()
        return redirect('blog_list')

   
   else:
      form = app1form()
      return render(request,'blog_form.html',{'form':form})
   
#editing_blog
@login_required
def blog_edit(request,blog_id):
    blog=get_object_or_404(app1, pk=blog_id,user=request.user)
    if request.method=='POST':
         form=app1form(request.POST,request.FILES,instance=blog)
         if form.is_valid():
             blog=form.save(commit=False)
             blog.user=request.user
             blog.save()
             return redirect('blog_list')
             
    
    else:
      form=app1form(instance=blog)
    return render(request,'blog_form.html',{'form':form})

@login_required
def blog_dlt(request,blog_id):

   blog = get_object_or_404(app1,pk=blog_id,user=request.user)
   if request.method=='POST':
      blog.delete()
      return redirect ('blog_list')
   return render(request,'blog_delete.html',{'blog':blog})

def register(request):
   if request.method=='POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
         user=form.save(commit=False)
         user.set_password(form.cleaned_data['password1'])
         user.save()
         login(request,user)
         return redirect('blog_list')
   else:
     form=UserRegistrationForm()

   return render(request,'registration/register.html',{'form':form})



        
    
    
