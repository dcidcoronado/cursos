from django.db import models
import re

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        NAME_REGEX = re.compile(r'^[A-Z0-9][\w\s]+$')
        if postData['name']:
            if not NAME_REGEX.match(postData['name']):    
                errors['name'] = "Name must start with a capital letter!"
            elif len(postData['name']) < 5:
                errors['name'] = "The name of the show must be at least 5 characters long"
            elif Course.objects.filter(name=postData['name']) :
                errors['name'] = "Must be a new course"
        if not postData['name']:
            errors['name'] = "Must enter a Name"

        DESC_REGEX = re.compile(r'^[A-Z0-9][\w\s\-!$%^&*()_+|\'\~=`{}\[\]:";<>¡¿?,.\/]+$')
        if postData['description']: 
            if not DESC_REGEX.match(postData['description']):    
                errors['description'] = "Description must start with a capital letter!"
            if len(postData['description']) < 15:
                errors['description'] = "The description of the course must be at least 15 characters long"

        if not postData['description']:
            errors['description'] = "Must enter a Description"
        
        return errors    


class Course(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    
    objects = CourseManager()

    def __repr__(self):
        return f"{self.name}" 


