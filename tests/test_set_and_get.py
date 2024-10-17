from ttldict import TTLDict

dicty = dict()
dicty.update

dictionary = TTLDict()


def test():
    dictionary.set("a", 1, ttl=5)
    assert dictionary.get("a") == 1, "key value did not match expected .get() result"
