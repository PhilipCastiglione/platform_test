# Platform Test

## Implemented

* Back end API, MVC style
    * Heartbeat endpoint for testing & monitoring
* Player modeling
    * SQL database with migrations
    * Create (and Show, for debugging) endpoint
* Battle initiation
    * queued for async processing using redis queue
* Leaderboard implementation
    * uses a redis sorted set so this is fast

## Out of Scope (Also known as: things I didn't get to in time!)

* Battle processor & battle engine logic, this looked fun, but I didn't get there
* Auth (I like basic auth headers and JWTs for authz policies, can use redis cache to make this fast, bring it into middleware)
* Hosting
* Deployment (and CI/CD)

I might have done more, but I wanted to do things to a reasonable standard and Python isn't my native language. Overall I'm happy with what I achieved; I aimed for extensibility and believe it would be pretty easy to keep working on this application and smooth the rough edges to make it production-ready.

## Tools

* `pipenv` – environment & dependency management
* `git` - source control
* `asdf` - language version management
* `postman` - API development & QA
* `vscode` – code editor
* `macOS` - Mojave 10.14.6

## Technology Choices

* `python` - 3.6.7
* `flask` – web framework
* `sqllite` – db (not acceptable for production, it's gitignored to make the demo convenient)
* `SQLAlchemy` – ORM
* `flask migrate` - db schema migrations
* `pytest` - test runner
* `pylint` - (editor integrated) linting
* `redis queue` - async battle processing
* `redis` - 4.0.2 powers the queue, provides fast access & convenient data structures for leaderboard
* `dotenv` - secrets are injected into the application environment and excluded from the git repo

## Usage

Install deps (and any required tools not installed):

```
pipenv install
```

Establish .env from .env sample:

```
cp .env.sample .env
```

Create database & run migrations for dev and test dbs:

```
pipenv run flask db upgrade
TESTING=1 pipenv run flask db upgrade
```

You will need to start Redis in whatever way appropriate for your system. I am using [RedisApp](https://github.com/jpadilla/redisapp).

Run tests:

```
pipenv run pytest
```

Run the web server:

```
pipenv run python app.py
```

Import the postman collection into postman, then try out the requests!
