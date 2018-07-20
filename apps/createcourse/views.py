from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import *

def courses(request):
    all_courses = {
        "courses": Course.objects.all()
    }
    return render(request, "course.html", all_courses)

def add_process(request):
    errors = Course.objects.add_validate(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if request.method == 'POST':
        Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
    return redirect("/")

def delete(request, num):
    courseinfo = {
        "course": Course.objects.get(id = num)
    }
    return render(request, "delete.html", courseinfo)

def delete_process(request, num):
    Course.objects.get(id = num).delete()
    return redirect("/")

def add(request, num):
    courseinfo = {
        "course": Course.objects.get(id = num)
    }
    all_comments = {
        "comments": Comment.objects.all()
    }
    return render(request, "add.html", courseinfo, all_comments)

def add_comment(request):
    if request.method == 'POST':
        Comment.objects.create(comment = request.POST['comment'])

    return redirect("/")
