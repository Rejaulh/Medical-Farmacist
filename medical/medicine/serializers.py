from rest_framework import serializers
from .models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    is_expired = serializers.ReadOnlyField()

    class Meta:
        model = Medicine
        fields = [
            'id', 'name', 'generic_name', 'manufacturer', 'expiry_date',
            'cost_price', 'selling_price', 'stock', 'batch_number',
            'is_prescription_required', 'is_expired'
        ]
