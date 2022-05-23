import email
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from .models import user
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():

            # nm = fm.full_clean['name']
            # em = fm.full_clean['email']
            # pwd = fm.full_clean['password']

            nm=request.POST.get('name')
            em=request.POST.get('email')
            pwd=request.POST.get('password')

            reg = user(name=nm,email=em,password=pwd)
            reg.save()
    else:
        fm = StudentRegistration()
    stud = user.objects.all()
    return render(request,'addandshow.html',{'form':fm,'stu':stud})

#this Function to update the item
def data_update(request, id):
    #fm = StudentRegistration(request.POST)
    if request.method == 'POST':
        pi = user.objects.get(id = id)
        fm = StudentRegistration(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(id = id)
        fm = StudentRegistration(instance = pi) 
       # return HttpResponseRedirect('addandshow')
    return render(request,'updatestudent.html', {'form':fm,'id':id})


# This Function to Delete
def data_delete(request, id):
    if request.method == 'POST':
        pi = user.objects.get(id = id)
        pi.delete()
        return HttpResponseRedirect('/')