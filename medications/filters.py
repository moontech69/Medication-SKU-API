from django_filters import rest_framework as filters
from .models import MedicationSKU


# We create filters for each field we want to be able to filter on
class MedicationSKUFilter(filters.FilterSet):
    medication_name = filters.CharFilter(lookup_expr='icontains')
    presentation = filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = MedicationSKU
        fields = ['medication_name', 'presentation']
    
