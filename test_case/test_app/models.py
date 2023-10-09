from django.db import models


class Currency(models.Model):
    char_code = models.CharField(max_length=3)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.char_code


class Exchange(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=15, decimal_places=3)

    class Meta:
        unique_together = ['currency', 'date']

    def __str__(self):
        return f'{self.currency}: {self.value}'

