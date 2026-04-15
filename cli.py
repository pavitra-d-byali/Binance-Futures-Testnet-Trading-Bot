import argparse
import os
from bot.client import BinanceClient
from bot.orders import execute_order
from bot.logging_config import setup_logger

setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("Set BINANCE_API_KEY and BINANCE_API_SECRET as environment variables")

    client = BinanceClient(api_key, api_secret)

    print("Placing Order...")
    print(vars(args))

    try:
        response = execute_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )
        print("Order Successful")
        print(response)
    except Exception as e:
        print("Order Failed:", str(e))

if __name__ == "__main__":
    main()
# CLI
