import requests
import configuration
import data

def get_order():
    req = requests.post(url=configuration.URL_SERVICE + configuration.CREATE_Orders,
                        json=data.body).json()["track"]
    return req

def order_by_track(get_order):
    req = requests.get(url=configuration.URL_SERVICE + configuration.GET_ORDERS + get_order)
    return req