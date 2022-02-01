from django.shortcuts import render,HttpResponseRedirect
from crud.forms import Student
from crud.models import User

def home(request):
    if request.method == 'POST':
        form = Student(request.POST)
        if form.is_valid():
            form = User(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']

            )
            form.save()
            form = Student()
    else:
        form = Student()
        
    stud = User.objects.all()
    return render(request,'home.html',{"form":form,"stud":stud})

def delete(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk = id)
        pi.delete()

        return HttpResponseRedirect('/')

def Update(request,id):
    if request.method == "POST":
        fm = Student(request.POST)
        if fm.is_valid():

            User.objects.filter(pk = id).update(
                name = fm.cleaned_data["name"],
                email = fm.cleaned_data["email"],
                password = fm.cleaned_data["password"]
            )
        fm = Student()
    else:
        fm = Student()


    return render(request,"update.html",{"id":id,"form":fm})