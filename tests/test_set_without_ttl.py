from ttldict import TTLDict
import time

dictionary = TTLDict()


def test():
    dictionary.set("b", 2)
    assert dictionary.get("b") == 2
