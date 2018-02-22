import requests

# Список сделок по валютной паре


def trad(name):
    get = requests.get('https://api.exmo.com/v1/trades/?pair=' + name)
    get = (get.json())
    return get

# Книга ордеров по валютной паре


def order(name, limit):
    get = requests.get('https://api.exmo.com/v1/order_book/?pair=' + name + '&limit=' + str(limit))
    get = (get.json())
    return get

# Cтатистика цен и объемов торгов по валютным парам


def ticker():
    get = requests.get('https://api.exmo.com/v1/ticker/')
    get = (get.json())
    return get

# Настройки валютных пар


def settings():
    get = requests.get('https://api.exmo.com/v1/pair_settings/')
    get = (get.json())
    return get

# Cписок валют биржи


def currency():
    get = requests.get('https://api.exmo.com/v1/currency/')
    get = (get.json())
    return get


class pair:
    def __init__(self, name, limit=10, command='ask_top'):
        self.name = name
        self.limit = limit
        self.command = command

    # high - максимальная цена сделки за 24 часа
    # low - минимальная цена сделки за 24 часа
    # avg - средняя цена сделки за 24 часа
    # vol - объем всех сделок за 24 часа
    # vol_curr - сумма всех сделок за 24 часа
    # last_trade - цена последней сделки
    # buy_price - текущая максимальная цена покупки
    # sell_price - текущая минимальная цена продажи
    # updated - дата и время обновления данных
    def ticker(self):
        get = requests.get('https://api.exmo.com/v1/ticker/')
        get = (get.json())
        return get[self.name]

    # min_quantity - минимальное кол-во по ордеру
    # max_quantity - максимальное кол-во по ордеру
    # min_price - минимальная цена по ордеру
    # max_price - максимальная цена по ордеру
    # min_amount - минимальная сумма по ордеру
    # max_amount - максимальная сумма по ордеру
    def settings(self):
        get = requests.get('https://api.exmo.com/v1/pair_settings/')
        get = (get.json())
        return get[self.name]

    # ask_quantity - объем всех ордеров на продажу
    # ask_amount - сумма всех ордеров на продажу
    # ask_top - минимальная цена продажи
    # bid_quantity - объем всех ордеров на покупку
    # bid_amount - сумма всех ордеров на покупку
    # bid_top - максимальная цена покупки
    # bid - список ордеров на покупку, где каждая строка это цена, количество и сумма
    # ask - список ордеров на продажу, где каждая строка это цена, количество и сумма
    def order_book(self, command):
        self.command = command
        data = order(self.name, self.limit)[self.name][self.command]
        return data

    # trade_id - идентификатор сделки
    # type - тип сделки
    # price - цена сделки
    # quantity - кол-во по сделке
    # amount - сумма сделки
    # date - дата и время сделки в формате Unix
    def trades(self):
        data = trad(self.name)[self.name]
        return data

