from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model):

    class Meta:
        db_table = "questions"
        
    question_text  =  models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
    	#return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now


class Choice(models.Model):

    class Meta:
        db_table = "choices"

    question =  models.ForeignKey(Question,on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes  = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text



class Signup(models.Model):

    class Meta:
        db_table = "userandpass"

    username = models.CharField(max_length = 100)
    password = models.CharField(max_length=50)

    def __str__(sef):
        return self.username


class Comments(models.Model):
    
    class Meta:
        db_table = "Comments"
    
    author = models.CharField(max_length = 100)
    msg = models.CharField(max_length = 500)

    def __str__(self):
        return self.msg