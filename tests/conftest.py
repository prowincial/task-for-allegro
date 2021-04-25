import pytest
from mserver import api

def test_user_request():
    assert api.user_exists("allegro") == True
    assert api.user_exists("samara228") == True
    assert api.user_exists("pochemutakslozhnohmmmm") == True




