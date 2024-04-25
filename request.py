import requests
import configuration
import data


def create_order():
    return requests.post(
        url=configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=data.body
    )


def order_by_track(track):
    return requests.get(
        url=configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + track
    )
