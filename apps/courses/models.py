from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "The course name should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "The course description should be at least 10 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    #represent method
    def __repr__(self):
        return f"Course: {self.name} {self.desc}"

    objects = CourseManager()