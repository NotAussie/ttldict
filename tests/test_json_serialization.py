from ttldict import TTLDict
import json
import time

dictionary = TTLDict()


def test():
    dictionary.set("c", 3, ttl=10)
    data = json.dumps(dictionary)
    assert data == '{"c": 3}'
