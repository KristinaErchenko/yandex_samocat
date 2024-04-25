import pytest
import main
from request import create_order, order_by_track


def test_status_200():
    new_order_response = create_order()
    track_id = str(new_order_response.json()["track"])
    order_response = order_by_track(track_id)
    assert order_response.status_code == 200
