from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Company
from .forms import ExcelUploadForm
import pandas as pd
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Company
import pandas as pd

def process_uploaded_file(file):
    data = pd.read_excel(file)

    companies_to_create = []
    for index, row in data.iterrows():
        company_data = {
            'company_id': row.get('company_id'),
            'company_name': row.get('company_name'),
            'company_domain': row.get('company_domain'),
            'year_founded': row.get('year_founded'),
            'industry': row.get('industry'),
            'size_range': row.get('size_range'),
            'city': row.get('city'),
            'country': row.get('country'),
            'linkedin_url': row.get('linkedin_url'),
            'current_employee_estimate': row.get('current_employee_estimate'),
            'total_employee_estimate': row.get('total_employee_estimate')
        }
        companies_to_create.append(Company(**company_data))

    Company.objects.bulk_create(companies_to_create)

def upload_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES.get('excel_file')

        if excel_file and not excel_file.name.endswith(('.xlsx', '.xls')):
            raise ValidationError("Invalid file format. Please upload a .xlsx or .xls file.")

        if excel_file:
            process_uploaded_file(excel_file)
            return redirect('success')

    return render(request, 'upload_excel.html')

def success(request):
    return render(request, 'success.html')


# from django.shortcuts import render, redirect
# from .models import Company
# import pandas as pd
# from django.core.exceptions import ValidationError
#
#
# def upload_excel(request):
#     if request.method == 'POST':
#         excel_file = request.FILES.get('excel_file')
#
#         # Check file extension to allow only .xlsx and .xls files
#         if excel_file and not excel_file.name.endswith(('.xlsx', '.xls')):
#             raise ValidationError("Invalid file format. Please upload a .xlsx or .xls file.")
#
#         if excel_file:
#             data = pd.read_excel(excel_file)
#
#             for index, row in data.iterrows():
#                 Company.objects.create(
#                     company_id=row['company_id'],
#                     company_name=row['company_name'],
#                     company_domain=row['company_domain'],
#                     year_founded=row['year_founded'],
#                     industry=row['industry'],
#                     size_range=row['size_range'],
#                     city=row['city'],
#                     country=row['country'],
#                     linkedin_url=row['linkedin_url'],
#                     current_employee_estimate=row['current_employee_estimate'],
#                     total_employee_estimate=row['total_employee_estimate']
#                 )
#
#             return redirect('success')  # Redirect to a success page after successful upload
#
#     return render(request, 'upload_excel.html')
#
#
# def success(request):
#     return render(request, 'success.html')
#

from django.shortcuts import render
from .models import Company
from .forms import CompanySearchForm

def search(request):
    form = CompanySearchForm(request.GET)
    results = Company.objects.all()

    if request.method == 'GET' and form.is_valid():
        filters = {}

        for field_name, field in form.fields.items():
            query = form.cleaned_data[field_name]
            if query:
                filters[f"{field_name}__icontains"] = query

        results = results.filter(**filters)

    search_count = results.count()

    return render(request, 'search_results.html', {'form': form, 'results': results, 'search_count': search_count})
