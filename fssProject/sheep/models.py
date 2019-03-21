from django.db import models
from datetime import datetime
from django.utils import timezone

now = timezone.now()


class SheepReport(models.Model):
    Two = '20-30'
    Three = '30-40'
    Four = '40-50'
    Five = '50-60'
    Six = '60-70'
    Seven = '70-80'
    Eight = '80-90'
    Nine = '90-100'
    Hundred = '100-110'
    HundredOne = '110-120'
    HundredTwo = '120-130'
    HundredThree = '130-140'
    HundredFour = '140-150'
    HundredFive = '150-160'
    HundredSix = '160-170'
    HundredSeven = '170-180'
    HundredEight = '180-190'
    HundredNine = '190-200'
    TwoHundred = '200-210'
    TwoHundredOne = '210-220'
    TwoHundredTwo = '220-230'

    livestock_weight_CHOICES = (
        ('Weight', (
            (Two, '20-30'),
            (Three, '30-40'),
            (Four, '40-50'),
            (Five, '50-60'),
            (Six, '60-70'),
            (Seven, '70-80'),
            (Eight, '80-90'),
            (Nine, '90-100'),
            (Hundred, '100-110'),
            (HundredOne, '110-120'),
            (HundredTwo, '120-130'),
            (HundredThree, '130-140'),
            (HundredFour, '140-150'),
            (HundredFive, '150-160'),
            (HundredSix, '160-170'),
            (HundredSeven, '170-180'),
            (HundredEight, '180-190'),
            (HundredNine, '190-200'),
            (TwoHundred, '200-210'),
            (TwoHundredOne, '210-220'),
            (TwoHundredTwo, '220-230'),
        )
        ),
        ('Replacement Does', (
            ('Replacement Does', 'Replacement Does'),
        )
        ),
        ('Replacement Ewes', (
            ('Replacement Ewes', 'Replacement Ewes'),
        )
        ),
    )
    market_Date = models.DateField(default=datetime.now)
    sale_Type = models.CharField(max_length=20, default="Sheep/Goat")
    type_Livestock = models.CharField(max_length=30)
    head_Count = models.IntegerField(blank=True, null=True)
    livestock_weight = models.CharField(
        max_length=20, choices=livestock_weight_CHOICES, default=Two)
    high_price = models.DecimalField(max_digits=6, decimal_places=2)
    low_price = models.DecimalField(max_digits=6, decimal_places=2)
    remarks = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.sale_Type
