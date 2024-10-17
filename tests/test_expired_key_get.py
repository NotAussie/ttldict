from ttldict import TTLDict
import pytest
import time

dictionary = TTLDict()


def test():
    dictionary.set("a", 1, 2)
    time.sleep(2.5)
    assert dictionary.get("a") == None, "expired key did not get collected"
