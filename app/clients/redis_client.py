import redis

class RedisClient:
    def __init__(self):
        self.connection = redis.Redis(charset="utf-8", decode_responses=True)
