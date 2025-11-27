# Binance Futures Testnet Trading Bot

## Overview

A lightweight Python CLI tool that connects to Binance Futures **Testnet** and lets you place market, limit, and optional stop‑limit orders. It logs all API requests, responses, and errors to `bot.log` for easy debugging.

## Prerequisites

- Python 3.8+ installed
- Binance Futures Testnet account (create at https://testnet.binancefuture.com)
- API key and secret for the testnet account

## Setup

```bash
# Clone the repo (or copy the files you just received)
git clone <repo‑url>
cd trading_bot

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # on macOS/Linux
# or
# .\venv\Scripts\activate   # on Windows

# Install dependencies
pip install -r requirements.txt
```

## Configure API credentials

Create a `.env` file in the project root (it is ignored by git) with:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

The `bot/client.py` module reads these variables from the environment.

## Usage

```bash
# Market order (buy 0.001 BTCUSDT)
python cli.py market BTCUSDT 0.001 buy

# Limit order (sell 0.001 BTCUSDT at price 30000)
python cli.py limit BTCUSDT 0.001 30000 sell

# Stop‑limit order (buy 0.001 BTCUSDT, limit 31000, stop trigger 30500)
python cli.py stop BTCUSDT 0.001 31000 30500 buy
```

All commands print the raw Binance response on success or an error message on failure.

## Logging

All API interactions are written to `bot.log` (INFO level). Errors are logged with the ERROR level.

## Verification

1. Set your API keys in `.env`.
2. Run a market order – you should see an order ID in the output and a corresponding entry in `bot.log`.
3. Try a limit order – verify the order appears with the correct price.
4. (Optional) Test the stop‑limit command.

## How to Quit / Deactivate

The bot runs a single command and exits automatically, so you don't need to press anything to stop it.
When you are done using the bot and want to leave the virtual environment, simply type:

```bash
deactivate
```

## Beginner's Guide

If you are new to coding or trading, check out [beginner_guide.md](beginner_guide.md) for a simple explanation of how this bot works.
We have also added detailed comments to the code files (`cli.py`, `bot/client.py`, `bot/orders.py`) to help you learn!

## License

MIT – feel free to modify and extend.
