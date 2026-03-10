import redis
from app.config import settings

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

def get_url(code):
    return r.get(code)

def set_url(code, url):
    r.set(code, url)