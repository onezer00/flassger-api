.DEFAULT: help

help:
	@echo "make clean-build"
	@echo "       Clear all build directories"
	@echo "make isort"
	@echo "       run isort command cli in development features"
	@echo "make run"
	@echo "       run the web application"

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

isort:
	sh -c "isort --skip-glob=.tox --recursive . "

run:
	python main.py