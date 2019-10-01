# Platform Test

## Tools

`pipenv` – environment & dependency management
`git` - source control
`asdf` - language version management
`postman` - API development & QA
`vscode` – code editor

## Technology Choices

`python` - 3.6.7
`flask` – web framework
`sqllite` – db (not acceptable for production)
`SQLAlchemy` – ORM
`flask migrate` - db schema migrations
`pytest` - test runner
`pylint` - lintint

## Usage

install deps

some way to test the api - without postman?
.env from .env sample

Create database & run migrations:

```
pipenv run flask db init
pipenv run flask db upgrade
```

NOT THIS: pipenv run flask db migrate