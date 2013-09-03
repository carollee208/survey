from django.db import models

# Create your models here.

class Question(models.Model):
    user_question = models.CharField(max_length=200)
    user_date = models.DateTimeField('date entered')
    
    def _unicode_(self):
        return self.user_question

class Response(models.Model):
    question = models.ForeignKey(Question)
    user_response = models.CharField(max_length=200)
    
    def _unicode_(self):
        return self.user_response

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.IntegerField(max_length=50)
    # date = models.DateTimeField()

    def _unicode_(self):
        return self.first_name
