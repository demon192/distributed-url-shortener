import redis

r = redis.Redis(host="localhost", port=6379)

def get_url(code):
    return r.get(code)

def set_url(code, url):
    r.set(code, url)