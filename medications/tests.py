from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import MedicationSKU


"""
  Model Tests
"""


class MedicationSKUModelTest(TestCase):
    def setUp(self):
        MedicationSKU.objects.create(
            medication_name="Amoxicillin",
            presentation="Capsule",
            dose=500,
            unit="mg"
        )

    def test_MedicationSKU_creation(self):
        sku = MedicationSKU.objects.get(medication_name="Amoxicillin")
        self.assertEqual(sku.presentation, "Capsule")
        self.assertEqual(sku.dose, 500)
        self.assertEqual(sku.unit, "mg")

    def test_unique_constraints(self):
        with self.assertRaises(Exception):
            MedicationSKU.objects.create(
                medication_name="Amoxicillin",
                presentation="Capsule",
                dose=500,
                unit="mg"
            )

    def test_unique_title(self):
        with self.assertRaises(Exception):
            MedicationSKU.objects.create(
                medication_name="Amoxicillin",
                presentation="Tablet",
                dose=200,
                unit="IU"
            )


"""
  API Endpoint Tests
"""


class MedicationSKUAPITest(APITestCase):
    def setUp(self):
        self.MedicationSKU_data = {
            "medication_name": "Amoxicillin",
            "presentation": "Capsule",
            "dose": 500,
            "unit": "mg"
        }
        self.MedicationSKU = MedicationSKU.objects.create(
            **self.MedicationSKU_data)
        self.url = reverse("get_delete_update_medication",
                           args=[self.MedicationSKU.id])

    def test_create_MedicationSKU(self):
        data = {
            "medication_name": "Insulin",
            "presentation": "Injection",
            "dose": 100,
            "unit": "IU"
        }
        response = self.client.post(
            reverse("get_post_medication"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["medication_name"], "Insulin")

    def test_read_MedicationSKU(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["medication_name"], "Amoxicillin")

    def test_update_MedicationSKU(self):
        new_data = {
            "medication_name": "Insulin",
            "presentation": "Injection",
            "dose": 100,
            "unit": "IU"
        }
        response = self.client.patch(self.url, data=new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["medication_name"], "Insulin")
        self.assertEqual(response.data["presentation"], "Injection")
        self.assertEqual(response.data["dose"], 100)
        self.assertEqual(response.data["unit"], "IU")

    def test_delete_MedicationSKU(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class MedicationSKUBulkUploadTest(APITestCase):
    def setUp(self):
        self.bulk_upload_url = reverse("bulk_upload_medication")
        self.bulk_data = [
            {
                "medication_name": "Amoxicillin",
                "presentation": "Capsule",
                "dose": 500,
                "unit": "mg"
            },
            {
                "medication_name": "Ibuprofen",
                "presentation": "Tablet",
                "dose": 200,
                "unit": "mg"
            },
            {
                "medication_name": "Paracetamol",
                "presentation": "Tablet",
                "dose": 500,
                "unit": "mg"
            },
        ]

    def test_bulk_upload_success(self):
        response = self.client.post(
            self.bulk_upload_url, data=self.bulk_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 3)

    def test_bulk_upload_duplicate(self):
        # Adding a duplicate to test uniqueness constraint
        self.bulk_data.append({
            "medication_name": "Paracetamol",
            "presentation": "Tablet",
            "dose": 500,
            "unit": "mg"
        })
        response = self.client.post(
            self.bulk_upload_url, data=self.bulk_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Unique constraint violation", response.data["error"])


"""
  Edge Case Tests
"""


class MedicationSKUEdgeCaseTest(APITestCase):
    def setUp(self):
        self.invalid_MedicationSKU_data = {
            "medication_name": "Amoxicillin",
            "presentation": "Capsule",
            "dose": 500,
            # Missing unit field
        }

    def test_missing_fields(self):
        response = self.client.post(
            reverse("get_post_medication"), data=self.invalid_MedicationSKU_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("unit", response.data)

    def test_invalid_dose_type(self):
        invalid_data = {
            "medication_name": "Amoxicillin",
            "presentation": "Capsule",
            "dose": "300~400", # Invalid dose type
            "unit": "mg"
        }
        response = self.client.post(
            reverse("get_post_medication"), data=invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("dose", response.data)
