install:
	pip install -r test_requirements.txt

release:
	git tag -a $(shell python -c "from django_inlinecss import __version__; print(__version__)") -m "$(m)"
	git push origin --tags
