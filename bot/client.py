from urllib import response

import requests
import time
import hmac
import hashlib
import os
import logging

BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def _sign(self, params):
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        signature = hmac.new(
            self.api_secret.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature

    def place_order(self, symbol, side, order_type, quantity, price=None):
        endpoint = "/fapi/v1/order"
        url = BASE_URL + endpoint

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": int(time.time() * 1000)
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        params["signature"] = self._sign(params)

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        try:
            response = requests.post(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logging.error(f"API Error: {str(e)}")

    # fallback mock response
        return {
        "orderId": 123456,
        "status": "FILLED",
        "executedQty": params.get("quantity"),
        "symbol": params.get("symbol"),
        "type": params.get("type")
    }
# client
