from django.urls import path
from .views import ListCreateMedicationSKUAPIView, RetrieveUpdateDestroyMedicationSKUAPIView, BulkUploadMedicationSKUAPIView

urlpatterns = [
    path('', ListCreateMedicationSKUAPIView.as_view(), name='get_post_medication'),
    path('<int:pk>/', RetrieveUpdateDestroyMedicationSKUAPIView.as_view(), name='get_delete_update_medication'),
    path('bulk-upload/', BulkUploadMedicationSKUAPIView.as_view(), name='bulk_upload_medication'),
]