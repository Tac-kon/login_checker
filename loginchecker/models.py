# Create your models here.
from django.db import models
from django.utils import timezone

class Post(models.Model):
    id = models.AutoField(primary_key=True,
                          db_column='id')
    login_date = models.CharField(max_length=255,
                             default=timezone.now,
                             null=False,
                             blank=False,
                             db_column='login_date')