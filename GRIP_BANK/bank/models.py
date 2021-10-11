from django.db import models

class Customer(models.Model):
    bankno = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254)
    balance = models.BigIntegerField(null=True)


'''class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Account created')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)'''
