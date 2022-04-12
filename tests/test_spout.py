import json
import os

from technobabble import Babbler


def test_spout_softly_is_in_lowercase():
    babble = Babbler.spout_softly()
    lowered_babble = "".join([c.lower() for c in babble])
    assert babble == lowered_babble


def test_spout_is_in_wanted_list():
    with open(os.path.join(os.path.dirname(__file__), "test_data", "should_have_babbles.json"), "r") as file:
        data = json.load(file)
    for i in range(300):
        assert Babbler.spout() in data
