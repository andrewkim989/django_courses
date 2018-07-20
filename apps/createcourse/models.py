from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):

    def add_validate(self, submitted):
        errors = {}
        a = Course.objects.filter(name = submitted['name'])
        
        if len(submitted['name']) < 5:
            errors["name"] = "Course name should be over 5 characters long"
        elif a:
            errors["name"] = "The course name already exists"
        if len(submitted['desc']) < 15:
            errors["desc"] = "Description should be over 15 characters long"
                
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 1000)
    date_added = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()

class Comment(models.Model):
    comment = models.TextField(max_length = 1000)
    date_added = models.DateTimeField(auto_now_add = True)
    #course = models.ForeignKey(Course, related_name = "comments")
