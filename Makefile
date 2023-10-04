install:
	poetry install

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

selfcheck:
	poetry check

check: selfcheck test lint

brain-games:
	poetry run brain-games

lint:
	poetry run flake8 brain_games

brain-even:
	poetry run brain-even

.PHONY: install test lint selfcheck check build