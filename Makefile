PYTHON=python3
PIP=pip3

all: install test run

install:
	$(PIP) install -r requirements.txt

test:
	py -m unittest discover

run:
	py kalkulator.py
