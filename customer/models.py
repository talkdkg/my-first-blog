from django.conf import settings
from django.db import models
from django.utils import timezone


class employee(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=30)
    cparent=models.CharField(max_length=30)
    cis_featured=models.CharField(max_length=30)
    cimage=models.CharField(max_length=30)
    cis_active=models.CharField(max_length=30)
    cdescription=models.CharField(max_length=30)
    ccreated_date = models.DateTimeField(default=timezone.now)
    cpublished_date = models.DateTimeField(blank=True, null=True)

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
