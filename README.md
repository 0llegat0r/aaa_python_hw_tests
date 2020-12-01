```shell script
pip install -r requirements.txt
```

- issue1: 
```shell script
python -m doctest -v -o IGNORE_EXCEPTION_DETAIL issue1.py
```
- issue2: 
```shell script
python -m pytest issue2.py
```
> 
- issue3:
```shell script
python -m unittest issue3.py
```
- issue4:
```shell script
python -m pytest issue4.py
```
- issue5:
```shell script
coverage run -m unittest issue5.py && coverage report && coverage html
```