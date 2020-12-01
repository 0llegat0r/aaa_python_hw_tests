#!/bin/zsh
pip install -r requirements.txt
python -m doctest -v -o IGNORE_EXCEPTION_DETAIL issue1.py
python -m pytest issue2.py
python -m unittest issue3.py
python -m pytest issue4.py
coverage run -m unittest issue5.py && coverage report && coverage html