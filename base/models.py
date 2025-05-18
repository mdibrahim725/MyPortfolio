from django.db import models

# Create your models here.

class ContactModel(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile_no=models.IntegerField()
    email_subject=models.CharField(max_length=100)
    message_box=models.CharField(max_length=800)