from rest_framework import serializers
from .models import MedicationSKU

# create class to serializer model
class MedicationSKUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSKU
        fields = ('id', 'medication_name', 'presentation',
                  'dose', 'unit', 'created_at', 'updated_at')
