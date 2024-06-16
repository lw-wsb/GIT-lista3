Dokumentacja ZAD1

## Opis
Skrypt w Pythonie do automatycznego testowania różnych endpointów API przy użyciu narzędzia curl. Skrypt wysyła żądania HTTP do wybranej publicznej API (JSONPlaceholder) i sprawdza, czy odpowiedzi są poprawne (statusy HTTP i kluczowe elementy w odpowiedziach JSON np. userId).

## Wymagania
- Python 3.x
- curl

## Instalacja
1. Upewnij się, że masz zainstalowany Python 3.x.
2. Zainstaluj curl, jeśli jeszcze go nie masz:
    ```bash
    sudo apt-get install curl
    ```

## Użycie
1. Uruchom skrypt:
    ```bash
    python test_api.py
    ```
2. Skrypt wyświetli wyniki testów w konsoli.

## Przykład
Po uruchomieniu skryptu wyniki będą wyglądać następująco:
Test 1: PASSED
Test 2: PASSED
Test 3: PASSED

Dokumentacja ZAD2
# Projekt Kalkulator

## Opis
Prosty kalkulator napisany w Pythonie z funkcjami dodawania, odejmowania, mnożenia i dzielenia. Aplikacja zawiera również testy jednostkowe.

## Wymagania
- Python 3.x
- curl

## Struktura projektu
- `calculator.py`: Główna aplikacja kalkulatora
- `test_calculator.py`: Testy jednostkowe dla aplikacji kalkulatora
- `Makefile`: Plik Makefile do automatyzacji procesów instalacji, testowania i uruchamiania aplikacji
- `requirements.txt`: Plik z listą zależności (na potrzeby przykładu może być pusty lub zawierać `unittest`)

## Makefile
Komendy:
<ol>
    <li>make install - instalacja bibliotek</li>
    <li>make test - uruchomienie testów</li>
    <li>make run - uruchamianie aplikacji</li>
</ol>


