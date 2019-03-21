from django.db import models
from datetime import date


class LivestockSummary(models.Model):
    sale_date = models.DateField()
    sale_type = models.CharField(max_length=20, default="Livestock")
    receipts = models.IntegerField()
    sale_description = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.sale_type
