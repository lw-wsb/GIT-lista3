# Skrypt do testowania API

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

