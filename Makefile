.PHONY: default test build docs/build/html

default: .venv/lib/site-packages build docs/build/html

build: docs/build/html/.git lib/site-packages

ifeq ($(OS), Windows_NT)
PYTHON27?=C:\Python27\python.exe
NUKE_PYTHON?=C:/Program Files/Nuke10.5v7/python.exe
# abspath not work on windows
PYTHON_LIB=.venv/Lib/site-packages/
PYTHONPATH:=$(PYTHONPATH);lib/site-packages;lib;../lib/site-packages;../lib
else
PYTHON27?=/usr/bin/python
NUKE_PYTHON?=python
PYTHON_LIB=$(abspath .venv/lib/python2.7/site-packages/)
PYTHONPATH:=$(PYTHONPATH):$(abspath lib/site-packages):$(abspath lib)
endif

export PYTHONPATH

# https://github.com/pypa/pip/issues/5735
lib/site-packages: export PIP_NO_BUILD_ISOLATION=false
lib/site-packages: requirements.txt
	rm -rf lib/site-packages
	"$(PYTHON27)" -m pip install -r requirements.txt --target lib/site-packages

docs/.git:
	git fetch -fn origin docs:docs
	git worktree add -f docs docs

docs/build/html/.git: docs/.git
	git fetch -fn origin gh-pages:gh-pages
	rm -rf docs/build/html
	git worktree add -f docs/build/html gh-pages

docs/*: docs/.git

docs/build/html: .venv/lib/site-packages lib/site-packages docs/build/html/.git
	. ./scripts/activate-venv.sh &&\
		"$(MAKE)" -C docs html

test: .venv/lib/site-packages lib/site-packages
	. ./scripts/activate-venv.sh &&\
		pytest tests

.venv:
	virtualenv --python "$(PYTHON27)" --clear .venv
	"$(NUKE_PYTHON)" -c 'import imp;import os;print(os.path.dirname(imp.find_module("nuke")[1]))' > "$(PYTHON_LIB)/nuke.pth"
	touch .venv

.venv/lib/site-packages: .venv dev-requirements.txt
	. ./scripts/activate-venv.sh &&\
		pip install -U -r dev-requirements.txt
	touch .venv/lib/site-packages
