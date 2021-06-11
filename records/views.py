from django.shortcuts import render , redirect , HttpResponse
from django.contrib import messages
from .models import *
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def uniqueCharacters(str):

        # If at any time we encounter 2
        # same characters, return false
        for i in range(len(str)):
            for j in range(i + 1, len(str)):
                if (str[i] == str[j]):
                    return False;

        # If no duplicate characters
        # encountered, return true
        return True;

def clean():

        name = str(Emp_records.Name)
        pan = str(Emp_records.PAN_number)

        # validating the name
        if name.endswith('') or name.startswith('') :
            messages.info('Name must not contain any trailing or leading space!')


        # validating PAN
        if pan.isalpha() == "False" :
            messages.info("PAN card doesn't contain Alphanumeric char")


        if uniqueCharacters(pan) == "False":
            messages.info("PAN card is not Unique")



def index(request):
    records = Emp_records.objects.all()
    context = {"records": records}

    if request.method == 'POST':

        name = request.POST.get('Name')
        pan = request.POST.get('PAN_number')

        if name.endswith('') or name.startswith(''):
            messages.error(request,'Name must not contain any trailing or leading space!')
            #raise ValidationError("Name must not contain any trailing or leading space!")


            # validating PAN
        if pan.isalpha() == "False":
            messages.error(request,"PAN card doesn't contain Alphanumeric char")
            #raise ValidationError("PAN card doesn't contain Alphanumeric char")

        if uniqueCharacters(pan) == "False":
            messages.error(request,"PAN card is not Unique")
            #raise ValidationError("PAN card is not Unique")



        rec = Emp_records()
        rec.Name = request.POST.get('Name')
        rec.PAN_number = request.POST.get('PAN_number')
        rec.Age = request.POST.get('Age')
        rec.Gender = request.POST.get('Gender')
        rec.Email = request.POST.get('Email')
        rec.City = request.POST.get('City')
        rec.save()


        #return HttpResponse('Data Added successful!')



    return render(request, "home.html", context)

def search(request):
    query = request.GET.get('q')
    if query:
        results = Emp_records.objects.filter(Q(Name__icontains=query) | Q(PAN_number__icontains=query) | Q(Age__icontains=query) | Q(Gender__icontains=query) | Q(Email__icontains=query) | Q(City__icontains=query))
    else:
        results = Emp_records.objects.all().order_by("Name")

    return render(request, 'home.html' ,{'results':results})


def delete(request, pk):
    items = Emp_records.objects.get(id=pk)
    #if request.method == "POST":
    items.delete()
    return redirect("/")


    return render(request, 'home.html')
