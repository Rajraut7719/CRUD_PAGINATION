from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import StudentRegistration
from django.contrib import messages
from .models import User
from django.core.paginator import Paginator
# Create your views here.


def message(request):
    return render(request,'app/message.html')


def addandshow(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Data successfully Submitted')
            fm=StudentRegistration()
            return redirect('/message/')

    else:
        fm=StudentRegistration()
        stud=User.objects.all()
        paginator=Paginator(stud,5)
        page_number=request.GET.get('page')
        ServiceDatafinal=paginator.get_page(page_number)
           
    return render(request,'app/addandshow.html',{'form':fm,'stu':stud, 'ServiceDatafinal':ServiceDatafinal})


def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'app/update.html',{'form':fm})

def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        messages.success(request, 'Delete Data')
        return HttpResponseRedirect('/')

