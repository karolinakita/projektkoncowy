from django.shortcuts import render, redirect
from .forms import TransactionForm
from .models import Transaction
from django.contrib.auth.decorators import login_required

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user  # Przypisanie transakcji do użytkownika
            transaction.save()
            return redirect('transaction_list')  # Po zapisaniu przekierowanie do listy transakcji
    else:
        form = TransactionForm()
    return render(request, 'finances/add_transaction.html', {'form': form})


def transaction_list(request):
    # Sprawdzamy, czy użytkownik jest zalogowany
    if not request.user.is_authenticated:
        return redirect('login')  # Przekierowanie do strony logowania, jeśli użytkownik nie jest zalogowany

    # Pobieramy transakcje tylko dla zalogowanego użytkownika
    transactions = Transaction.objects.filter(user=request.user)
    return render(request, 'transaction_list.html', {'transactions': transactions})

def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user)  # Tylko transakcje użytkownika
    return render(request, 'finances/transaction_list.html', {'transactions': transactions})

def home(request):
    return render(request, 'home.html')


