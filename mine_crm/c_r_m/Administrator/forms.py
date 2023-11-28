
# forms.py
from django import forms
from import_export.forms import ImportForm, ExportForm

from .models import CustomerLeads
from import_export.formats.base_formats import XLSX, CSV

class CustomerLeadsImportForm(ImportForm):
    import_formats = [XLSX, CSV]

    class Meta:
        model = CustomerLeads

class CustomerLeadsExportForm(ExportForm):
    formats = [XLSX, CSV]
    class Meta:
        model = CustomerLeads
