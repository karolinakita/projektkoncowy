from django.db import models
from django.contrib.auth.models import User

# Model dla kategorii
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model dla transakcji
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Łączymy transakcje z użytkownikiem
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Relacja z modelem Category
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Kwota transakcji
    description = models.TextField()  # Opis transakcji
    date = models.DateTimeField()  # Data dodania transakcji

    def __str__(self):
        return f'{self.category} - {self.amount} ({self.date.strftime("%Y-%m-%d")})'
