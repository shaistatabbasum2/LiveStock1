# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from app.models import Category
from django.utils import timezone
import datetime

# Create your views For Student.
def insert(request):
    context = {'success': False}
    if request.method == "POST":
        # HANDLE THE FORM
          name = request.POST['name']
          if request.POST.get('name')=="":
              return render(request,'insert.html', {'error': True})    
          description = request.POST['description']
          if request.POST.get('description')=="":
              return render(request,'insert.html', {'error1': True})                    
          currentupdate = datetime.datetime.now() 
          print(name)
          ins=Category(name=name, description=description, created_on=currentupdate)
          ins.save()
          context = {'success': True}  
    return render(request,'insert.html', context)
def show(request):
    allTasks = Category.objects.all()
    context = {'tasks': allTasks}
    return render(request,'list.html', context)
#This Function Will Edit/Update in Student
def delete(request,category_id):
    delete = Category.objects.get(category_id=category_id)
    delete.delete()
    return redirect('/show')
 #This Function Will Edit/Update in Student
def edit(request , category_id):
    print("come here")
    cat = Category.objects.get(category_id=category_id)
    return render(request, 'update.html',{'cat':cat})
def updated(request, category_id):
    if request.method == 'POST':
        category_id = request.POST['category_id']
        name = request.POST['name']
        if request.POST.get('name')=="":
            return render(request, 'update.html',{'error':True})
        description = request.POST['description']
        if request.POST.get('description')=="":
              return render(request,'insert.html', {'error1': True})  
        updated_on = datetime.datetime.now() 
        updated_on = Category(updated_on = updated_on)
        
    else:  
            edit = Category.objects.get(category_id = category_id)      
            edit.name = name 
            edit.description = description           
            edit.save()
            return redirect(reverse('show'))
          