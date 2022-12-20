import pytest


def test_add_passing():
    assert (1, 2, 3) == (1, 2, 3)


def test_add_failing():
    assert (1, 2, 3) == (3, 2, 1)


def test_custom_failing():
    pytest.fail()
