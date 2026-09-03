# Mon Super Projet

Small FastAPI application used as a GitHub Actions teaching example.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Interactive docs: http://127.0.0.1:8000/docs

## Lint and test

```bash
ruff check .
ruff format --check .
pytest -v
```

## Continuous integration

`.github/workflows/ci.yaml` runs lint, format check and tests on every push and
pull request.
