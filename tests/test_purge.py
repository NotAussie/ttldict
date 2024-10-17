from ttldict import TTLDict
import json
import time

dictionary = TTLDict()


def test():
    dictionary.set("c", 3, ttl=1)
    beforeSize = dictionary.__len__()

    time.sleep(2)

    dictionary.purge()
    afterSize = dictionary.__len__()  # Running after to allow purge to handle clearing

    assert beforeSize > afterSize, "purge (._cleanup()) did not purge expired key"
