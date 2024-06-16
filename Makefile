# Definicje zmiennych
PYTHON=python3
PIP=pip3

# Domyślna reguła, która jest uruchamiana, gdy nie podano żadnej reguły
all: install test run

# Reguła instalująca zależności
install:
	$(PIP) install -r requirements.txt

# Reguła uruchamiająca testy jednostkowe
test:
	py -m unittest discover

# Reguła uruchamiająca aplikację
run:
	py kalkulator.py
