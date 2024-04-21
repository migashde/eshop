from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=200)