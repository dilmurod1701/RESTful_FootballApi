from django.contrib.auth.models import User
from django.db import models


class Game(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    date = models.DateField()
    hour = models.CharField(max_length=90)
    venue = models.CharField(max_length=100)

    class Meta:
        db_table = 'game'

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"


class Email(models.Model):
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = 'email'

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.user.username
