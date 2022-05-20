# apiTools.py
# Written by ef1500
# API tools
# Adds functions like Refresh, etc
# Adds more functionality for APIs
from cachetools import TTLCache

def refreshValue(interval):
    """
    Decorator to refresh a value after a certain time. This is great if you want to
    refresh a token every hour, for example.
    example usage: 
    @refreshvalue(100)
    getToken(apiQuery)
    """
    @TTLCache(maxsize=1, ttl=interval)
    def refreshvalue(func, *args, **kwargs):
        return func(*args, **kwargs)
    return refreshValue

