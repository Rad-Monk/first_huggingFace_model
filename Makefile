install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -vvv --cov=app 

debug:
	python -m pytest -vv --pdb