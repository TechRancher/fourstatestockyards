from django.db import models
from datetime import datetime
from django.utils import timezone

now = timezone.now()


class LivestockReport(models.Model):
    One = '100-200'
    Two = '200-300'
    Three = '300-400'
    Four = '400-500'
    Five = '500-600'
    Six = '600-700'
    Seven = '700-800'
    Eight = '800-900'
    Nine = '900-1000'
    Thousand = '1000-1100'
    ThousandOne = '1100-1200'
    ThousandTwo = '1200-1300'
    ThousandThree = '1300-1400'
    ThousandFour = '1400-1500'
    ThousandFive = '1500-1600'
    ThousandSix = '1600-1700'
    ThousandSeven = '1700-1800'
    ThousandEight = '1800-1900'
    ThousandNine = '1900-2000'
    TwoThousand = '2000-2100'
    TwoThousandOne = '2100-2200'
    TwoThousandTwo = '2200-2300'
    TwoThousandThree = '2300-2400'
    TwoThousandFour = '2400-2500'
    TwoThousandFiveToFiveThousand = '2500-5000'
    livestock_weight_CHOICES = (
        ('Weight', (
            (One, '100-200'),
            (Two, '200-300'),
            (Three, '300-400'),
            (Four, '400-500'),
            (Five, '500-600'),
            (Six, '600-700'),
            (Seven, '700-800'),
            (Eight, '800-900'),
            (Nine, '900-1000'),
            (Thousand, '1000-1100'),
            (ThousandOne, '1100-1200'),
            (ThousandTwo, '1200-1300'),
            (ThousandThree, '1300-1400'),
            (ThousandFour, '1400-1500'),
            (ThousandFive, '1500-1600'),
            (ThousandSix, '1600-1700'),
            (ThousandSeven, '1700-1800'),
            (ThousandEight, '1800-1900'),
            (ThousandNine, '1900-2000'),
            (TwoThousand, '2000-2100'),
            (TwoThousandOne, '2100-2200'),
            (TwoThousandTwo, '2200-2300'),
            (TwoThousandThree, '2300-2400'),
            (TwoThousandFour, '2400-2500'),
            (TwoThousandFiveToFiveThousand, '2500-5000'),
        )
        ),
        ('Age', (
                ('Young', 'Young'),
                ('Older', 'Older'),
        )
        ),
        ('Bottle Calves', (
            ('Bottle Calves', 'Bottle Calves'),
        )
        ),
        ('Pairs', (
            ('Pairs', 'Pairs'),
        )
        ),
    )
    market_Date = models.DateField(default=datetime.now)
    sale_Type = models.CharField(max_length=20, default='Livestock')
    type_Livestock = models.CharField(max_length=30)
    head_Count = models.IntegerField(blank=True, null=True)
    livestock_weight = models.CharField(
        max_length=20, choices=livestock_weight_CHOICES, default=One)
    high_price = models.DecimalField(max_digits=6, decimal_places=2)
    low_price = models.DecimalField(max_digits=6, decimal_places=2)
    remarks = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.sale_Type
