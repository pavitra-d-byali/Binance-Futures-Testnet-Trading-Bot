from bot.client import BinanceClient
from bot.validators import validate_order

def execute_order(client, symbol, side, order_type, quantity, price=None):
    validate_order(symbol, side, order_type, quantity, price)
    return client.place_order(symbol, side, order_type, quantity, price)
# orders
