import request


# Ерченко Кристина, 15-я когорта — Финальный проект. Инженер по тестированию плюс
def in_autotests_we_trust(a, b):
    if a == b:
        print('Тест пройден')
    else:
        print('Тест провален')


create_order_response = request.create_order()
track_id = str(create_order_response.json()["track"])
order_response = request.order_by_track(track_id)
in_autotests_we_trust(order_response.status_code, 200)
