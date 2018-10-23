from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.

#<<--------COURSE HOME HTML-------->>
def index(request):
    print("\n<<---------------INDEX HTML--------------->>\n")
    
    course = Course.objects.all()

    context = {
        'course': course
    }
    
    return render(request,'courses/index.html', context)

#<<--------ADD COURSE POST-------->>
def process(request):
    print("\n<<---------------PROCESSING COURSE FORM--------------->>\n")
    response = "You have reached the process page!"

    print("PRINTING COURSE FORM: ", request.POST)

    errors = Course.objects.basic_validator(request.POST)

    if len(errors):
        # if the errors object contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        course = Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])

        return redirect('/')

#<<--------REMOVAL HTML-------->>
def remove(request, number):
    print("\n<<---------------REMOVE COURSE FORM--------------->>\n")
    course = Course.objects.get(id=number)

    #CONTEXT
    context = {
        'course': course
    }

    return render(request,'courses/remove.html', context)

#<<--------REMOVAL POST-------->>
def confirm_remove(request):
    print("\n<<---------------PROCESSING COURSE REMOVAL--------------->>\n")
    print("PRINTING COURSE REMOVAL FORM: ",request.POST['course_id'])

    course = Course.objects.get(id=request.POST['course_id'])

    course.delete()

    return redirect('/')
    