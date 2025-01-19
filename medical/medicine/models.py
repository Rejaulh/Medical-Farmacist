from django.db import models
from datetime import date

# Create your models here.
class Medicine(models.Model):
    """
    Model representing a medicine in a pharmacy system.
    """
    name = models.CharField(max_length=200, unique=True)
    generic_name = models.CharField(max_length=200, blank=True, null=True)  # Optional generic name
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    expiry_date = models.DateField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  # Inventory count
    batch_number = models.CharField(max_length=100, unique=True)  # Batch tracking
    is_prescription_required = models.BooleanField(default=False)

    def is_expired(self):
        """Check if the medicine has expired."""
        return date.today() > self.expiry_date

    def __str__(self):
        return f"{self.name} (Batch: {self.batch_number})"

    class Meta:
        ordering = ['expiry_date']  # List medicines by earliest expiry date