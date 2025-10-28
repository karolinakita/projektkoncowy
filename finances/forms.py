from django import forms
from .models import Transaction, Category

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'category', 'date']  # Dodajemy kategorię
        labels = {
            'amount': 'Cena',
            'description': 'Opis',
            'category': 'Kategoria',
            'date': 'Data'
        }

    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Wybierz kategorię")

    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'})
    )