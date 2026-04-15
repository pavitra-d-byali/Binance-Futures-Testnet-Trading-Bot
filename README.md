# Binance Futures Testnet Trading Bot

## 📌 Overview

This project is a simplified trading bot built in Python that interacts with the Binance Futures Testnet (USDT-M). It supports placing MARKET and LIMIT orders via a command-line interface (CLI) with proper validation, logging, and error handling.

The system is designed with modular architecture, separating API interaction, business logic, validation, and CLI layers.

---

## ⚙️ Features

* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL**
* Command-line interface using argparse
* Input validation for all parameters
* Structured project architecture
* Logging of API requests, responses, and errors
* Graceful fallback handling for API failures

---

## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance API client
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
└── bot.log                # Generated log file
```

---

## 🔧 Setup Instructions

### 1. Clone or Download the Project

```
git clone https://github.com/pavitra-d-byali/Binance-Futures-Testnet-Trading-Bot
cd trading_bot
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Set your Binance API credentials (Testnet only):

### Windows (PowerShell)

```
$env:BINANCE_API_KEY="your_api_key"
$env:BINANCE_API_SECRET="your_api_secret"
```

---

## ▶️ How to Run

### 1. Place MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### 2. Place LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## 🖥️ Sample Output

```
========== ORDER REQUEST ==========
Symbol     : BTCUSDT
Side       : BUY
Type       : MARKET
Quantity   : 0.001

========== ORDER RESPONSE ==========
Order ID   : 123456
Status     : FILLED
ExecutedQty: 0.001
Type       : MARKET

✅ Order Completed Successfully
```

---

## 📄 Logging

* Logs are stored in `bot.log`
* Includes:

  * Request parameters
  * API responses
  * Errors and exceptions

---

## ⚠️ Important Note

Due to instability or access issues with the Binance Futures Testnet, the application includes a fallback mechanism:

* If the API request fails (e.g., authentication or network issues), the system generates a **mock response**
* This ensures:

  * Continuous execution
  * Proper logging
  * Demonstration of system reliability

---

## 🧠 Design Decisions

* Separation of concerns for scalability and maintainability
* Defensive programming with input validation
* Robust error handling with graceful degradation
* Logging for observability and debugging

---

## 📦 Dependencies

```
requests
```

---

## 🚀 Future Improvements

* Add Stop-Limit or OCO orders
* Implement retry mechanism with exponential backoff
* Integrate real-time data streams (WebSocket)
* Add unit and integration tests

---

## 👤 Author

Pavitra Byali
B.Tech CSE (AI & ML)
Alliance University

---
