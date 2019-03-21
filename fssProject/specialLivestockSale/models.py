from django.db import models
from datetime import datetime


class SpecialLivestockSale(models.Model):
    post_date = models.DateField(default=datetime.now, blank=True)
    sale_date = models.DateField()
    sale_type = models.CharField(max_length=50, default="Special Cow Sale")
    sale_description = models.TextField()
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.sale_type
