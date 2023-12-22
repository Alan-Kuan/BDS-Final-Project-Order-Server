# Big Data System: Final Project - Order API Server
## Prerequisites
- The project is managed by [**Poetry**](https://python-poetry.org/). Make sure it's installed.
- Run `poetry install` at the project's root.

## Usage
Development mode:
```sh
poetry run python3 ./main.py dev
```

Production mode:
```sh
poetry run python3 ./main.py prod <API Host Root>
```

`<API Host Root>` will be filled in OpenAPI Spec's `servers` section.

E.g.,
```sh
poetry run python3 ./main.py prod https://example.com
```
