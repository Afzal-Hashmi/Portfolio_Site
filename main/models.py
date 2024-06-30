from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    aboutme = models.CharField(max_length=500)

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class skill_list(models.Model):
    skill = models.CharField(max_length=100)

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)


    def __str__(self):
        return self.name
