from django.db import models

# Create your models here.

class Message(models.Model):
  sender_name = models.CharField(max_length=150)
  sender_email = models.CharField(max_length=150)
  subject = models.CharField(max_length=150)
  text_body = models.TextField(blank = False)

  def __str__(self):
      return f'{self.subject.capitalize()}, from: , {self.sender_name.capitalize()}'

class Project(models.Model):
  title = models.CharField(max_length=150)
  skills = models.CharField(max_length=150)
  images = models.TextField(blank=False)
  description = models.TextField(blank = False)


  def __str__(self):
    return f'{self.title}'



