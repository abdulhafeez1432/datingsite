from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Who(models.Model):
    name = models.CharField("Who Issue", max_length=50)

    def __str__(self):
        return f'{self.name }'

    class Meta:
        verbose_name = 'Who'
        verbose_name_plural = 'Who'

class Term(models.Model):
    name = models.CharField("Term Name", max_length=500)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Term'
        verbose_name_plural = 'Terms'

class User(AbstractUser):
    is_male = models.BooleanField(default=False)
    is_female = models.BooleanField(default=False)
    phone = models.CharField("Phone Number", max_length=50)
    who = models.ForeignKey(Who, related_name='who', on_delete=models.CASCADE, null=True, blank=True)
    term = models.ManyToManyField(Term, related_name='term+', null=True, blank=True)



class Plan(models.Model):

    PLAN_FREE_TIER_ID       = 1
    PLAN_FREE_DURATION_DAYS = 15
    name              = models.CharField(max_length=255)
    description       = models.CharField(max_length=255, null=True, blank=True)
    duration_days     = models.IntegerField(default=PLAN_FREE_DURATION_DAYS)
    price         = models.DecimalField(max_digits=10, decimal_places=2)
    created_at        = models.DateTimeField(auto_now_add=True)
    last_updated_on   = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=50, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    disable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    payment  = models.BooleanField(default=False)    
    end_time = models.DateTimeField()
    last_updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username


""" class IntroQuestion(models.Model):
    user = models.OneToOneField(User, related_name='intro', on_delete=models.CASCADE)
    phone = models.CharField("Phine Number", max_length=50)
    who = models.ForeignKey(Who, related_name='who', on_delete=models.CASCADE)
    term = models.ManyToManyField(Term, related_name='term')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.name} - {self.phone}'
     """




