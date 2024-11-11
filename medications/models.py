from django.db import models
from django.db.models import UniqueConstraint

# Create your models here.
class MedicationSKU(models.Model):
    medication_name = models.CharField(max_length=100, unique=True)
    presentation = models.CharField(max_length=100)
    dose = models.IntegerField()
    unit = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['medication_name']
        constraints = [
            UniqueConstraint(
                fields=['medication_name', 'presentation', 'dose', 'unit'],
                name='unique_medication_sku_combination'
            ),
        ]