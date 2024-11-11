from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from django_filters import rest_framework as filters
from .models import MedicationSKU
from .serializers import MedicationSKUSerializer
from .pagination import CustomPagination
from .filters import MedicationSKUFilter


class ListCreateMedicationSKUAPIView(ListCreateAPIView):
    serializer_class = MedicationSKUSerializer
    queryset = MedicationSKU.objects.all()
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MedicationSKUFilter


class RetrieveUpdateDestroyMedicationSKUAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationSKUSerializer
    queryset = MedicationSKU.objects.all()
