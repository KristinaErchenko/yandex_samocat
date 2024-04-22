import pytest
import main

def test_status_200():
    code = main.code
    assert code == 200