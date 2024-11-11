from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.db.utils import IntegrityError
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

class BulkUploadMedicationSKUAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        # print('request-data: ', data)
        serializers = [MedicationSKUSerializer(data=item) for item in data]
        # print('serializers: ', serializers)
        if all(serializer.is_valid() for serializer in serializers):
            try:
                with transaction.atomic():
                    movie_objects = [MedicationSKU(**serializer.validated_data) for serializer in serializers]
                    created_movies = MedicationSKU.objects.bulk_create(movie_objects)
                return Response(MedicationSKUSerializer(created_movies, many=True).data, status=status.HTTP_201_CREATED)
            
            except IntegrityError:
                return Response({"error": "Unique constraint violation"}, status=status.HTTP_400_BAD_REQUEST)
        errors = [serializer.errors for serializer in serializers if not serializer.is_valid()]
        return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
    