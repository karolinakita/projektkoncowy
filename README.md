Budget Tracker Application

Aplikacja do zarządzania wydatkami. Umożliwia użytkownikom śledzenie swoich wydatków, kategoryzowanie ich oraz generowanie miesięcznych podsumowań. Aplikacja posiada system użytkowników, dzięki czemu każdy użytkownik może zarządzać swoimi osobistymi wydatkami.

Funkcjonalności

Logowanie: Użytkownicy mogą się zarejestrować, a następnie zalogować w celu zarządzania swoimi wydatkami. Na potrzeby projektu stworzono domyślny profil:
Nazwa użytkownika: Karolina | Hasło: haslo

Zarządzanie wydatkami: Użytkownicy mogą:

Dodawać nowe wydatki.

Edytować istniejące wydatki.

Usuwać wydatki.

Kategorie: Użytkownicy mogą przypisać wydatki do różnych kategorii (np. jedzenie, transport, rozrywka, rachunki).

Wymagania

Aby uruchomić aplikację lokalnie, musisz mieć zainstalowane następujące oprogramowanie:

Python (w wersji 3.7 lub wyższej)

Django (w wersji 5.2 lub wyższej)

SQLite (baza danych używana w tej aplikacji, domyślnie dostępna w Pythonie)

Instalacja i uruchamianie aplikacji lokalnie

Klonowanie repozytorium: Aby rozpocząć, sklonuj repozytorium aplikacji na swoje lokalne urządzenie:

git clone https://github.com/TwójUsername/BudgetTracker.git


Utworzenie wirtualnego środowiska: Przejdź do katalogu aplikacji i utwórz wirtualne środowisko:

cd BudgetTracker
python -m venv .venv


Aktywacja wirtualnego środowiska: Aktywuj wirtualne środowisko:

Na systemie Windows:

.venv\Scripts\activate


Na systemie macOS/Linux:

source .venv/bin/activate


Instalacja zależności: Zainstaluj wymagane zależności:

pip install -r requirements.txt


Migracje bazy danych: Aby utworzyć bazę danych, uruchom migracje:

python manage.py migrate


Uruchomienie aplikacji: Teraz możesz uruchomić aplikację lokalnie:

python manage.py runserver


Dostęp do aplikacji: Otwórz przeglądarkę i przejdź pod adres:

http://127.0.0.1:8000/
