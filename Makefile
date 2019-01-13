.PHONY: test

test:
	pipenv run lint
	pipenv run test
