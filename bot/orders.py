"""Order helper functions.
Each function receives a `client` instance from `client.py` and returns the
raw Binance response (a dict). Errors are caught, logged and re‑raised as
`RuntimeError` so the CLI can display a friendly message.
"""

import logging
from binance.exceptions import BinanceAPIException

logger = logging.getLogger(__name__)

def place_market_order(client, symbol: str, quantity: float, side: str):
    """Place a market order.
    `side` must be either "BUY" or "SELL" (case‑insensitive).
    """
    # 1. Validate the side (must be BUY or SELL)
    side = side.upper()
    if side not in ("BUY", "SELL"):
        raise ValueError('side must be BUY or SELL')
    try:
        # 2. Send the order to Binance
        # "MARKET" means "buy/sell immediately at the best available price"
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        # 3. Log the success
        logger.info('Market order placed: %s', order)
        return order
    except BinanceAPIException as e:
        # 4. If something goes wrong (e.g., not enough funds), log it and tell the user
        logger.error('Market order error: %s', e)
        raise RuntimeError(f'Binance API error: {e}')

def place_limit_order(client, symbol: str, quantity: float, price: float, side: str, time_in_force: str = 'GTC'):
    """Place a limit order.
    `time_in_force` defaults to Good‑Till‑Cancelled.
    """
    side = side.upper()
    if side not in ("BUY", "SELL"):
        raise ValueError('side must be BUY or SELL')
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            timeInForce=time_in_force,
            quantity=quantity,
            price=str(price)  # Binance expects price as string
        )
        logger.info('Limit order placed: %s', order)
        return order
    except BinanceAPIException as e:
        logger.error('Limit order error: %s', e)
        raise RuntimeError(f'Binance API error: {e}')

# OPTIONAL: Stop‑Limit order (bonus)
def place_stop_limit_order(client, symbol: str, quantity: float, price: float, stop_price: float, side: str, time_in_force: str = 'GTC'):
    """Place a stop‑limit order (bonus implementation)."""
    side = side.upper()
    if side not in ("BUY", "SELL"):
        raise ValueError('side must be BUY or SELL')
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='STOP',
            timeInForce=time_in_force,
            quantity=quantity,
            price=str(price),
            stopPrice=str(stop_price)
        )
        logger.info('Stop‑Limit order placed: %s', order)
        return order
    except BinanceAPIException as e:
        logger.error('Stop‑Limit order error: %s', e)
        raise RuntimeError(f'Binance API error: {e}')
