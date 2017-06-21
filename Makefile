#!/usr/bin/make

VENV ?= $(PWD)/venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

default: install

install:
	virtualenv --python=python $(VENV)
	$(PYTHON) setup.py build
	$(PYTHON) setup.py install


clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	rm -rf $(VENV) dist pinboard_pdf.egg-info

.PHONY: install
