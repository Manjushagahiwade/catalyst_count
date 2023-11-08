from django import forms

from django import forms

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Select an Excel file', required=True)


from django import forms
from .models import Company

from django import forms
from django import forms

class CompanySearchForm(forms.Form):
    company_name = forms.CharField(required=False, label="Company Name")
    company_domain = forms.CharField(required=False, label="Company Domain")
    year_founded = forms.CharField(required=False, label="Year Founded")
    industry = forms.CharField(required=False, label="Industry")
    size_range = forms.CharField(required=False, label="Size Range")
    city = forms.CharField(required=False, label="City")
    country = forms.CharField(required=False, label="Country")
    linkedin_url = forms.CharField(required=False, label="LinkedIn URL")
    current_employee_estimate = forms.CharField(required=False, label="Current Employee Estimate")
    total_employee_estimate = forms.CharField(required=False, label="Total Employee Estimate")

