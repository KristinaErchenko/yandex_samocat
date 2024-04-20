import request
# Ерченко Кристина, 15-я когорта — Финальный проект. Инженер по тестированию плюс
def in_autotests_we_trust(a, b):
    if a == b:
        print('Тест пройден')
    else:
        print('Тест провален')

order = request.get_order()
s = str(order)
track = request.order_by_track(s)
code = track.status_code
in_autotests_we_trust(code, 200)