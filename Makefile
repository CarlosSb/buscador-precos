# Variáveis para facilitar a manutenção
PYTHON := venv/bin/python
PIP := venv/bin/pip
WATCH := watchmedo auto-restart --directory="./" --pattern="*.py" --recursive --ignore-directories --ignore-patterns="*__pycache__*;*.pyc" --
install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) main.py

dev:
	$(WATCH) $(PYTHON) main.py

clean:
	rm -rf venv
	find . -type d -name "__pycache__" -exec rm -rf {} +