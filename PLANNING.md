# All

- [ ] README
- [ ] Postman collection
- [ ] seed data

# Web API

- [x] backend only, use flask, json interface
- [x] env
- [x] simple database to persist player info - start with sqlite, keep it simple
- [x] config
- [X] routes
- [X] models
- [x] player CRUD endpoints
- [x] controllers
- [x] sql alchemy setup
- [x] migrations
- [x] model validators
- [x] battle endpoint
- [x] enqueue battles
- [x] add score to player model
- [x] leaderboard endpoint
- [x] redis implementation of leaderboard fetching
- [ ] tests

# Battle Processor

- [x] ~worker app~ containing within the main app
- [x] queue system [redis queue](https://python-rq.org/)
- [ ] process integrity requirements
- [ ] pass battles to the engine
- [ ] update players
- [ ] update leaderboard

# Battle Engine

- [ ] Battle logic
