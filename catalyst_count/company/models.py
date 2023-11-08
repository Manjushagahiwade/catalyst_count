from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.CharField(max_length=256, null=True, blank=True)
    company_name = models.CharField(max_length=256, null=True, blank=True)
    company_domain = models.CharField(max_length=256, null=True, blank=True)
    year_founded = models.CharField(max_length=256, null=True, blank=True)
    industry = models.CharField(max_length=256, null=True, blank=True)
    size_range = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    country = models.CharField(max_length=256, null=True, blank=True)
    linkedin_url = models.CharField(max_length=256, null=True, blank=True)
    current_employee_estimate = models.CharField(max_length=256, null=True, blank=True)
    total_employee_estimate = models.CharField(max_length=256, null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)