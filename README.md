# Binance Futures Testnet Trading Bot

## Setup
1. Create Binance Futures Testnet account
2. Generate API keys
3. Set environment variables:

```
export BINANCE_API_KEY=your_key
export BINANCE_API_SECRET=your_secret
```

4. Install dependencies:
```
pip install -r requirements.txt
```

## Run Examples

### Market Order
```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order
```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

## Assumptions
- Only USDT-M futures supported
- Simple validation only
# Binance-Futures-Testnet-Trading-Bot
